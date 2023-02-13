Sample app demonstrating pushing Django to production with Celery workers and schedulers (beat) with a PostgreSQL database for the backend and Redis for the Celery backend

Endpoints:
- `/` (the index page): Lists all tasks run
- `run/` Trigger an immediate task with the message set to `"manual task"`

Schedules:
- Currently defined in `src/conf/beat.py` (TODO: switch to `django_celery_beat`): Defines a task to run every minute with the message `"automatic task"`
