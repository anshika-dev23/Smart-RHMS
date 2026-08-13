<div align="center">

<img src="assets/logo.svg" alt="SMART-RHMS Logo" width="600"/>

<br/><br/>

<img width="80" alt="logo" src="https://api.iconify.design/lucide/heart-pulse.svg?color=%23e7352c" />

# SMART-RHMS
### Smart Rural Health Monitoring & Management System

**IoT vitals monitoring · AI-driven risk prediction · Telemedicine — engineered for rural, low-connectivity healthcare.**

<p>
<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
<img src="https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white" />
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
</p>

<p>
<img src="https://img.shields.io/github/stars/YOUR-USERNAME/smart-rhms?style=flat-square&color=E7352C" />
<img src="https://img.shields.io/github/forks/YOUR-USERNAME/smart-rhms?style=flat-square" />
<img src="https://img.shields.io/github/last-commit/YOUR-USERNAME/smart-rhms?style=flat-square" />
<img src="https://img.shields.io/badge/license-MIT-yellow.svg?style=flat-square" />
<img src="https://img.shields.io/badge/status-active--development-orange?style=flat-square" />
</p>

**[Live Demo](#) · [Documentation](#-api-reference) · [Report Bug](../../issues) · [Request Feature](../../issues)**

<br/>

<!-- Animated typing banner — same service used on GitHub profile READMEs -->
<a href="#">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=E7352C&center=true&vCenter=true&width=600&lines=Smart+Rural+Health+Monitoring+System;IoT+%2B+AI+%2B+Telemedicine;Built+for+Low-Connectivity+Rural+India" alt="Typing SVG" />
</a>

<br/><br/>

<!-- Live/dynamic badges -->
<img src="https://komarev.com/ghpvc/?username=YOUR-USERNAME&label=Repo%20Views&color=e7352c&style=flat-square" />
<img src="https://img.shields.io/github/languages/top/YOUR-USERNAME/smart-rhms?style=flat-square" />
<img src="https://img.shields.io/github/repo-size/YOUR-USERNAME/smart-rhms?style=flat-square" />
<img src="https://img.shields.io/github/issues/YOUR-USERNAME/smart-rhms?style=flat-square" />
<img src="https://img.shields.io/github/contributors/YOUR-USERNAME/smart-rhms?style=flat-square" />

</div>

<br/>

## 📌 Why SMART-RHMS?

Over **65% of India's population lives in rural areas**, yet the doctor-to-patient ratio there is a
fraction of urban centers, and hospitals can be hours away. Chronic conditions — hypertension,
diabetes, COPD — go unmonitored between visits, and by the time a patient reaches a clinic, a
preventable complication has often already become an emergency.

**SMART-RHMS closes that gap.** A low-cost ESP32 + sensor kit continuously streams vitals from
the patient's home to the cloud, where a risk engine flags anything abnormal *before* it becomes
critical — routing the alert to the nearest ASHA worker and doctor, with a teleconsultation only a
tap away.

<br/>

## 🏗 System Architecture

```mermaid
flowchart TD
    A[👤 Rural Patient] --> B[📟 Sensors]
    A --> C[🧑‍⚕️ ASHA Health Worker]
    B --> D[📡 ESP32 Microcontroller]
    C --> D
    D --> E[🌐 Internet]
    E --> F[⚡ FastAPI Backend]
    F --> G[(🗄️ PostgreSQL)]
    F --> H[🤖 Machine Learning Risk Engine]
    H --> I[📊 Risk Prediction]
    I --> J[🩺 Doctor Dashboard]
    I --> K[💬 AI Assistant]

    style A fill:#E7352C,color:#fff
    style D fill:#E7352C,color:#fff
    style F fill:#009688,color:#fff
    style G fill:#4169E1,color:#fff
    style H fill:#7C3AED,color:#fff
    style J fill:#0EA5E9,color:#fff
    style K fill:#7C3AED,color:#fff
```

> GitHub renders this diagram automatically — no image needed.

| Layer | Responsibility | Status |
|:--|:--|:--:|
| 📟 ESP32 Firmware | Reads HR / SpO₂ / temperature / BP, pushes to the API | 🔜 Planned |
| ⚡ **FastAPI Backend** | Auth, patient registry, ingestion, alerting | ✅ **Live** |
| 🗄️ **PostgreSQL** | Patients, vitals, risk scores, alert history | ✅ **Live** |
| 🤖 ML Risk Engine | Flags abnormal vitals; upgradeable to a trained model | ✅ **v0 Live** |
| 🩺 Doctor Dashboard | Prioritized triage view, patient trends | ✅ Prototype |
| 💬 AI Assistant | Natural-language querying over patients & alerts | 🔜 Planned |

<br/>

## ✨ Key Features

<table>
<tr>
<td width="50%" valign="top">

**🔴 Real-Time Monitoring**
Live heart rate, SpO₂, temperature, and blood pressure streamed from wearable sensors, visualized with rolling trend charts.

**🧠 AI Risk Scoring**
Every reading is scored instantly. Rule-based today, structured to drop in a trained classifier with zero API changes.

**🚨 Smart Alerting**
Threshold breaches auto-generate alerts routed to the right ASHA worker and doctor, with a full acknowledgment audit trail.

</td>
<td width="50%" valign="top">

**🏘️ Built for the Field**
Village-based patient registry designed around how ASHA workers actually operate — offline-tolerant by design.

**🔐 Role-Based Security**
JWT auth for humans (ASHA / doctor / admin), separate device-key auth for hardware — no shared human credentials on IoT devices.

**📹 Integrated Telemedicine**
One tap from a flagged patient to a teleconsultation request — no app-switching required.

</td>
</tr>
</table>

<br/>

## 🎬 Demo

<div align="center">
<i>Add a screen recording or GIF of the dashboard here — repos with a visual demo get significantly more engagement.</i><br/>
<code>docs/demo.gif</code>
</div>

<br/>

## 🚀 Quick Start

```bash
git clone https://github.com/YOUR-USERNAME/smart-rhms.git
cd smart-rhms
cp .env.example .env
docker compose up --build
```

Backend live at `http://localhost:8000` · Interactive API docs at `http://localhost:8000/docs`

No hardware yet? Simulate an ESP32:

```bash
python scripts/simulate_device.py --device-id ESP32-001 --api-key <your-device-key>
```

<br/>

## 📡 API Reference

| Method | Endpoint | Description |
|:--|:--|:--|
| `POST` | `/auth/register` | Register an ASHA worker, doctor, or admin |
| `POST` | `/auth/login` | Get a JWT access token |
| `POST` | `/patients` | Register a patient and link a device ID |
| `GET` | `/patients` | List patients, optionally filtered by village |
| `GET` | `/patients/{id}/vitals` | Full vitals history for a patient |
| `GET` | `/patients/{id}/risk` | Latest AI risk score for a patient |
| `POST` | `/devices/vitals` | ESP32 posts a new sensor reading here |
| `GET` | `/alerts` | List alerts, filterable by acknowledgment status |
| `POST` | `/alerts/{id}/acknowledge` | Mark an alert as handled |

Full interactive Swagger docs auto-generate at `/docs`.

<br/>

## 🛠 Tech Stack

<p>
<img src="https://skillicons.dev/icons?i=py,fastapi,postgres,react,tailwind,docker,git" />
</p>

**Backend** FastAPI · SQLAlchemy · Pydantic · JWT (python-jose) · bcrypt
**ML** Rule-based risk engine (scikit-learn-ready)
**Frontend** React · Recharts · Tailwind CSS
**Hardware** ESP32 · pulse-oximeter, HR, and temperature sensors
**Infra** Docker · Docker Compose · PostgreSQL

<br/>

## 📂 Project Structure

```
smart-rhms-backend/
├── app/
│   ├── main.py              FastAPI app & router registration
│   ├── models.py            SQLAlchemy models
│   ├── schemas.py           Pydantic request/response schemas
│   ├── auth.py              JWT + device-key auth
│   ├── ml/risk_model.py     Risk prediction (rule-based → ML-ready)
│   └── routers/             auth · patients · vitals · alerts
├── scripts/simulate_device.py   ESP32 stand-in for local development
├── docker-compose.yml
└── README.md
```

<br/>

## 🗺 Roadmap

- [x] Core backend — FastAPI + PostgreSQL
- [x] Rule-based risk scoring engine
- [x] Doctor dashboard prototype
- [ ] ESP32 firmware for live sensor ingestion
- [ ] Trained ML model replacing rule-based v0
- [ ] AI assistant for natural-language triage queries
- [ ] SMS fallback alerts for zero-connectivity villages
- [ ] Village-scoped data access for ASHA workers

<br/>

## 🤝 Contributing

Contributions are welcome. Fork the repo, create a feature branch, and open a PR — for larger
changes, please open an issue first to discuss the approach.

```bash
git checkout -b feature/your-feature
git commit -m "Add: your feature"
git push origin feature/your-feature
```

<br/>

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.

<br/>

<div align="center">

**If this project is useful to you, consider giving it a ⭐ — it helps others discover it.**

<sub>Built as a demonstration of an IoT + AI-assisted rural health monitoring pipeline. Not a certified medical device.</sub>

</div>