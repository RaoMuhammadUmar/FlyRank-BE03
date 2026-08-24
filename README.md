# FlyRank BE-03 — Authentication API

A FastAPI authentication API built with Supabase Auth.

This project implements user signup, login, logout, JWT verification, protected routes, and Swagger Bearer authentication.

## Tech Stack

- Python
- FastAPI
- Supabase Auth
- PostgreSQL
- Docker
- JWT
- Swagger UI

## Features

- User signup
- User login
- User logout
- JWT access-token verification
- Protected API routes
- Reusable FastAPI authentication dependency
- Public API route
- Swagger Bearer authentication
- Environment-based configuration

## Project Structure

```text
FlyRank-BE03/
│
├── app/
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── route.py
│   └── supabase_client.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
