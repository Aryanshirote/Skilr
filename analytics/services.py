import pdfplumber
import pandas as pd
import spacy
import re

from sklearn.metrics.pairwise import cosine_similarity
import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Lenovo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

import pytesseract
from PIL import Image

img = Image.open("static/images/bg2.png")

text = pytesseract.image_to_string(img)

print(text)
from pdf2image import convert_from_path
import pytesseract


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

    query = " ".join(skills[:3])   # use top skills

    url = f"https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": query,
        "results_per_page": 10
    }

    response = requests.get(url, params=params)

    data = response.json()

    jobs = []

    for job in data["results"]:

        jobs.append({
            "title": job["title"],
            "company": job["company"]["display_name"],
            "location": job["location"]["display_name"],
            "url": job["redirect_url"],
            "description": job["description"]
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




