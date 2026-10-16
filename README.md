# CivicLoop AI — Predictive Waste Intelligence & Verified Civic Action Network

## Overview

CivicLoop AI is a civic waste operations platform for reporting waste incidents, analysing recurring hotspots, prioritising collection interventions, and tracking resolution evidence for human review. It combines a citizen reporting experience with an operations dashboard, a FastAPI backend, local AI analysis, route optimisation, and optional IoT/Firebase integrations.

## Problem Statement

Reactive complaint handling can leave reports fragmented across channels, make prioritisation difficult, and allow recurring hotspots to persist. Without reliable closure evidence and review, a complaint may be marked complete without clearly demonstrating that the civic issue was resolved. CivicLoop AI is intended to address these workflow gaps; the repository does not claim independently verified statistics about them.

## Proposed Solution

1. **SEE** — Collect incident descriptions, photos, and location information from citizens and connected systems.
2. **PREDICT** — Analyse available incident and bin data, with explainable ranking and classification outputs where supported by the current implementation.
3. **ACT** — Present collection priorities, alerts, routes, and fleet information for operational review.
4. **VERIFY** — Track complaint status and evidence, with human review remaining part of the operational workflow.

## Features

### Working in the repository

- Citizen waste-incident submission with image and location fields.
- Complaint tracking and operations-dashboard complaint views.
- SQLite persistence through SQLAlchemy models.
- Dustbin status, fill-level, battery, alert, and route views.
- FastAPI authentication with JWT access tokens and role-aware dashboard routes.
- WebSocket endpoints for dashboard updates.
- Waste fill-level and waste-type image analysis endpoints.
- YOLO-based model loading when model files and dependencies are available, with simulation fallbacks in the backend for unavailable models.
- Collection route optimisation using Google OR-Tools.
- Leaflet-based maps and fleet/driver views in the dashboard.
- IoT update endpoint protected by an API key, plus included ESP32/Raspberry Pi examples and a simulator.
- Optional Firebase Admin/Firestore synchronisation when `serviceAccountKey.json` is supplied.

### Partial or environment-dependent

- AI results use simulation when the relevant model is unavailable; they are not a validated forecasting system.
- Firebase synchronisation is optional and disabled when credentials are absent.
- Resolution evidence and human review are represented by the existing complaint workflow; they are not a municipal verification service.

## Technology Stack

- **Operations dashboard:** React 19, Vite, React Router, Axios, Recharts, Leaflet, and React Leaflet (`waste-dashboard/`).
- **Citizen app:** React 19, Vite, React Router, Axios, and React Leaflet (`citizen-app/`).
- **Additional frontend:** a root React/Vite app with Leaflet and the existing dashboard components.
- **Backend:** Python, FastAPI, Uvicorn, SQLAlchemy, and Pydantic.
- **Database:** SQLite by default at `smart-waste-backend-v2/waste_management.db`.
- **AI/ML:** Ultralytics YOLO model loading for bin/waste analysis, with a rules/simulation fallback.
- **Optimisation:** Google OR-Tools for collection-route optimisation.
- **Mapping and live updates:** Leaflet, WebSockets, GPS/fleet endpoints, ESP32, and Raspberry Pi examples.
- **Optional integration:** Firebase Admin SDK and Google Cloud Firestore.

The presence of a dependency or example does not guarantee that the corresponding external service or hardware is configured in every environment.

## Project Structure

```text
smart-waste-management/
├── smart-waste-backend-v2/   FastAPI app, SQLAlchemy models, AI, routes, seed scripts, and IoT tools
├── waste-dashboard/          Authenticated operations dashboard
├── citizen-app/              Citizen reporting and complaint tracking frontend
├── src/                      Additional root React/Vite dashboard frontend
├── hardware/                 Hardware examples
├── iot_hardware/             ESP32/Raspberry Pi sensor examples
├── react-native-reference/   Mobile integration notes
└── public/                   Shared frontend static assets
```

## Installation and Setup

### Backend

From the repository root:

```powershell
cd smart-waste-backend-v2
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:SECRET_KEY = "<replace-with-a-long-random-secret>"
$env:ADMIN_PASSWORD = "<choose-a-strong-local-admin-password>"
python -c "from database import initialize_database; initialize_database()"
python seed_admin.py
python main.py
```

The backend uses `sqlite:///./waste_management.db` by default. `initialize_database()` creates missing SQLAlchemy tables without dropping existing data.

### Operations dashboard

In another terminal:

```powershell
cd waste-dashboard
npm install
npm run dev
```

The dashboard normally opens at `http://localhost:5173`.

### Citizen app

To run the citizen-facing frontend separately:

```powershell
cd citizen-app
npm install
npm run dev
```

The Vite server will select an available local port if 5173 is already in use.

### IoT simulator

With the backend running:

```powershell
cd smart-waste-backend-v2
python simulate_iot.py
```

## Environment Configuration

The backend loads optional values from a `.env` file. Use placeholders for local or deployment secrets:

```dotenv
DATABASE_URL=sqlite:///./waste_management.db
SECRET_KEY=<replace-with-a-long-random-secret>
ADMIN_PASSWORD=<choose-a-strong-admin-password>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
CORS_ORIGINS=http://localhost:5173,http://localhost:5174,http://localhost:5175
UPLOAD_DIR=./uploads
MAX_REQUEST_SIZE_MB=5
RATE_LIMIT=100/minute
IOT_API_KEY=<replace-with-your-iot-api-key>
VITE_IOT_API_KEY=<same-iot-key-for-the-dashboard-only-when-needed>
```

Firebase is optional. If used, provide a local `serviceAccountKey.json` as required by the Firebase Admin SDK configuration; do not commit that file. No Gemini API key is required for this rebranded application, and no new AI integration was added.

## API Documentation

When the backend is running, FastAPI provides interactive documentation at:

`http://localhost:8000/docs`

The OpenAPI JSON document is available at `http://localhost:8000/openapi.json`.

## Sample Data and Limitations

The repository includes seed and simulator scripts for demo dustbins, complaints, routes, and IoT updates. Some analytics values and AI outputs may be synthetic or simulation-based. Model quality, hotspot prediction, closure verification, and municipal integration have not been independently validated. Set `ADMIN_PASSWORD` to a strong local value before running the admin seed script; no default password is committed.

## Future Scope

- Validate forecasting against longitudinal municipal incident data.
- Improve hotspot detection and explainable risk ranking.
- Add stronger evidence capture and formal reviewer workflows.
- Improve route optimisation with live constraints and collection capacity.
- Integrate with municipal work-order and identity systems.

## Licence and Attribution

No tracked `LICENSE` or `COPYING` file was present in the cloned repository at the time of this update. Review the upstream repository's licensing terms before publishing or redistributing.

CivicLoop AI reuses and rebrands the existing open-source repository available at [github.com/sohit7ss/smart-waste-management](https://github.com/sohit7ss/smart-waste-management). The inherited implementation and its original contributors should be acknowledged; this repository should not be presented as entirely original code.
