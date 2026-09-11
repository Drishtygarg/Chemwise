# ChemWise — AI Virtual Chemistry Lab

ChemWise is a responsive Flask web application for exploring chemical
reactions in a controlled, educational setting. It combines a
**deterministic chemistry engine** (the sole authority on whether a
reaction is valid, its equation, products, observations, and safety
level) with **Gemini AI** used strictly for explanation and tutoring —
never for deciding chemistry facts.

## Features

- **Chemical Library** — browse and search a catalog of chemicals by name, formula, or category
- **Run Experiment** — select two chemicals and get a verified, deterministic reaction result
- **Authentication** — persistent accounts with hashed passwords (Flask-Login)
- **Experiment History** — every supported experiment is saved to the student's history
- **AI Explanation** — Gemini explains an already-confirmed result in plain language (never invents chemistry)
- **PDF Reports** — download a formatted report of any experiment result
- **AI Viva** — an AI-tutored Q&A session grounded in a saved experiment's confirmed facts
- **Periodic Table** — a full 118-element reference, cross-linked to the chemical catalog
- **Faculty Dashboard** — role-restricted aggregate view of student activity

## Architecture

```
app/
  models/        SQLAlchemy models (User, Chemical, Reaction, Experiment, VivaSession, VivaQuestion)
  routes/        Flask Blueprints (chemicals, experiment, auth, ai, report, viva, periodic_table, faculty)
  services/      Business logic (reaction_engine, ai_service, pdf_service)
  repositories/  Database access layer, isolated from routes
  data/          Seed data (chemicals.json, reactions.json, periodic_table.json)
templates/       Jinja2 templates, organized by feature
static/          CSS
scripts/         seed_data.py, promote_faculty.py
```

**Chemistry rule:** The `Reaction` table and `reaction_engine.py` are
the only source of truth for chemistry. Gemini is only ever asked to
explain or discuss facts that have already been established there —
it cannot alter or invent a reaction result.

## Setup

```bash
pip install -r requirements.txt
python scripts/seed_data.py   # populate chemicals + reactions
python run.py
```

The app opens automatically at `http://127.0.0.1:5000`.

### Environment variables (`.env`)

```
FLASK_ENV=development
SECRET_KEY=change-me-to-a-random-value
DATABASE_URL=sqlite:///chemwise.db
GEMINI_API_KEY=your-gemini-api-key-here
GEMINI_MODEL=gemini-2.0-flash
```

Get a free Gemini API key at https://aistudio.google.com/apikey.
Without it, AI Explanation and AI Viva show a graceful "unavailable"
message — the rest of the app works normally.

### Making a user a faculty member

```bash
python scripts/promote_faculty.py user@example.com
```

## Tech Stack

Flask · SQLAlchemy · Flask-Login · SQLite · Gemini API (`google-genai`) · ReportLab

