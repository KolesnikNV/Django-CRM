FROM --platform=linux/amd64 python:3.9

WORKDIR /app
COPY .env .
COPY . .
RUN chmod +x docker-entrypoint.sh
RUN pip install gunicorn
RUN pip install -r requirements.txt 
ENTRYPOINT ["./docker-entrypoint.sh"]


