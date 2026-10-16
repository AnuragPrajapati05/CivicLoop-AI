# ♻️ CivicLoop AI
### Predictive Waste Intelligence & Verified Civic Action Network

**Team CODE5URGE** · Civic Waste Operations · React · FastAPI · SQLite · Leaflet

CivicLoop AI is a civic waste-operations platform designed to connect citizen reporting with municipal operations workflows. It brings incident reporting, bin monitoring, complaint tracking, route planning, fleet visibility, waste analysis, and operational analytics into one project.

> **Prototype status:** This repository contains an adapted and rebranded existing implementation. Some AI outputs, analytics, and device activity can use simulation or sample data. Predictive performance and environmental impact have not been independently validated.

---

## 🚦 The CivicLoop Workflow

| Stage | Purpose | Example |
|---|---|---|
| **SEE** | Collect incident descriptions, photos, locations, and available bin/device signals. | A resident reports an overflowing bin. |
| **PREDICT** | Analyse available data and surface classifications or priorities where supported. | Flag a bin or complaint for attention. |
| **ACT** | Support operational review with alerts, collection routes, and fleet information. | An operator reviews a suggested collection route. |
| **VERIFY** | Track status and supporting information for human review. | A reviewer checks the complaint status and evidence. |

The workflow describes the intended product direction; it does not imply that every stage is automated or validated in the current prototype.

## ✨ What’s in the Project?

### Citizen experience
- Submit a waste complaint with location, description, urgency, and optional photo.
- Track a complaint using its tracking identifier.
- Use browser location where permission is granted.

### Operations dashboard
- Dashboard summaries for bins, complaints, alerts, routes, and fleet activity.
- Smart-bin status and fill-level views.
- Complaint queues, status updates, and image-analysis actions.
- Route planning and route-stop visualisation.
- Fleet and driver views, including browser geolocation where enabled.
- Analytics charts and waste-segregation guidance.

### Backend and integrations
- FastAPI endpoints with JWT authentication and role-aware access.
- SQLAlchemy persistence using SQLite by default.
- WebSocket endpoints for supported live updates.
- OR-Tools-based route optimisation where configured.
- Waste image-analysis endpoints with local model loading and simulation fallbacks.
- Optional IoT simulator and ESP32/Raspberry Pi examples.
- Optional Firebase synchronisation when valid local credentials are provided.

Feature availability depends on configuration, dependencies, model files, and whether the backend is running. The presence of a page or integration does not guarantee a live external service is configured.

## 🧱 Architecture

```text
Citizen App ─────────┐
                     │
Operations Dashboard ├── HTTP / WebSocket ──> FastAPI Backend
                     │                            │
Root Frontend ───────┘                            ├── SQLAlchemy / SQLite
                                                  ├── AI analysis / fallbacks
                                                  ├── Route optimisation
                                                  ├── IoT simulator / device API
                                                  └── Optional Firebase sync
```

## 🛠️ Technology Stack

| Area | Technologies |
|---|---|
| Operations dashboard | React, Vite, React Router, Axios, Recharts, Leaflet, React Leaflet |
| Citizen app | React, Vite, React Router, Axios, React Leaflet |
| Additional frontend | Root React/Vite app |
| Backend | Python, FastAPI, Uvicorn, SQLAlchemy, Pydantic |
| Database | SQLite by default |
| AI / image analysis | Ultralytics YOLO when model files and dependencies are available; simulation fallback otherwise |
| Route optimisation | Google OR-Tools |
| Live updates and devices | WebSockets, IoT simulator, ESP32/Raspberry Pi examples |
| Optional integration | Firebase Admin SDK / Firestore |

## 📁 Repository Structure

```text
CivicLoop-AI/
├── smart-waste-backend-v2/   # FastAPI backend, models, routes, seed scripts, IoT tools
├── waste-dashboard/          # Operations dashboard
├── citizen-app/              # Citizen reporting and tracking app
├── src/                      # Additional root frontend
├── public/                   # Static assets
├── hardware/                 # Hardware examples
├── iot_hardware/             # ESP32 and Raspberry Pi examples
└── react-native-reference/   # Mobile integration notes
```

## 🚀 Run Locally (Windows PowerShell)

### 1. Prerequisites

- Node.js and npm
- Python 3.11+ (or a compatible version supported by the backend dependencies)
- Git

Optional integrations may require additional dependencies, model files, credentials, hardware, or services.

### 2. Start the backend

Open a terminal at the repository root:

