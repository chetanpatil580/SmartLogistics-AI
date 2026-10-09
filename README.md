# 🚀 AI-Powered Logistics Management System (Control Tower)
### Built with clean **MVC (Model - View - Controller)** Architecture

A enterprise-grade AI Logistics Software with predictive machine learning models, telemetry anomaly detection, route optimization, demand forecasting, and a dark-themed **Control Tower Dashboard** designed after industrial logistics nerve centers.

---

## 🏗️ 1. Architecture Overview (MVC Pattern)

```
ai_logistics_system/
├── run.py                       # 🚀 Application entry point (runs Flask server)
├── config.py                    # ⚙️ Configuration settings & paths
├── requirements.txt             # 📦 Project dependencies
│
├── database/                    # 🗄️ Database Layer
│   ├── init_db.py               # Database initialization & seeding script
│   └── logistics.db             # SQLite relational database
│
├── ml_engine/                   # 🧠 Machine Learning Engine
│   ├── train_models.py          # Training pipeline for all 6 ML models
│   ├── predictor.py             # Inference pipeline & scoring heuristics
│   ├── delay_model.pkl          # Scikit-Learn RandomForest delay classifier
│   ├── eta_model.pkl            # Scikit-Learn RandomForest ETA regressor
│   ├── demand_model.pkl         # Scikit-Learn RandomForest demand forecaster
│   ├── cost_model.pkl           # Scikit-Learn RandomForest cost estimator
│   ├── maintenance_model.pkl    # Scikit-Learn fleet maintenance model
│   └── anomaly_model.pkl        # Scikit-Learn IsolationForest anomaly detector
│
├── models/                      # 🧱 MODEL LAYER (M) - Business Logic & Data Access
│   ├── base.py                  # Database connection & query execution
│   ├── order_model.py           # Orders CRUD & AI delay scoring
│   ├── fleet_model.py           # Vehicles, telematics, predictive maintenance
│   ├── shipment_model.py        # Live GPS tracking & sensor anomalies
│   ├── warehouse_model.py       # Inventory, stockout risks & reorder triggers
│   ├── route_model.py           # Routes, waypoints & TSP optimizer
│   ├── driver_model.py          # Driver profiles, performance scoring & assignment
│   ├── cost_model.py            # Operating costs (fuel, driver, tolls, maintenance)
│   ├── alert_model.py           # Real-time incident logs & resolutions
│   ├── recommendation_model.py  # Automated AI logistics recommendations
│   └── chatbot_model.py         # Natural Language logistics query assistant
│
├── controllers/                 # 🎮 CONTROLLER LAYER (C) - HTTP & REST Endpoints
│   ├── dashboard_controller.py  # Control Tower dashboard metrics & charts
│   ├── order_controller.py      # Order creation, status updates & live ML inference
│   ├── fleet_controller.py      # Fleet roster & live vehicle telematics
│   ├── shipment_controller.py   # Live GPS telemetry simulator & tracking
│   ├── warehouse_controller.py  # Inventory operations & demand forecasts
│   ├── route_controller.py      # Waypoint sequence & route optimization
│   ├── driver_controller.py     # Driver scoring & auto-match endpoint
│   ├── cost_controller.py       # Expense breakdown & ML cost estimator
│   ├── analytics_controller.py  # KPI reports & operational charts
│   ├── alert_controller.py      # Incident management & one-click resolution
│   └── ai_controller.py         # Consolidated AI/ML API & Chatbot endpoint
│
└── views/                       # 🎨 VIEW LAYER (V) - Control Tower Interface
    ├── templates/
    │   ├── base.html            # Dark layout, top nav, sidebar, AI Chatbot drawer
    │   ├── dashboard.html       # Exact Control Tower Dashboard (matches UI image)
    │   ├── orders.html          # Order Management with live AI delay badge & modal
    │   ├── fleet.html           # Fleet Management & predictive maintenance meters
    │   ├── shipments.html       # Interactive Leaflet GPS map & telemetry alerts
    │   ├── warehouse.html       # Warehouses, inventory table & seasonal forecaster
    │   ├── routes.html          # Route Management with waypoint optimizer
    │   ├── drivers.html         # Driver score cards & assignment engine
    │   ├── costs.html           # Operating cost breakdown & AI cost estimator
    │   ├── analytics.html       # Analytics charts & performance KPIs
    │   └── alerts.html          # Incident notification center
    └── static/
        ├── css/
        │   └── style.css        # Control Tower custom dark stylesheet
        └── js/
            ├── dashboard.js     # Chart.js sparklines, donut & spline curve charts
            └── chatbot.js       # Interactive AI Logistics Chatbot drawer
```

---

## 📦 2. Core Functional Modules

| Module | Functionality |
|---|---|
| 📦 **Order Management** | Create, update, track orders with real-time AI delay probability & ETA estimation. |
| 🚚 **Fleet Management** | Vehicles, drivers, capacities, engine thermal monitoring & predictive maintenance risk scoring. |
| 📍 **Shipment Tracking** | Live geospatial Leaflet map, GPS coordinates, velocity, dwell time & telemetry anomaly alerts. |
| 🏭 **Warehouse Management** | Multi-hub capacity tracking, inventory replenishment thresholds & seasonal AI demand forecasting. |
| 🛣️ **Route Management** | Corridor distance minimization, priority waypoint sequencing, fuel & time savings calculator. |
| 👨‍✈️ **Driver Management** | Driver dossiers, experience, performance scores, delay penalties & automated optimal matching. |
| 💰 **Cost Management** | Fuel consumption, driver wages, toll fees, maintenance reserves & ML cost estimator. |
| 📊 **Analytics Dashboard** | On-time delivery rate, fleet utilization, monthly consignment volume & root cause Pareto charts. |
| 🔔 **Alerts & Incidents** | Real-time incident feed for delay warnings, excessive dwell holds, low stock & speed anomalies. |

