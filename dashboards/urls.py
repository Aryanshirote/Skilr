from django.urls import path
from dashboards.views import *

urlpatterns = [
    path('', home, name="home"),
    path("dasboard/", dashboard, name="dashboard"),
    path("resume-score/<int:id>/", resume_score, name="resume_score"),
    path("skill-gap/<int:id>/", skill_gap, name="skill_gap"),
    path("resume_history/", resume_history, name="resume_history"),
    path("about/", about, name="about"),
    path("feedback/", feedback_view, name="feedback"),
    path("charts/",  charts, name="charts"),
    
]