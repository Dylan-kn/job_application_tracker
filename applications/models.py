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
    status = models.CharField(
        max_length=50,
        choices=status_choices,
        default="Applied"
    )
    date_applied = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.position} at {self.company} ({self.status})"
    

