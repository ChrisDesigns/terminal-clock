  
FROM debian:stretch-slim
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app-build
WORKDIR /app-build
RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:80", "server:app"]