from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ["company", "position", "city", "status", "notes", "company_domain", "job_description"]

