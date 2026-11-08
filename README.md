# jero-act-9 — Laboratory Activity 9: System-to-System API Integration

Flask + SQLite student app (continues Lab 8). Retrieve a partner's records, save selected ones locally, and send a practice record to the partner.

## Run locally
    pip install -r requirements.txt
    python init_db.py
    python app.py

## Render
- Build: `pip install -r requirements.txt`  Start: `gunicorn app:app`
- Enter the partner's Render URL (`https://<app>.onrender.com/api/students`) in the page.

## Endpoints added
- `GET /partner-records?url=` — server-side fetch of partner records (also `/api/classmate/students`)
- `POST /import-student` — save a partner record, source `Classmate API`
- `POST /send-to-partner` — send a practice record (source `Partner API`)
- `POST /api/students` — stores `source` (default `External API`; the page's form sends `Local`)

Use fictional data only.
