from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from analytics.models import Resume
from analytics.services import normalize_skills, get_job_matches
from dashboards.models import Feedback 
# -------------------------------------------------------
# HOME VIEW
# -------------------------------------------------------



def home(request):
    total_resumes = Resume.objects.count()
    total_jobs = total_resumes * 3  

    testimonials = Feedback.objects.filter(rating__gte=4).order_by('-created_at')[:4]

    context = {
        "total_resumes": total_resumes,
        "total_jobs": total_jobs,
        "placements": int(total_resumes * 0.25),
        "testimonials": testimonials
    }

    return render(request, "home.html", context)

@login_required
def dashboard(request):
    user = request.user
    profile = user.profile

    resume = Resume.objects.filter(user=user).last()

    job_results = []
    best_match = None
    total_resumes = Resume.objects.filter(user=user).count()

    if resume and resume.skills:
        user_skills = normalize_skills(resume.skills)

        print("🔥 DEBUG START")
        print("Skills:", user_skills)
        print("Industry:", profile.industry)
        
        job_results = get_job_matches(
            user_skills,
            profile.industry.lower()
        )

        if job_results:
            best_match = job_results[0]

    return render(request, "dashboard.html", {
        "total_resumes": total_resumes,
        "job_results": job_results[:5],
        "best_match": best_match
    })

def resume_score(request, id):

    resume = Resume.objects.get(id=id)

    skills = resume.skills.split(",")

    score = min(len(skills) * 8, 100)

    resume.skill_list = resume.skills.split(",")

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

def resume_history(request):
    
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

    return render(request,"resume_history.html",{
        "resumes":resumes,
        "total_resumes":total_resumes,
        "latest_score":latest_score,
        "total_skills":total_skills,
        "skill_gaps":skill_gaps
    })
    


from .models import Feedback


from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib.auth.decorators import login_required


@login_required
def feedback_view(request):

    if request.method == "POST":

        category = request.POST.get("category")
        rating = request.POST.get("rating")
        message = request.POST.get("message")
        screenshot = request.FILES.get("screenshot")

        Feedback.objects.create(
            user=request.user,
            category=category,
            rating=rating,
            message=message,
            screenshot=screenshot
        )

        return render(request,"feedback.html",{"success":True})

    return render(request,"feedback.html")


def about(request):
    return render(request,"about.html")

 
from django.contrib.auth.decorators import login_required
from analytics.models import Resume
from analytics.utils import *

@login_required
def charts(request):
    resumes = Resume.objects.filter(user=request.user).order_by("uploaded_at")

    if not resumes:
        return render(request, "charts.html", {"error": "No resumes found"})

    
    score_chart = generate_score_chart(resumes, request.user.username)
    skill_chart = generate_skill_growth_chart(resumes, request.user.username)

    return render(request, "charts.html", {
        "score_chart": score_chart,
        "skill_chart": skill_chart
    })