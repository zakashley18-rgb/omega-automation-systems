"""YouTube upload simulation integration for local/offline workflows."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path


class YouTubeUploader:
    """Simulates a YouTube upload and records it to local logs."""

    def __init__(self, log_path: str = "logs/youtube_uploads.log") -> None:
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

    def simulate_upload(self, title: str, video_path: str, description: str = "") -> dict:
        """Log a fake upload event while keeping the pipeline testable."""
        record = {
            "title": title,
            "video_path": video_path,
            "description": description,
            "status": "SIMULATED_UPLOAD_SUCCESS",
            "uploaded_at": datetime.utcnow().isoformat() + "Z",
        }
        self.log_path.write_text(self.log_path.read_text() + str(record) + "\n" if self.log_path.exists() else str(record) + "\n")
        return record