```powershell
cd smart-waste-backend-v2
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Set local secrets for this terminal session. Use your own strong values; do not commit them:

```powershell
$env:SECRET_KEY = "<your-long-random-secret>"
$env:ADMIN_PASSWORD = "<your-strong-local-admin-password>"
```

Initialise the database, seed the administrator, and start the API:

```powershell
python -c "from database import initialize_database; initialize_database()"
python seed_admin.py
python main.py
```

The backend is expected at `http://localhost:8000`. If the app starts on a different port, use the address printed by the server.

API documentation (when the backend is running): [http://localhost:8000/docs](http://localhost:8000/docs)

> **Database note:** The default local database is `waste_management.db` inside the backend directory. Back up any existing database before changing or resetting local data.

### 3. Start the operations dashboard

Open a second terminal from the repository root:

```powershell
cd waste-dashboard
npm install
npm run dev
```

Open the local URL printed by Vite (often `http://localhost:5173`).

### 4. Start the citizen app (optional)

Open a third terminal from the repository root:

```powershell
cd citizen-app
npm install
npm run dev
```

Vite uses another available port if the default port is already occupied.

### 5. Start the root frontend (optional)

```powershell
npm install
npm run dev
```

Run each frontend in its own terminal. The root frontend, operations dashboard, and citizen app are separate applications; they do not automatically share one navigation shell.

### 6. Run the IoT simulator (optional)

With the backend running, open another terminal:

```powershell
cd smart-waste-backend-v2
python simulate_iot.py
```

Use only the IoT key configured for your local backend/device simulator. Do not use a privileged secret in browser-exposed variables.

## 🔐 Configuration & Secrets

The backend supports environment-based configuration. Depending on the features used, configure values such as:

- `SECRET_KEY` — signing key for authentication tokens.
- `ADMIN_PASSWORD` — password used by the admin seed script.
- `DATABASE_URL` — database connection; SQLite is the local default.
- `IOT_API_KEY` — key protecting the IoT update endpoint.
- Optional Firebase service-account credentials for Firebase synchronisation.

Use a local `.env` or terminal environment variables as supported by the code. Keep `.env`, `.env.*` (except intentionally committed examples), service-account JSON files, private keys, database files, and other credentials out of Git. Rotate any credential that has been accidentally published.

**No Gemini API key is required by the current rebranded application as audited.** Map tiles currently use Leaflet-based providers; verify the configured tile URL and its usage policy before changing providers or adding a key. Any `VITE_*` value is exposed to frontend code and must not be treated as a server-side secret.

## 🧪 Demo Data & Limitations

- Seed and simulator scripts can provide demo bins, complaints, routes, and device updates.
- Some AI outputs can be simulated when models or dependencies are unavailable.
- Analytics may contain sample or synthetic values.
- Real-time updates require the relevant backend endpoints and services.
- Hardware examples do not mean physical sensors are connected.
- Forecast accuracy, hotspot prioritisation, environmental impact, and evidence-based closure have not been independently validated.
- The prototype is not a substitute for municipal dispatch systems or a formal civic verification process.

When presenting the project, label sample data and simulated results clearly.

## 🗺️ Roadmap

- [ ] Evaluate waste-overflow prediction using historical time-series data.
- [ ] Add explainable risk scores with visible contributing factors.
- [ ] Formalise evidence capture and human reviewer workflows.
- [ ] Test route planning with real fleet capacity and operational constraints.
- [ ] Add integration tests for citizen reporting and complaint resolution.
- [ ] Validate performance with a municipal or community pilot.
- [ ] Document deployment, security, and operational monitoring.

## 🤝 Attribution & Licensing

CivicLoop AI builds on and rebrands the existing project at [sohit7ss/smart-waste-management](https://github.com/sohit7ss/smart-waste-management). This repository should not be represented as entirely original code.

No tracked `LICENSE` or `COPYING` file was found in the cloned repository when this README was prepared. Review the upstream repository’s current licensing terms and preserve any required notices before redistributing or publishing. Do not assume that the absence of a local license automatically grants permission to relicense inherited code.

## 👥 Team

**CODE5URGE**

## 📌 Project Summary

CivicLoop AI aims to connect citizen reports with waste-operation workflows through the cycle **SEE → PREDICT → ACT → VERIFY**. The current codebase provides a prototype foundation for exploring these workflows; further integration, testing, and real-world validation are required before claims of predictive effectiveness or operational impact can be made.
