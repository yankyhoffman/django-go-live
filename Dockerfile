FROM python:3.10-slim

RUN apt-get update && apt-get install -y libpq-dev build-essential && apt-get clean

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
