# ♻️ CivicLoop AI
### Predictive Waste Intelligence & Verified Civic Action Network

**Team CODE5URGE** · Smart Civic Operations · React · FastAPI · SQLite · Leaflet

CivicLoop AI brings citizen waste reporting and operational workflows together in one platform. It provides interfaces for incident reporting, bin monitoring, complaint tracking, route planning, fleet visibility, waste analysis, and operational analytics.

> **Prototype note:** Some AI outputs, analytics, and device activity may use sample data or simulation. Predictive performance and environmental impact have not been independently validated.

---

## 🚦 The CivicLoop Workflow

| Stage | Goal | Example |
|---|---|---|
| **SEE** | Collect incident descriptions, photos, locations, and available bin/device signals. | A resident reports an overflowing bin. |
| **PREDICT** | Analyse available data and surface classifications or priorities where supported. | Flag a bin or complaint for attention. |
| **ACT** | Support operational review with alerts, collection routes, and fleet information. | An operator reviews a suggested collection route. |
| **VERIFY** | Track status and supporting information for human review. | A reviewer checks complaint status and evidence. |

This workflow represents the product direction; it does not imply every stage is automated or validated in the current prototype.

## ✨ Key Capabilities

### 🧑‍🤝‍🧑 Citizen experience
- Submit waste complaints with location, description, urgency, and an optional photo.
- Track a complaint using its tracking identifier.
- Use browser location when permission is granted.

### 🏙️ Operations dashboard
- View summaries for bins, complaints, alerts, routes, and fleet activity.
- Monitor bin status and fill levels.
- Review complaint queues, update statuses, and trigger available image-analysis actions.
- View collection routes and route stops on maps.
- Explore fleet and driver views, including browser geolocation where enabled.
- Access analytics charts and waste-segregation guidance.

### ⚙️ Backend and integrations
- FastAPI endpoints with JWT authentication and role-aware access.
- SQLAlchemy persistence with SQLite as the default local database.
- WebSocket endpoints for supported live updates.
- OR-Tools-based route optimisation where configured.
- Waste image-analysis endpoints with local model loading and simulation fallbacks.
- Optional IoT simulator and ESP32/Raspberry Pi examples.
- Optional Firebase synchronisation when valid local credentials are configured.

Availability depends on configuration, dependencies, model files, and backend status. A page or integration in the code does not guarantee an external service or physical device is connected.

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

## 📁 Project Structure

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

## 🚀 Run Locally — Windows PowerShell

### Prerequisites
- Node.js and npm
- Python 3.11+ (or a compatible version supported by the backend dependencies)
- Git

Optional integrations may require additional dependencies, model files, credentials, hardware, or services.

### 1. Start the backend

From the repository root:

```powershell
cd smart-waste-backend-v2
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Set your own local secrets for this terminal session. Never commit them:

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

The backend is expected at `http://localhost:8000`. Use the address printed by the server if it differs.

- API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Default local database: `smart-waste-backend-v2/waste_management.db`

> Back up any existing database before resetting or changing local data.

### 2. Start the operations dashboard

Open a second terminal from the repository root:

```powershell
cd waste-dashboard
npm install
npm run dev
```

Open the URL printed by Vite (often `http://localhost:5173`).

### 3. Start the citizen app (optional)

Open a third terminal from the repository root:

```powershell
cd citizen-app
npm install
npm run dev
```

Vite selects another available port if the default port is occupied.

### 4. Start the root frontend (optional)

```powershell
npm install
npm run dev
```

The root frontend, operations dashboard, and citizen app are separate applications and do not automatically share one navigation shell. Run each in its own terminal.

### 5. Run the IoT simulator (optional)

With the backend running:

```powershell
cd smart-waste-backend-v2
python simulate_iot.py
```

Use only the IoT key configured for your local backend/device simulator. Never place privileged secrets in browser-exposed variables.

## 🔐 Configuration & Security

Depending on the features you use, backend configuration may include:

- `SECRET_KEY` — token-signing key.
- `ADMIN_PASSWORD` — password used by the admin seed script.
- `DATABASE_URL` — database connection; SQLite is the local default.
- `IOT_API_KEY` — key protecting the IoT update endpoint.
- Firebase service-account credentials — optional, for Firebase synchronisation.

Use a local `.env` or terminal environment variables as supported by the code. Keep secrets, service-account JSON files, private keys, local database files, and uploads out of Git. Rotate any credential that has been published accidentally.

**A Gemini API key is not required by the current application as audited.** Map tiles use Leaflet-based providers; verify the configured tile URL and its usage policy before changing providers or adding a key. Any `VITE_*` value is bundled into frontend code and must not be treated as a server-side secret.

## 🧪 Demo Data & Known Limitations

- Seed and simulator scripts can provide demo bins, complaints, routes, and device updates.
- AI outputs may be simulated when models or dependencies are unavailable.
- Analytics may include sample or synthetic values.
- Live updates require the relevant backend endpoints and services.
- Hardware examples do not mean physical sensors are connected.
- Forecast accuracy, hotspot prioritisation, environmental impact, and evidence-based closure have not been independently validated.
- This prototype is not a substitute for municipal dispatch systems or a formal civic verification process.

Clearly label sample data and simulated results during presentations and demos.

## 🗺️ Roadmap

- [ ] Evaluate waste-overflow prediction using historical time-series data.
- [ ] Add explainable risk scores with visible contributing factors.
- [ ] Formalise evidence capture and human-review workflows.
- [ ] Test route planning with fleet capacity and operational constraints.
- [ ] Add integration tests for reporting and complaint resolution.
- [ ] Validate performance through a municipal or community pilot.
- [ ] Document deployment, security, and operational monitoring.

## 📄 Licensing & Acknowledgements

Before redistributing or publishing this repository, review the licensing terms and required notices for all included components and dependencies.

## 👥 Team

**CODE5URGE**

---

CivicLoop AI explores the workflow **SEE → PREDICT → ACT → VERIFY** to connect citizen reports with waste-operation processes. Further integration, testing, and real-world validation are needed before claiming predictive effectiveness or operational impact.
