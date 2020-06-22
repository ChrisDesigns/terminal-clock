  
FROM python:3.7-slim-stretch
COPY . /app-build
WORKDIR /app-build
RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:app", "-k gevent"]