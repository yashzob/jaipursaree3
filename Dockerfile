FROM python:3

# set work directory
WORKDIR /usr/src/app


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY /jaipur /usr/src/app

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]