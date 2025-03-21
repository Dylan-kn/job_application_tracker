from django.urls import path
from .views import job_list, add_job, edit_job, delete_job

urlpatterns = [
    path('', job_list, name="job_list"),
    path('add/', add_job, name="add_job"),
    path('edit/<int:job_id>/', edit_job, name="edit_job"),
    path('delete/<int:job_id>/', delete_job, name="delete_job"),
]
