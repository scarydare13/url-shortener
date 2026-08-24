# URL Shortener

This project uses FastAPI, SQLAlchemy, PostgreSQL, and Alembic for database schema management.

## Prerequisites

- Python 3.11+
- PostgreSQL installed and running
- A PostgreSQL database created for the project
- Virtual environment (recommended)

## 1) Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## 2) Configure the database connection

Create a `.env` file in the project root if it does not already exist.

Example:

```env
DATABASE_URL=postgresql+psycopg://postgres:your_password@localhost:5432/url_shortener
```

Notes:
- Replace `your_password` with your actual PostgreSQL password.
- If your password contains special characters like `@`, URL-encode them.
- Example: `Test@123` becomes `Test%40123`.

## 3) Create the PostgreSQL database

Log in to PostgreSQL and create a database:

```sql
CREATE DATABASE url_shortener;
```

Then make sure the database is reachable using the URL in `.env`.

## 4) Run Alembic migrations

From the project root, run:

```powershell
python -m db.init_db
```

This executes Alembic and applies the migration to create the tables.

Alternative (if you want to use Alembic directly):

```powershell
alembic upgrade head
```

## 5) What tables are created

The initial migration creates:

- `urls`
- `url_clicks`

These tables include the required schema for the URL shortener application, such as UUID primary keys, active/expired flags, timestamps, foreign keys, and indexes.

## 6) Check the migration status

To see the current Alembic revision state:

```powershell
alembic current
```

To list revision history:

```powershell
alembic history
```

## 7) If you need to roll back the migration

```powershell
alembic downgrade -1
```

Or downgrade to a specific revision:

```powershell
alembic downgrade <revision_id>
```

## 8) Troubleshooting

### ModuleNotFoundError for `app.db`

Make sure you are running the project from the correct module layout. Use:

```powershell
python -m db.init_db
```

not:

```powershell
python -m app.db.init_db
```

### Connection errors

Check:
- PostgreSQL is running
- The database name is correct
- Username/password are correct
- The host and port are correct
- The `.env` file has no extra spaces or quotes

### `ValueError: invalid interpolation syntax` from Alembic

This usually happens when `%` appears in the password without being escaped. In PostgreSQL URLs, encode special characters properly, for example:

```env
DATABASE_URL=postgresql+psycopg://postgres:Test%40123@localhost:5432/url_shortener
```

## Project migration structure

The database migration files live in:

```text
alembic/
  env.py
  script.py.mako
  versions/
```

The migration revision file used to create the initial schema is:

```text
alembic/versions/<revision>_create_initial_url_schema.py
```

## Summary

To set up the database and create tables:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
# create .env with DATABASE_URL
python -m db.init_db
```

This will run Alembic and create the database tables for the project.
