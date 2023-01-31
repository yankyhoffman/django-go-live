from django.db import models


class Job(models.Model):
    message = models.TextField()
    ran_on = models.DateTimeField(auto_now_add=True)
