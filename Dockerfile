FROM python:3.10-slim

RUN apt-get update && apt-get install -y libpq-dev build-essential && apt-get clean

WORKDIR /usr/src/app

RUN pip install --no-cache-dir gunicorn==20.1.0

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --system --no-create-home webadmin
RUN chown -R webadmin .
USER webadmin

COPY src .

RUN mkdir staticfiles
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
