FROM python:3.7

# for debugging purposes
ENV PYTHONBUFFERED 1

WORKDIR /app


# copy and install requirements.txt
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# copy the full app
COPY . /app

# run the app
CMD python manage.py runserver 0.0.0.0:8000