---

## 🧠 3. Advanced AI / Machine Learning Capabilities

1. **Delivery Delay Prediction**:
   - Random Forest Classifier trained on distance, weight, vehicle capacity, traffic level, weather, previous delays, and warehouse processing hours.
   - Outputs: Delay probability (e.g. `Order #ORD-1024 → 78% probability of delay`) and risk classification (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`).
2. **ETA Prediction**:
   - Random Forest Regressor calculating dynamic delivery arrival times down to the minute.
3. **Smart Route Optimization**:
   - Solves multi-waypoint stop sequencing based on urgency priority (`Urgent`, `High`, `Medium`, `Low`) and distance heuristics. Calculates distance saved (km), hours saved, and fuel cost reduction ($).
4. **Demand Forecasting**:
   - Machine Learning regressor forecasting item demand across Normal, Peak, and Festival seasons.
5. **Inventory Prediction**:
   - Calculates days of supply vs. supplier lead times, flagging imminent stockout deficits before shelves are depleted.
6. **Anomaly Detection**:
   - Scikit-Learn `IsolationForest` continuously auditing live vehicle telematics (fuel spikes >38 L/100km, excessive dwell idle >35m, abnormal speeds, and route diversions).
7. **AI Logistics Chatbot**:
   - Interactive slide-in assistant answering questions:
     - *"Where is order ORD1024?"*
     - *"Which deliveries are delayed?"*
     - *"Show today's high-risk shipments."*
     - *"What is the fleet status?"*
8. **AI Recommendations**:
   - Decision support engine proposing operational mitigations:
     - *"5 shipments have a high delay probability. Consider rerouting 2 shipments."*
     - *"Vehicle VH-1004 has high maintenance risk (78.5%). Shift cargo to backup fleet."*

---

## ⚡ 4. Quick Start & Execution Guide

### Prerequisites
Python 3.10+ with standard data science libraries:
```bash
pip install -r requirements.txt
```

### Launch the Control Tower Application
Run the main application file:
```bash
python run.py
```

Open your browser at:
👉 **`http://127.0.0.1:5000`**

---

## 🗺️ 5. GPS Map & Routing Engine (OSRM & OpenRouteService)

The GPS mapping system supports real street-level turn-by-turn highway routing using **OSRM** and **OpenRouteService (ORS)**.

### Configuration Methods

#### Option A: Direct Web UI (Recommended)
1. Navigate to **[Live Shipment Tracking (`/shipments`)](http://127.0.0.1:5000/shipments)**.
2. Click the top-right button: **`🔑 OSRM / ORS API Keys`**.
3. Choose your preferred engine:
   - **OSRM (Open Source Routing Machine)**: Works out-of-the-box using the public routing cluster (`https://router.project-osrm.org`) or your private instance. You can optionally attach an access token/key.
   - **OpenRouteService (ORS)**: Enter your free API key from [openrouteservice.org](https://openrouteservice.org/dev/#/signup).
4. Click **Test Connection** and **Save Settings**. Settings are saved directly to the database and take effect immediately without restarting the server!

#### Option B: Environment Variables or `config.py`
You can also supply keys via environment variables or in `config.py`:
```bash
# In your terminal or .env:
export ORS_API_KEY="your-openrouteservice-api-key"
export OSRM_API_KEY="your-optional-osrm-token"
export OSRM_BASE_URL="https://router.project-osrm.org"
```

Or configure directly in [`config.py`](file:///c:/Users/CHETAN%20PATIL/Downloads/ai%20logistics%20softwer/config.py):
```python
ORS_API_KEY = "5b3ce3597851110001cf6248..."
OSRM_BASE_URL = "https://router.project-osrm.org"
```

### Live Road Tracing Features
- On the **Live Shipment Map**, click any vehicle or select **"Trace Route"** from the table to draw real highway driving paths from the truck's live GPS coordinates to its destination.
- On the **Route Management Page (`/routes`)**, click **"Preview GPS Route"** to trace the multi-waypoint interstate corridor.

---

## 🌐 6. REST API Endpoints

- `GET /` - Control Tower Dashboard
- `GET /api/map/settings` - Retrieve routing provider & masked API keys
- `POST /api/map/settings` - Save OSRM / ORS API keys and server URLs
- `GET /api/map/route` - Get turn-by-turn coordinates between any lat/lng points
- `GET /api/map/shipment-route/<id>` - Trace real highway route for a shipment
- `POST /api/ai/predict-delay` - Predict delivery delay probability
- `POST /api/ai/predict-eta` - Predict estimated hours of delivery
- `POST /api/ai/optimize-route` - Run AI waypoint route optimization
- `POST /api/ai/forecast-demand` - Run warehouse item demand forecasting
- `POST /api/ai/detect-anomaly` - Run IsolationForest telemetry audit
- `GET /api/ai/recommendations` - Fetch prioritized AI recommendations
- `POST /api/ai/chatbot` - Ask natural language logistics questions
