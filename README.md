# Group Ticket Booking Registration Platform

## Project Structure

```text
repo/
  backend/
  frontend/
  docker-compose.yml
  README.md
```

## Backend (FastAPI)

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Health check:

```bash
curl http://localhost:8000/health
```

## Frontend (React + Vite)

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

App URL:

```text
http://localhost:5173
```

## Database (PostgreSQL + pgAdmin via Docker Compose)

```bash
docker compose up -d
```

- PostgreSQL: `localhost:5432`
- pgAdmin: `http://localhost:5050` (email: `admin@example.com`, password: `admin`)
