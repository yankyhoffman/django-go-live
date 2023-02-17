FROM python:3.10-slim

RUN apt-get update && apt-get install -y libpq-dev build-essential && apt-get clean

WORKDIR /usr/src/app

RUN pip install gunicorn==20.1.0

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --system --no-create-home webadmin
USER webadmin

COPY src .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
