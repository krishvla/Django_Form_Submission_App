from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MasterIncident(models.Model):
    location = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    incident_location = models.TextField()
    initial_severity = models.CharField(max_length=50)
    suspected_cause = models.TextField()
    actions_takem = models.TextField()
    sub_incident_types = models.CharField(max_length=100)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    