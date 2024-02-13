FROM python:3.11-slim-bookworm



ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /www
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

