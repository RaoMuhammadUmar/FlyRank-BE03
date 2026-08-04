# FlyRank Backend Engineering – BE-04

## Overview

This project is a CRUD REST API built with **Python**, **FastAPI**, and **PostgreSQL**. The PostgreSQL database runs inside a Docker container, while the API communicates with it using the **Psycopg** driver.

The project demonstrates how to migrate a FastAPI application from SQLite to PostgreSQL while keeping the REST API unchanged.

---

## Features

* Create tasks
* Read tasks
* Update tasks
* Delete tasks
* PostgreSQL database integration
* Dockerized database
* Request validation using Pydantic
* Interactive API documentation with Swagger UI

---

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* Docker
* Psycopg
* Pydantic
* Uvicorn

---

## Project Structure

```text
app/
│── main.py
│── route.py
│── models.py
│── database.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/RaoMuhammadUmar/FlyRank-BE04.git
cd FlyRank-BE04
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Start PostgreSQL

Run PostgreSQL using Docker:

```bash
docker run --name taskdb \
-e POSTGRES_PASSWORD=dev \
-e POSTGRES_DB=tasks \
-p 5432:5432 \
-v taskdata:/var/lib/postgresql/data \
-d postgres:17
```

Verify the container is running:

```bash
docker ps
```

---

## Run the API

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| GET    | `/tasks`      | Retrieve all tasks      |
| POST   | `/tasks`      | Create a new task       |
| PUT    | `/tasks/{id}` | Update an existing task |
| DELETE | `/tasks/{id}` | Delete a task           |

---

## Database

Database Server: PostgreSQL

Connection:

* Host: localhost
* Port: 5432
* Database: tasks

The application automatically creates the `tasks` table if it does not already exist.

---

## Learning Outcomes

This project demonstrates:

* Building REST APIs with FastAPI
* Connecting FastAPI to PostgreSQL
* Using Psycopg for database communication
* Running PostgreSQL in Docker
* Executing CRUD operations with SQL
* Organizing a backend project into separate modules
* Migrating from SQLite to PostgreSQL with minimal API changes
