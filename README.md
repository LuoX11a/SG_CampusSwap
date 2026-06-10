# SG CampusSwap

<div align="center">

**A campus-centric C2C marketplace for Singapore university students**

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![React Native](https://img.shields.io/badge/Mobile-React_Native-61DAFB?logo=react)](https://reactnative.dev/)
[![Expo](https://img.shields.io/badge/Framework-Expo-000020?logo=expo)](https://expo.dev/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-4169E1?logo=postgresql)](https://www.postgresql.org/)
[![Firebase](https://img.shields.io/badge/Chat-Firebase-DD2C00?logo=firebase)](https://firebase.google.com/)
[![AWS](https://img.shields.io/badge/Hosting-AWS_Free_Tier-FF9900?logo=amazon-aws)](https://aws.amazon.com/free/)

</div>

---

## About

SG CampusSwap is a mobile application that provides a trusted, convenient, and campus-centric platform for Singapore university students to trade second-hand goods — textbooks, electronics, furniture, and daily necessities.

### Why This Exists

General-purpose marketplaces like Carousell and Facebook Marketplace are not designed for student-specific needs. SG CampusSwap addresses this gap with:

- **Verified student community** — Registration requires a university email (domain whitelist + email verification)
- **Campus-based discovery** — Filter items by campus location, find suggested meetup points
- **Course-code textbook search** — Search for textbooks by course code (e.g., "CS1010", "MA1101R")
- **In-app chat** — Real-time messaging between buyers and sellers
- **Trust via ratings** — User profiles with transaction reviews

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React Native (Expo) — iOS + Android |
| **Backend** | FastAPI (Python 3.11+) + Uvicorn |
| **Database** | PostgreSQL 15 via Neon (free tier) |
| **ORM** | SQLAlchemy 2.0 + Alembic |
| **Auth** | JWT + university email domain whitelist + verification code |
| **Real-time Chat** | Firebase Firestore |
| **Image Storage** | Cloudinary |
| **Push Notifications** | Expo Push Notifications |
| **Deployment** | AWS EC2 (free tier, ap-southeast-1) + Nginx + Let's Encrypt |
| **CI/CD** | GitHub Actions |

---

## Project Structure

```
sg-campusswap/
├── backend/                    # FastAPI server
│   ├── app/
│   │   ├── main.py            # App entry point
│   │   ├── config.py          # Settings & env vars
│   │   ├── database.py        # SQLAlchemy async engine
│   │   ├── models/            # ORM models
│   │   ├── schemas/           # Pydantic request/response schemas
│   │   ├── api/v1/            # Route handlers
│   │   ├── services/          # Business logic
│   │   └── utils/             # Email whitelist, helpers
│   ├── migrations/            # Alembic migrations
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
│
├── mobile/                    # React Native (Expo)
│   ├── app/                   # Expo Router pages
│   ├── src/
│   │   ├── components/        # Reusable UI components
│   │   ├── screens/           # Screen implementations
│   │   ├── stores/            # Zustand state management
│   │   ├── hooks/             # Custom hooks
│   │   ├── services/          # API client
│   │   └── types/             # TypeScript types
│   ├── package.json
│   └── eas.json
│
├── docs/                      # Project documentation
└── .github/workflows/         # CI/CD pipeline
```

---

## Features

### MVP (12-Week Sprint)
- [ ] User registration with university email verification (domain whitelist)
- [ ] Item listing with image upload (Cloudinary)
- [ ] Search by keyword, course code, category
- [ ] Filter by campus, price range, condition
- [ ] Real-time in-app chat (Firebase)
- [ ] User profile with transaction reviews & ratings
- [ ] Campus-based meetup point suggestions

### Future Versions
- Wishlist / saved items
- Offer / price negotiation system
- Push notifications for new items matching saved searches
- Item listing bump / promote system
- Chat message read receipts & typing indicators
- Dark mode

---

## Getting Started

### Prerequisites

- **Python 3.11+** with `pip`
- **Node.js 18+** with `npm`
- **Expo CLI** (`npm install -g expo-cli`)
- **PostgreSQL** (or a [Neon](https://neon.tech) free-tier database)
- **Firebase** project with Firestore enabled
- **Cloudinary** account

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables (or create .env)
cp .env.example .env
# Edit .env with your DATABASE_URL, JWT_SECRET, FIREBASE_CREDENTIALS, CLOUDINARY_*, etc.

# Run migrations
alembic upgrade head

# Start dev server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API docs available at `http://localhost:8000/docs` (Swagger UI).

### Mobile App Setup

```bash
cd mobile

# Install dependencies
npm install

# Start Expo dev server
npx expo start
```

Scan the QR code with Expo Go (iOS/Android) to test on your device.

### Environment Variables (Backend)

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | Neon PostgreSQL connection string |
| `JWT_SECRET` | Secret key for JWT signing |
| `ALLOWED_EMAIL_DOMAINS` | Comma-separated university email domains |
| `FIREBASE_SERVICE_ACCOUNT_PATH` | Path to Firebase service account JSON |
| `CLOUDINARY_CLOUD_NAME` | Cloudinary cloud name |
| `CLOUDINARY_API_KEY` | Cloudinary API key |
| `CLOUDINARY_API_SECRET` | Cloudinary API secret |
| `SMTP_HOST` / `SMTP_PORT` / `SMTP_USER` / `SMTP_PASS` | Email service for verification codes |

---

## Team

| Name | Role |
|------|------|
| Huang Hongrui | Project Manager |
| Renxian Tang | Frontend Lead |
| Wang Bowei | Backend Lead |
| Jiahai Xiong | Frontend Developer |
| Wang Xu | Backend Developer |
| Junliang Li | UI/UX Designer & QA |

---

## Development Workflow

- **Methodology**: Agile / Scrum (2-week sprints)
- **Branching**: `main` → `develop` → `feature/*`, `fix/*`
- **Commits**: [Conventional Commits](https://www.conventionalcommits.org/) — `feat:`, `fix:`, `docs:`, `refactor:`, `test:`
- **PR Reviews**: ≥1 approving review required before merge

---

## License

This project is developed as part of the CP3102 coursework at James Cook University Singapore (2026 TR2).

---

<div align="center">
<i>Built with FastAPI + React Native · Deployed on AWS Free Tier · $0 monthly cost</i>
</div>
