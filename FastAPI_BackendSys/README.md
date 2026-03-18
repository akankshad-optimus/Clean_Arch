# FastAPI Backend System

This folder contains the FastAPI backend entrypoint and local project setup for Clean Architecture.

## This Folder

- `main.py` - FastAPI application startup.
- `requirements.txt` - Python dependencies for FastAPI.
- `.gitignore` - ignored files for local development.

## Setup

1. Create and activate a Python virtual environment in this folder:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and fill critical values:

   ```powershell
   copy .env.example .env
   ```

4. Run the app:

   ```powershell
   uvicorn main:app --reload
   ```

## Secure Data Notes

- Never commit `.env` to Git; `.gitignore` already excludes it.
- Store secrets in environment variables in production (e.g. Docker secrets, cloud key vault).

## Notes

- If your app imports from `project/`, run from `FastAPI_BackendSys` or add the parent folder to `PYTHONPATH`.
- For clean architecture, keep business logic in `project/domain` and use case orchestration in `project/application`.
- Add API routes in `project/presentation/controllers` and wiring in `main.py`.
