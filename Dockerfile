# python runtime
FROM python:3.7-alpine

# working directory
WORKDIR /app

# copy current directory into container
ADD . /app

# install requirements
RUN pip3 install -r requirements.txt

# make port 8000 available
EXPOSE 8000

# gunicorn configuration
CMD ["gunicorn", "--config", "./stockstash/config/gunicorn_config.py", "stockstash:app"]