"""Content status persistence helpers for the Omega dashboard."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

# Keep runtime-compatible storage in the existing project-level data folder.
DATA_PATH = Path("data/content_status.csv")


class ContentStatusStore:
    """Stores generated artifact statuses in a CSV file used by Streamlit."""

    columns = ["id", "type", "title", "status", "notes", "timestamp"]

    def __init__(self, path: Path = DATA_PATH) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            pd.DataFrame(columns=self.columns).to_csv(self.path, index=False)

    def add_entry(self, item_type: str, title: str, status: str, notes: str = "") -> None:
        """Append a single content record and keep IDs incremental."""
        df = pd.read_csv(self.path)
        entry_id = int(df["id"].max()) + 1 if not df.empty else 1
        row = {
            "id": entry_id,
            "type": item_type,
            "title": title,
            "status": status,
            "notes": notes,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        pd.concat([df, pd.DataFrame([row])], ignore_index=True).to_csv(self.path, index=False)

    def read_all(self) -> pd.DataFrame:
        """Read the full status log as a DataFrame for dashboard display."""
        return pd.read_csv(self.path)
