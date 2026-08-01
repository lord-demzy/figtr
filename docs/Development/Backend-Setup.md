# FIGTR — Backend Setup Guide

## Purpose

This guide provides instructions for setting up the FIGTR backend locally for development.

## Required Python Version

- **Python 3.12 or higher** is required.
- The backend was tested on Python 3.14.4.
- `pyproject.toml` specifies `requires-python = ">=3.12"`.

## Virtual Environment Setup

Create a virtual environment inside `backend/.venv/`:

### Windows

```powershell
cd backend
py -3.12 -m venv .venv
```

Or with your default Python:

```powershell
cd backend
python -m venv .venv
```

### macOS / Linux

```bash
cd backend
python3 -m venv .venv
```

## Activating the Virtual Environment

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### Windows (Command Prompt)

```cmd
.venv\Scripts\activate.bat
```

### macOS / Linux

```bash
source .venv/bin/activate
```

## Dependency Installation

With the virtual environment activated, install the development dependencies:

### Windows

```powershell
pip install -r requirements\development.txt
```

### macOS / Linux

```bash
pip install -r requirements/development.txt
```

This installs:
- **Base dependencies:** Django, Django REST Framework, django-environ, django-cors-headers, psycopg2-binary
- **Development dependencies:** pytest, pytest-django, pytest-cov, ruff, black

## Environment Variables

Copy the example environment file and update values as needed:

```powershell
copy .env.example .env
```

or on macOS/Linux:

```bash
cp .env.example .env
```

The default development configuration uses **SQLite** for simplicity. To use PostgreSQL, set `USE_SQLITE=False` and configure the `DB_*` variables in `.env`.

## Running the Server

With the virtual environment activated:

```powershell
python manage.py runserver
```

The server will be available at: **http://127.0.0.1:8000/**

### Health Check Endpoint

Verify the backend is running:

```
GET /api/health/
```

Expected response:

```json
{
  "status": "ok"
}
```

## Running Tests

With the virtual environment activated:

```powershell
python -m pytest
```

Or from the `backend/` directory:

```powershell
cd backend
.venv\Scripts\python.exe -m pytest
```

## Code Quality Tools

### Linting with Ruff

```powershell
ruff check .
```

### Formatting with Black

```powershell
black .
```

## Django System Checks

Run Django's built-in system checks:

```powershell
python manage.py check
```

## Project Structure

See `docs/Architecture/Backend-Architecture.md` for the full backend architecture and structure.