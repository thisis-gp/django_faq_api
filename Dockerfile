# Dockerfile

# Use a Python base image
FROM python:3.9-slim-buster

# Set environment variables (optional, but good practice)
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE faq_project.settings  # Your Django settings file

# Create a working directory inside the container
WORKDIR /app

# Copy requirements file first for caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . /app/

# Collect static files (if you have any)
RUN python manage.py collectstatic --noinput

# Expose the port your Django app runs on (adjust if needed)
EXPOSE 8000

# Start the Django development server (adjust if you use a different server)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] # or python manage.py runserver 0.0.0.0:8000