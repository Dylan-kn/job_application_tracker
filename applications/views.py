from django.shortcuts import render, redirect, get_object_or_404
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


def edit_job(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id)

    if request.method == "POST":
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect("job_list")
    else:
        form = JobApplicationForm(instance=job)

    return render(request, "applications/edit_job.html", {"form": form, "job": job})


def delete_job(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id)

    if request.method == "POST":
        job.delete()
        return redirect("job_list")
    
    return render(request, "applications/delete_job.html", {"job": job})