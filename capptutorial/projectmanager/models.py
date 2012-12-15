from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=128)
    short_description = models.CharField(max_length=128)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
