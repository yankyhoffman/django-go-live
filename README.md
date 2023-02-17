Sample app demonstrating pushing Django to production with Celery workers and schedulers (beat) with a PostgreSQL database for the backend and Redis for the Celery backend

Endpoints:
- `/` (the index page): Lists all tasks run
- `run/` Trigger an immediate task with the message set to `"manual task"`

Schedules:
- Run `auto` task every minute with the message `"automatic task"`
