FROM python:3.14-slim

WORKDIR /app

COPY . .

RUN pip install Flask

EXPOSE 5000

CMD ["python", "app/app.py"]