FROM python:3.13

WORKDIR /app

COPY . /app

RUN pip install Flask

RUN pip install prometheus_client

EXPOSE 5000

CMD ["python", "app.py"]
