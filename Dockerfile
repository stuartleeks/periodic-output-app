FROM python:3.12.1-slim-bullseye

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY periodic_output_app .

CMD ["python", "app.py"]
