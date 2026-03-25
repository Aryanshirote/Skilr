import pdfplumber
import pandas as pd
import spacy
import re

from sklearn.metrics.pairwise import cosine_similarity
import pytesseract
from pdf2image import convert_from_path

from PIL import Image



pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Lenovo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
def extract_text_ocr(pdf_path):

    images = convert_from_path(
        pdf_path,
        poppler_path=r"C:\Users\Lenovo\Downloads\Release-25.12.0-0\poppler-25.12.0\Library\bin"
    )

    text = ""

    for img in images:
        text += pytesseract.image_to_string(img)

    return text

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Load skills dataset
skills_df = pd.read_csv("analytics/skills.csv")
skills_list = skills_df["skill"].str.lower().tolist()


def analyze_resume(resume):

    text = ""

    # Extract text from PDF
    with pdfplumber.open(resume.file.path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    text_lower = text.lower()

    # NLP processing
    doc = nlp(text_lower)

    found_skills = set()

    # Detect skills
    for token in doc:
        if token.text in skills_list:
            found_skills.add(token.text)

    # Also detect multi-word skills
    for skill in skills_list:
        if skill in text_lower:
            found_skills.add(skill)

    # Save to database
    resume.extracted_text = text
    resume.skills = ", ".join(sorted(found_skills))
    resume.save()

    embedding = get_embedding(text)

    resume.embedding = embedding.tolist()
    resume.save()

    roles = predict_roles(text)


def extract_email(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    match = re.findall(pattern, text)
    return match[0] if match else None

def extract_phone(text):
    pattern = r'\+?\d[\d\s]{8,15}'
    match = re.findall(pattern, text)
    return match[0] if match else None

def extract_skills(text, skills_list):

    text_lower = text.lower()
    found = set()

    for skill in skills_list:
        if skill in text_lower:
            found.add(skill)

    return list(found)


from spacy.matcher import PhraseMatcher

def skill_matcher(text, skills):

    doc = nlp(text.lower())

    matcher = PhraseMatcher(nlp.vocab)
    patterns = [nlp.make_doc(skill) for skill in skills]

    matcher.add("SKILLS", patterns)

    matches = matcher(doc)

    detected = set()

    for match_id, start, end in matches:
        detected.add(doc[start:end].text)

    return list(detected)

# =========================================================
# Detect Skill Gap
# =========================================================

def detect_skill_gap(resume_skills, job_description, skills_list):

    job_skills = []

    text = job_description.lower()

    for skill in skills_list:
        if skill in text:
            job_skills.append(skill)

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    missing_skills = job_set - resume_set

    return list(missing_skills)

def calculate_score(skills):

    score = 0

    important_skills = [
        "python",
        "sql",
        "data structures",
        "machine learning",
        "django"
    ]

    for skill in skills:
        if skill in important_skills:
            score += 15

    return min(score, 100) 


# ---------------------------------------
# embbdedings
# ---------------------------------------
model = None

def get_model():
    global model
    if model is None:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model

def get_embedding(text):
    model = get_model()
    return model.encode(text)

def match_jobs(resume_text, job_descriptions):

    model = get_model()

    resume_embedding = model.encode([resume_text])

    job_embeddings = model.encode(job_descriptions)

    scores = cosine_similarity(resume_embedding, job_embeddings)

    return scores


# ----------------------------------------------------------------------
# API integration
# ----------------------------------------------------------------------

import requests

APP_ID = "bcce1fa6"
APP_KEY = "238921f096811494fea7cf0715111b03"

def fetch_jobs(skills):

    query = " ".join(skills[:3])

    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": query,
        "results_per_page": 10
    }

    response = requests.get(url, params=params)
    data = response.json()

    jobs = []

    for job in data.get("results", []):

        jobs.append({
            "title": job.get("title", "No Title"),
            "company": job.get("company", {}).get("display_name", "Unknown Company"),
            "location": job.get("location", {}).get("display_name", "Not specified"),
            "url": job.get("redirect_url", "#"),
            "description": job.get("description", "No description available")
        })

    return jobs

# -----------------------------------------------------
# JOB MATCH LOGIC
# -----------------------------------------------------
def calculate_match(resume_text, job_description):

    model = get_model()

    resume_embedding = model.encode([resume_text])
    job_embedding = model.encode([job_description])

    score = cosine_similarity(resume_embedding, job_embedding)[0][0]

    return round(score * 100, 2)


# ========================================================================
# Role Profiles
# ========================================================================

ROLE_PROFILES = {
    "Data Scientist": """
    Machine learning, statistics, Python, pandas, numpy,
    data analysis, deep learning, AI, model training
    """,

    "Backend Developer": """
    Python, Django, APIs, backend systems,
    databases, REST APIs, server-side development
    """,

    "Data Analyst": """
    SQL, Excel, Power BI, Tableau,
    data visualization, business intelligence
    """,

    "Frontend Developer": """
    HTML, CSS, JavaScript, React,
    UI development, web design
    """,

    "DevOps Engineer": """
    Docker, Kubernetes, AWS,
    CI/CD pipelines, infrastructure automation
    """
}

from sklearn.metrics.pairwise import cosine_similarity


def predict_roles(resume_text):

    model = get_model()

    resume_embedding = model.encode([resume_text])

    roles = []
    role_descriptions = list(ROLE_PROFILES.values())
    role_names = list(ROLE_PROFILES.keys())

    role_embeddings = model.encode(role_descriptions)

    scores = cosine_similarity(resume_embedding, role_embeddings)[0]

    for i, score in enumerate(scores):

        roles.append({
            "role": role_names[i],
            "score": round(score * 100, 2)
        })

    roles.sort(key=lambda x: x["score"], reverse=True)

    return roles[:3]




from .job_data import JOB_ROLES, COMMON_SKILLS, CORE_WEIGHT, COMMON_WEIGHT


def normalize_skills(skills_text):
    """
    Convert resume skills into clean list
    """
    skills = skills_text.lower().replace(",", " ").split()
    return list(set(skills))
def calculate_weighted_score(user_skills, role_skills):

    # Normalize
    user_set = set([s.lower().strip() for s in user_skills])
    role_set = set([s.lower().strip() for s in role_skills])
    common_set = set([s.lower().strip() for s in COMMON_SKILLS])

    # CORE MATCH
    core_matched = user_set & role_set
    core_missing = role_set - user_set

    #  NEW CORE SCORE (BALANCED)
    if len(user_set) + len(role_set) == 0:
        core_score = 0
    else:
        core_score = (2 * len(core_matched)) / (len(user_set) + len(role_set))

    # COMMON MATCH
    common_matched = user_set & common_set

    #  Reduce importance of common skills
    if len(common_set) == 0:
        common_score = 0
    else:
        common_score = len(common_matched) / len(common_set)

    # FINAL SCORE (CORE dominates)
    final_score = (core_score * 0.8) + (common_score * 0.2)

    return {
        "final_score": round(final_score * 100, 2),
        "core_matched": list(core_matched),
        "core_missing": list(core_missing),
        "common_matched": list(common_matched)
    }

def get_job_matches(user_skills, industry):
    """
    Returns all job matches for selected industry
    """

    results = []

    industry_jobs = JOB_ROLES.get(industry, {})

    for role, role_skills in industry_jobs.items():

        score_data = calculate_weighted_score(user_skills, role_skills)

        results.append({
            "role": role,
            "score": score_data["final_score"],
            "core_matched": score_data["core_matched"],
            "core_missing": score_data["core_missing"],
            "common_matched": score_data["common_matched"]
        })

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)

    return results

