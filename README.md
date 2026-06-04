# SIBAS

Student Information and Biometric Attendance System (SIBAS) is a browser-based DBMS group project built with Streamlit and PostgreSQL.

## Current Deliverable

This version contains the Streamlit app shell and authentication foundation:

- Multi-page Streamlit layout
- PostgreSQL user table initialization
- Secure password hashing and verification with PBKDF2
- Login/logout UI
- Streamlit session management
- Role-based page access for Administrator, Lecturer, and Student

## Team Setup

1. Clone the repository.
2. Create a branch for your work.
3. Commit changes with clear messages.
4. Open a pull request for review before merging.

## Local Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create a `.env` file:

```powershell
Copy-Item .env.example .env
```

Update `DATABASE_URL` inside `.env` to match your PostgreSQL database:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/sibas
```

Seed the first administrator account:

```powershell
python scripts/seed_admin.py
```

Run the app:

```powershell
streamlit run app.py
```

## Project Structure

```text
app.py                  Streamlit login and dashboard landing page
app/
  config.py             Environment configuration
  db.py                 PostgreSQL connection and schema setup
  security.py           Password hashing and verification
  session.py            Login session and RBAC helpers
  users.py              User queries and authentication logic
pages/
  1_Administrator.py    Administrator-only shell
  2_Lecturer.py         Lecturer-only shell
  3_Student.py          Student-only shell
scripts/
  seed_admin.py         Creates the first administrator user
```

## Security Notes

- Passwords are never stored as plain text.
- Database queries use parameterized placeholders instead of raw string concatenation.
- Role checks are enforced on each protected page.

## Project Notes

Add the complete project description, requirements, database schema, setup instructions, and team member roles here as the project develops.
