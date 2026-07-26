# FlyRank Backend Engineering - BE-02

## Overview

This project is a CRUD REST API built using Python, FastAPI, and SQLite.

The API allows users to:

- Create tasks
- Read tasks
- Update tasks
- Delete tasks

Data is stored in a SQLite database, so it persists after the server restarts.

## Technologies

- Python
- FastAPI
- SQLite
- Uvicorn
- Pydantic

## Project Structure

```
app/
    main.py
    routes.py
    models.py
    database.py
```

## Installation

```bash
git clone <repository-url>
cd FlyRank-Python-BE01

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## Database

The SQLite database is automatically created as:

```
tasks.db
```

## Example SQL Query

```sql
SELECT * FROM tasks;
```
