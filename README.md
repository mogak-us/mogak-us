# Mogak.us

## Introduction

Mogak.us is a community management platform designed for individuals who want to gather and pursue their interests independently. The name "Mogak.us" is derived from the Korean words "모여서 각자" (Mogak) meaning "gather and do individually" and "우리" (Us) meaning "us". This platform is tailored for those who manage communities of people who wish to engage in activities together yet independently.

## Main Concept

The main concept of Mogak.us revolves around providing tools for effective community management. It is particularly focused on:

- **Member Management**: Efficiently manage community members and their participation.
- **Meeting Management**: Organize meetings, track attendance, and facilitate post-meeting retrospectives.


## Technologies

1. Inertia - powered by the official [Inertia.js Django Adapter](https://github.com/inertiajs/inertia-django)
2. Django latest
3. Vite latest - powered by [Django Vite](https://github.com/MrBin99/django-vite)
4. Vue 3 latest
5. [WhiteNoise](https://whitenoise.evans.io/en/stable/index.html) - to serve static files

## How to install & run

1. Download the repo. You can either:

   a. Clone the repo (without the git history):

   ```sh
   git clone https://github.com/oboynitro/django_inertia_vue_scaffold.git
   ```

2. Install required Python packages.

   ```sh
   # Create and activate a virtual environment
   # linux and mac
   virtualenv venv
   source .venv/bin/activate

   #windows users
   ./venv/Scripts/activate


   # Install required Python packages
   pip install -r requirements.txt
   ```

3. Install required Node.js packages.

   ```sh
   npm install
   ```

4. Run the Vite dev server:

   ```sh
   npm run dev
   ```

5. Run Django's default migrations:

   ```sh
   python manage.py migrate
   ```

6. Run the Django dev server (in a separate terminal):

   ```sh
   python manage.py runserver
   ```

## Aider Configuration

This project includes a `.aider.config.yml` file for configuring the Aider tool. Below is a basic example of what this configuration file might contain:

```yaml
# Aider configuration file

# Example configuration options
editor: vim
language: en_US
```

You can customize these settings according to your preferences.

## How to build for production

1. Set `DEBUG=False` in [settings.py](./inertia_django_vite_vue_minimal/settings.py).

   ```py
   # In settings.py
   ...
   DEBUG=False
   ...
   ```

2. Build the JS/assets for production:

   ```sh
   npm run build
   ```

3. Run `collectstatic`:

   ```sh
   rm -rf staticfiles/
   python manage.py collectstatic
   ```

4. Run the Django server:

   ```sh
   python manage.py runserver
   ```




-----



See https://github.com/oboynitro/django_inertia_vue_scaffold/tree/main
