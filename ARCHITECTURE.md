# Project Architecture

This document provides an overview of the architecture of the Django + Inertia + Vue with Vite scaffold project.

## Overview

The project is a web application built using Django as the backend framework, Vue.js for the frontend, and Vite as the build tool. It leverages Inertia.js to create a single-page application (SPA) experience without the need for a separate API.

## Key Components

### Backend

- **Django**: Serves as the primary backend framework, handling HTTP requests, database interactions, and business logic.
- **Django Apps**: The project is structured into multiple Django apps, each responsible for a specific domain of the application. The `main/api.py` file defines the API endpoints using Django Ninja.
- **Django ORM**: Used for database interactions, providing an abstraction layer over the database.
- **Django Allauth**: Manages user authentication and registration.
- **Inertia-Django**: Bridges the gap between Django and Inertia.js, allowing for seamless SPA development.

### Frontend

- **Vue.js**: A progressive JavaScript framework used for building user interfaces.
- **Vite**: A modern build tool that provides fast development and optimized production builds.
- **Vue Components**: The UI is composed of reusable Vue components, organized by pages and layouts. The frontend source code is located in the `static/src/js` directory.

### Middleware

- **WhiteNoise**: Serves static files efficiently in production.
- **Custom Middleware**: Additional middleware can be added to handle cross-cutting concerns like logging and security.

## Development Workflow

1. **Backend Development**: Use Django's development server to test backend changes.
2. **Frontend Development**: Use Vite's development server for hot module replacement and fast feedback.
3. **Integration**: Inertia.js facilitates the integration between the frontend and backend, allowing for seamless page transitions.

## Deployment

- **Production Build**: Use Vite to build optimized frontend assets.
- **Static Files**: Use Django's `collectstatic` command to gather static files for production.
- **Server**: Deploy the Django application using a WSGI server like Gunicorn, with Nginx as a reverse proxy.

## Conclusion

This architecture leverages the strengths of Django, Vue.js, and Vite to create a modern web application with a smooth development experience and efficient production performance.
