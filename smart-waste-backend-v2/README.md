# CivicLoop AI Backend

FastAPI backend for **CivicLoop AI — Predictive Waste Intelligence & Verified Civic Action Network**.

## Setup

Open PowerShell in this folder:

```powershell
cd "C:\Users\anurag_prajapati\Desktop\smart-waste-management\smart-waste-backend-v2"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Configure local secrets before seeding the administrator:

```powershell
$env:SECRET_KEY = "<strong-random-secret>"
$env:ADMIN_PASSWORD = "<strong-admin-password>"
```

## Initialize the database

The project uses SQLite at `waste_management.db` by default. Create missing tables without deleting existing data:

```powershell
python -c "from database import initialize_database; initialize_database()"
```

## Seed the admin user

```powershell
python seed_admin.py
```

The admin email is:

```text
admin@smartwaste.city.in
```

The password is the value assigned to `ADMIN_PASSWORD`; no default password is stored in the source code.

## Start the backend

```powershell
python main.py
```

The API runs at:

- API: http://localhost:8000
- Swagger documentation: http://localhost:8000/docs
- Health check: http://localhost:8000/health

## Optional environment variables

Create a local `.env` file if needed. Do not commit it.

```dotenv
DATABASE_URL=sqlite:///./waste_management.db
SECRET_KEY=<strong-random-secret>
ADMIN_PASSWORD=<strong-admin-password>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
CORS_ORIGINS=http://localhost:5173,http://localhost:5174,http://localhost:5175
UPLOAD_DIR=./uploads
IOT_API_KEY=<your-iot-api-key>
```

Firebase integration is optional. Add `serviceAccountKey.json` locally only when Firebase synchronisation is required; never commit that file.

## Project contents

- `main.py` — FastAPI application
- `database.py` — SQLAlchemy engine, models base, and database initialization
- `models.py` — SQLAlchemy models
- `routes/` — API route modules
- `ai/` — waste and bin analysis logic
- `seed_admin.py` — administrator seed script
- `seed_db.py` and `seed_demo.py` — optional sample-data scripts
- `simulate_iot.py` — optional IoT simulator

The main project README is located one folder above this directory at `../README.md`.
