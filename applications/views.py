from django.shortcuts import render, redirect
from .models import JobApplication
from .forms import JobApplicationForm


def job_list(request):
    jobs = JobApplication.objects.all()
    return render(request, "applications/job_list.html", {"jobs": jobs})


def add_job(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("job_list")
    else: 
        form = JobApplicationForm()

    return render(request, "applications/add_job.html", {"form": form})


