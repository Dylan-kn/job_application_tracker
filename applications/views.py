from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from .forms import JobApplicationForm
import requests
from django.conf import settings



def job_list(request):
    jobs = JobApplication.objects.all()

    weather_data = {}
    for job in jobs:
        if job.city:
            try:
                weather_api_key = settings.OPENWEATHERMAP_API_KEY
                weather_url = (
                    f"http://api.openweathermap.org/data/2.5/weather?q={job.city}&units=imperial&appid={weather_api_key}"
                )
                weather_response = requests.get(weather_url)
                if weather_response.status_code == 200:
                    wdata = weather_response.json()
                    weather_data[job.id] = {
                        "temp": wdata["main"]["temp"],
                        "condition": wdata["weather"][0]["main"],
                        "icon": wdata["weather"][0]["icon"],
                    }
            except Exception:
                weather_data[job.id] = None
                

    return render(request, "applications/job_list.html", {
        "jobs": jobs,
        "weather_data": weather_data,
        })


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