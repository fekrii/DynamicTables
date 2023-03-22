# FROM python:3.10

# ENV PYTHONUNBUFFERED 1

# COPY ./requirements.txt /requirements.txt
# COPY . /app


# WORKDIR /app
# EXPOSE 8000

# RUN pip install --upgrade pip && \
#     pip install -r /requirements.txt && \
#     adduser --disabled-password --no-create-home app && \
#     mkdir -p /home/app/web && \
#     mkdir -p /home/app/web/staticfiles && \
#     mkdir -p /home/app/web/mediafiles && \
#     chown -R app:app /home/app/web && \
#     chmod -R 755 /home/app/web


# ENV PATH="/py/bin:$PATH"

# USER app

# # CMD ["run.sh"]

# pull official base image
FROM python:3.9.6-alpine

# set work directory
COPY ./requirements.txt /requirements.txt
COPY . /app


WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .