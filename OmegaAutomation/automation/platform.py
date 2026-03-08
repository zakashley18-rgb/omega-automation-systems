from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List
import random

import pandas as pd

DATA_PATH = Path("data/content_status.csv")


@dataclass
class TrendItem:
    source: str
    topic: str
    engagement: float


class TrendEngine:
    """Detect and rank trending topics from social and search sources."""

    sources = ["Reddit", "TikTok", "Instagram", "Google Trends"]

    def detect_trends(self, seed: str = "AI Automation") -> List[TrendItem]:
        items: List[TrendItem] = []
        for source in self.sources:
            for i in range(1, 4):
                engagement = round(random.uniform(0.4, 1.0), 3)
                items.append(TrendItem(source=source, topic=f"{seed} trend {i} ({source})", engagement=engagement))
        return sorted(items, key=lambda x: x.engagement, reverse=True)


class VideoFactory:
    """Generate long-form YouTube assets."""

    def generate_script(self, title: str) -> str:
        return (
            f"Intro: Welcome to this deep dive on {title}.\\n"
            "Body: Explain the opportunity, core steps, and practical examples.\\n"
            "CTA: Ask viewers to subscribe for more automation workflows."
        )

    def generate_title(self, idea: str) -> str:
        return f"{idea}: The Automation Blueprint for 2026"

    def generate_thumbnail_prompt(self, topic: str) -> str:
        return f"High contrast YouTube thumbnail for {topic}, futuristic UI, cinematic lighting"

    def generate_voiceover(self, script: str) -> str:
        return f"VOICEOVER_READY::{script[:120]}..."

    def build_video(self, script: str, output_path: str = "logs/generated_video.txt") -> str:
        # Placeholder marker for a MoviePy pipeline.
        Path(output_path).write_text(f"MoviePy pipeline placeholder\\n\\n{script}")
        return output_path


class ShortsFactory:
    def create_short(self, topic: str) -> str:
        return f"Vertical short created for '{topic}' with hook -> value -> CTA format."


class SocialMediaPipeline:
    platforms = ["Twitter", "Instagram", "TikTok"]

    def generate_posts(self, topic: str) -> Dict[str, str]:
        return {
            platform: f"{topic} | {platform} post: quick insight + actionable tip + CTA"
            for platform in self.platforms
        }


class BookFactory:
    def script_to_chapter(self, script: str) -> str:
        return f"Chapter 1\\n========\\n{script}\\n\\nKey Takeaways\\n- Repeatable system\\n- Measurable outcomes"

    def compile_ebook(self, chapters: List[str], output_path: str = "logs/generated_ebook.txt") -> str:
        Path(output_path).write_text("\\n\\n".join(chapters))
        return output_path


class AppIdeaGenerator:
    def generate(self, niche: str) -> Dict[str, List[str] | str]:
        return {
            "idea": f"{niche} Automation Copilot",
            "features": [
                "Trend detection dashboard",
                "AI content generation",
                "Automated publishing scheduler",
            ],
            "tasks": [
                "Validate market demand",
                "Build MVP workflow",
                "Launch with 10 pilot users",
            ],
        }


class AffiliateProductEngine:
    def find_products(self, niche: str) -> List[Dict[str, str]]:
        return [
            {"name": f"{niche} Toolkit Pro", "angle": "Best value starter stack"},
            {"name": f"{niche} Enterprise Suite", "angle": "Scale faster with automation"},
        ]

    def generate_review_script(self, product_name: str) -> str:
        return (
            f"Today we're reviewing {product_name}.\\n"
            "Pros: fast setup, measurable ROI.\\n"
            "Cons: learning curve for advanced workflows.\\n"
            "Verdict: strong option for creators and operators."
        )


class ContentStatusStore:
    columns = ["id", "type", "title", "status", "notes", "timestamp"]

    def __init__(self, path: Path = DATA_PATH) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            pd.DataFrame(columns=self.columns).to_csv(self.path, index=False)

    def add_entry(self, item_type: str, title: str, status: str, notes: str = "") -> None:
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
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        df.to_csv(self.path, index=False)

    def read_all(self) -> pd.DataFrame:
        return pd.read_csv(self.path)
