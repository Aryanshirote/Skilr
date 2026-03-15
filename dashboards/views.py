from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from analytics.models import Resume

# -------------------------------------------------------
# HOME VIEW
# -------------------------------------------------------

def home(request):
    return render (request, 'home.html')

# -------------------------------------------------------
# DASHBOARD VIEW
# -------------------------------------------------------

@login_required
def dashboard(request):

    resumes = Resume.objects.filter(user=request.user)

    total_resumes = resumes.count()

    latest_score = 0
    total_skills = 0
    skill_gaps = 0

    if resumes.exists():

        latest = resumes.last()

        skills = latest.skills.split(",")

        total_skills = len(skills)

        # simple scoring logic
        latest_score = min(total_skills * 10, 100)

        required_skills = [
            "python","sql","django","machine learning",
            "data structures","git"
        ]

        skill_gaps = len([
            skill for skill in required_skills
            if skill not in [s.strip().lower() for s in skills]
        ])

    return render(request,"dashboard.html",{
        "resumes":resumes,
        "total_resumes":total_resumes,
        "latest_score":latest_score,
        "total_skills":total_skills,
        "skill_gaps":skill_gaps
    })


def resume_score(request, id):

    resume = Resume.objects.get(id=id)

    skills = resume.skills.split(",")

    score = min(len(skills) * 8, 100)

    return render(request,"resume_score.html",{
        "resume":resume,
        "score":score
    })

def skill_gap(request,id):

    resume = Resume.objects.get(id=id)

    resume_skills = [s.strip().lower() for s in resume.skills.split(",")]

    required = [
    "python",
    "sql",
    "django",
    "machine learning",
    "data structures",
    "git"
    ]

    missing = []

    for skill in required:
        if skill not in resume_skills:
            missing.append(skill)

    return render(request,"skill_gap.html",{
        "missing":missing,
        "resume_skills":resume_skills
    })


# def job_match(request,id):

#     resume = Resume.objects.get(id=id)

#     skills = resume.skills.lower()

#     jobs = [
#     "Python Django Developer with SQL",
#     "Frontend Developer React HTML CSS",
#     "Data Analyst Python Pandas SQL"
#     ]

#     matches = []

#     for job in jobs:

#         score = 0

#         for skill in resume.skills.split(","):
#             if skill.lower() in job.lower():
#                 score += 10

#         matches.append((job,score))

#     return render(request,"job_match.html",{
#         "matches":matches
#     })