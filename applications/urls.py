from django.urls import path
from .views import job_list, add_job

urlpatterns = [
    path('', job_list, name="job_list"),
    path('add/', add_job, name="add_job"),
]

print("DEBUG: applications.urls loaded ->", urlpatterns)