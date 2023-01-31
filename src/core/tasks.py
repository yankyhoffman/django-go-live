from celery import shared_task

from core.models import Job


@shared_task
def manual():
    Job.objects.create(message='manual task')


@shared_task
def auto():
    Job.objects.create(message='automatic task')
