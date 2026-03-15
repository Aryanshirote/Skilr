from django.urls import path
from dashboards.views import *

urlpatterns = [
    path('', home, name="home"),
    path("dasboard/", dashboard, name="dashboard"),
    path("resume-score/<int:id>/", resume_score, name="resume_score"),
    path("skill-gap/<int:id>/", skill_gap, name="skill_gap"),
    # path("job-match/<int:id>/", job_match, name="job_match"),
]