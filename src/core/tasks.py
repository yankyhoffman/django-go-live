from celery import shared_task

from core.models import Job


@shared_task
def manual():
    Job.objects.create(message='manual task')


@shared_task
def auto():
    Job.objects.create(message='automatic task')


MESSAGES = {
    'a': 'task A',
    'b': 'task B',
    'c': 'task C',
}


@shared_task
def autoarg(*args):
    if not args:
        args = [*MESSAGES]

    for arg in args:
        message = MESSAGES.get(arg)
        if message is None:
            continue

        Job.objects.create(message=message)
