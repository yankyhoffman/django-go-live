from celery.schedules import crontab

SCHEDULE = {
    'auto': {
        'task': 'core.tasks.auto',
        'schedule': crontab(),
    }
}
