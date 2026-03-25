
import matplotlib.pyplot as plt
import matplotlib

from analytics.job_data import JOB_ROLES
matplotlib.use('Agg')
from collections import Counter
import os


from analytics.services import calculate_weighted_score, normalize_skills

def generate_skill_chart(skills, username):
    if not skills:
        return None

    # Count frequency
    skill_counts = Counter(skills)

    labels = list(skill_counts.keys())
    values = list(skill_counts.values())

    # Create plot
    plt.figure()
    plt.bar(labels, values)
    plt.xticks(rotation=30)

    # Save image
    file_path = f"media/charts/{username}_skills.png"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    plt.savefig(file_path, bbox_inches='tight')
    plt.close()

    return file_path

def calculate_score(skills):
    return min(len(skills) * 10, 100)


def generate_score_chart(resumes, username):
    

    scores = []
    labels = []

    for i, resume in enumerate(resumes):
        skills = normalize_skills(resume.skills)

        score = calculate_resume_score(
            skills,
            resume.user.profile.industry
    )

        scores.append(score)
        labels.append(f"R{i+1}")

    plt.figure()
    plt.plot(labels, scores, marker='o')

    plt.xlabel("Resumes")
    plt.ylabel("Score")
    plt.title("Resume Improvement")

    file_path = f"media/charts/{username}_score.png"
    plt.savefig(file_path)
    plt.close()

    return file_path

def generate_skill_growth_chart(resumes, username):
    import matplotlib.pyplot as plt

    counts = []
    labels = []

    for i, resume in enumerate(resumes):
        skills = normalize_skills(resume.skills)

        counts.append(len(set(skills)))
        labels.append(f"R{i+1}")

    plt.figure()
    plt.plot(labels, counts, marker='o')

    plt.xlabel("Resumes")
    plt.ylabel("Number of Skills")
    plt.title("Skills Growth")

    file_path = f"media/charts/{username}_skills_growth.png"
    plt.savefig(file_path)
    plt.close()

    return file_path



def calculate_resume_score(user_skills, industry):
    industry_jobs = JOB_ROLES.get(industry, {})

    best_score = 0

    for role, role_skills in industry_jobs.items():
        score_data = calculate_weighted_score(user_skills, role_skills)

        if score_data["final_score"] > best_score:
            best_score = score_data["final_score"]

    return best_score