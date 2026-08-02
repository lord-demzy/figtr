# FIGTR

**School Management, Simplified**

FIGTR is a commercial multi-tenant SaaS platform for managing schools, students, teachers, and academic operations.

## Technology Stack

### Backend

- **Framework:** Django 5.x
- **API:** Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (django-rest-framework-simplejwt)
- **Task Queue:** Celery + Redis (planned)

### Frontend

- **Framework:** Next.js 16 (React 19)
- **Language:** TypeScript 5
- **Styling:** Tailwind CSS v4
- **Components:** shadcn/ui + Base UI
- **Forms:** React Hook Form + Zod
- **Icons:** Lucide React

### Infrastructure

- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Hosting:** To be determined

## Project Structure

```
figtr/
├── backend/          # Django backend
│   ├── config/       # Django settings and URLs
│   ├── fig3/         # FIG3 Platform
│   │   ├── core/     # FIG3 Core — reusable platform services
│   │   └── edu/      # FIG3 Edu — education product
│   └── requirements/ # Python dependencies
├── frontend/         # Next.js frontend
│   ├── src/
│   │   ├── app/      # Next.js App Router
│   │   ├── components/ui/  # UI components
│   │   └── lib/      # Utilities and API client
│   └── public/       # Static assets
├── docs/             # Documentation
│   ├── Vision/
│   ├── Architecture/
│   ├── Database/
│   ├── API/
│   ├── UI/
│   └── Decisions/
├── docker/           # Docker configs
└── scripts/          # Utility scripts
```

## Getting Started

### Prerequisites

- Python 3.12+
- Node.js 18+
- PostgreSQL
- Docker (optional)

### Backend Setup

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux
pip install -r requirements/development.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env.local    # optional: configure env vars
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the frontend.

### Documentation

See `docs/` folder for:

- [Product Vision](docs/Vision/Product-Vision.md)
- [System Architecture](docs/Architecture/System-Architecture.md)
- [Frontend Architecture](docs/Architecture/Frontend-Architecture.md)
- [Database Conventions](docs/Database/Database-Conventions.md)
- [API Standards](docs/API/API-Standards.md)
- [Design System](docs/UI/Design-System.md)

## Development

### Backend

```bash
cd backend
python -m pytest
ruff check .
black .
```

### Frontend

```bash
cd frontend
npm run lint
npm run build
```

## Contributing

See [.clinerules](.clinerules) for development rules and guidelines.

## License

Proprietary — All rights reserved.
