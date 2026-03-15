from django.shortcuts import render, redirect
from .models import Resume
from .services import analyze_resume
from django.contrib.auth.decorators import login_required


@login_required
def upload_resume(request):

    if request.method == "POST" and request.FILES.get("file_upload"):

        resume = Resume.objects.create(
            user=request.user,
            file=request.FILES["file_upload"]
        )

        # Run analysis
        analyze_resume(resume)

        return redirect("dashboard")

    return render(request, "fileupload.html")


from .services import fetch_jobs, calculate_match
from .models import Resume


def job_match(request, id):

    resume = Resume.objects.get(id=id)

    resume_text = resume.extracted_text
    skills = [s.strip() for s in resume.skills.split(",")] if resume.skills else []

    jobs = fetch_jobs(skills)

    results = []

    for job in jobs:

        score = calculate_match(resume_text, job["description"])
        results.append({
            "title": job["title"],
            "company": job["company"],
            "location": job["location"],
            "url": job["url"],
            "score": score
        })

    return render(request, "job_match.html", {
        "jobs": results,
        "resume": resume
    })