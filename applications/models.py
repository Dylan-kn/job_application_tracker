from django.db import models

class JobApplication(models.Model):
    status_choices = (
        ("Applied", "Applied"),
        ("Interview", "Interview"),
        ("Offer", "Offer"),
        ("Rejected", "Rejected"),
    )

    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True)
    status = models.CharField(
        max_length=50,
        choices=status_choices,
        default="Applied"
    )
    notes = models.TextField(blank=True)
    job_description = models.TextField(blank=True)

    company_domain = models.CharField("Company Website (domain only, e.g. Netflix.com)", max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.position} at {self.company} ({self.status})"
    
    def get_logo_url(self):
        if self.company_domain:
            return f"https://logo.clearbit.com/{self.company_domain}"
        return None
    

