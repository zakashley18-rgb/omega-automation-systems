# Omega Automation

Production-ready local scaffold for the Omega Automation dashboard with modular architecture and safe AI fallbacks.

## Project structure

```text
OmegaAutomation/
  dashboard/
  automation/
  ai/
  trends/
  integrations/
  data/
  logs/
  security/
dashboard/
  verification_dashboard.py
data/
  content_status.csv
logs/
run_dashboard.bat
```

## Features

- Streamlit verification dashboard (kept compatible with existing run command).
- Reusable modules for trends, content factories, integrations, and security.
- CSV content status logging (`data/content_status.csv`).
- `.env` support for `OPENAI_API_KEY`.
- Simple username/password login for dashboard access.
- OpenAI-backed generation with automatic fallback when API key is missing.
- YouTube upload simulation logging to `logs/youtube_uploads.log`.
- Social media post generation module.

## Setup (Windows-friendly)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. (Optional) configure environment:
   - Copy `.env.example` to `.env`
   - Add `OPENAI_API_KEY` and/or custom dashboard credentials.

## Run instructions

### Option A: command line

```bash
python -m streamlit run dashboard\verification_dashboard.py
```

### Option B: launcher

Double-click `run_dashboard.bat` or run:

```bash
run_dashboard.bat
```

Default login (if not overridden in `.env`):
- Username: `admin`
- Password: `admin123`
