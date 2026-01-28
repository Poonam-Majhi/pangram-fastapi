# Pangram Checker API

A RESTful web service built with FastAPI to check if a given string is a pangram (contains all 26 letters of the English alphabet, case-insensitive).

## Features
- Accepts a string via GET (query parameter) or POST (JSON payload) request.
- Returns `true` if it's a pangram, `false` otherwise.
- Auto-generated docs at **`/docs`**(Swagger).
- No authentication required.

## Prerequisities
- Python 3.11+
- Git
- Visual Studio Code with Python extension

## Installation
1. Clone the repo: `git clone https://github.com/Poonam-Majhi/pangram-fastapi.git`
2. Navigate to the directory: `cd pangram-fastapi`
3. Create & activate a virtual environment:
   - `python -m venv.venv`
   ### Windows
   `.venv/Scripts/activate.bat`
4. Install dependencies: `pip install -r requirements.txt` 

## Usage
1. Run the app: `uvicorn app.main:app --reload`(In cmd)
2. API Endpoint: 
- **GET**: `/check_pangram?text=your_string` (e.g., `http://127.0.0.1:8000/check_pangram text=The%20quick%20brown%20fox`)
- **POST**: `/check_pangram` with JSON: `{"text": "Sphinx of black quartz, judge my vow"}`
3. Example Response: `{"is_pangram": true}`
4. View API docs at: `http://127.0.0.1:8000/docs`
5. Open browser:
  - Swagger UI: http://localhost:8000/docs#

## Code Structure
- `main.py`: Main FastAPI app with GET and POST endpoint logic (imports functions from `utils.py`).
- `utils.py`: Utility functions, including the pangram-checking logic (e.g., `is_pangram(text)` function).
- `test_main.py`: Unit tests.
- `requirements.txt`: Dependencies.
- `azure-deploy.md`: Documentation about code deployment on Azure Cloud.

## Testing
Run tests: `python -m pytest -q`

## Environment Used
`OS: Windows 10.`
`Python Version: 3.9+.`
`IDE: VS Code.`