from django.urls import path
from api import views

urlpatterns = [
    path('about/',views.about.as_view()),
    path('education/',views.education.as_view()),
    path('projects/',views.Projects.as_view()),
    path('skills/',views.skills.as_view()),
    path('certificate/',views.certification.as_view()),
]
