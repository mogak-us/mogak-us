# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Node.js and npm
RUN apt-get update && apt-get install -y nodejs npm

# Set the working directory
WORKDIR /app

# Install dependencies
COPY pyproject.toml poetry.lock /app/

COPY README.md /app

# Copy the package folder so that Poetry can find it during install
COPY mogak_us /app/mogak_us

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

# Copy the project files
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["sh", "-c", "poetry run python manage.py migrate && poetry run python manage.py runserver 0.0.0.0:8000"]
