FROM python:3.11

# Environment Variables
ENV PYTHONUNBUFFERED 1

# Work Directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000