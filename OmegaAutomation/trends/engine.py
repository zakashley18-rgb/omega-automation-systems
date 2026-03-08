"""Trend discovery engine used by the dashboard and automation workflows."""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import List


@dataclass
class TrendItem:
    """A single trend observation from one source."""

    source: str
    topic: str
    engagement: float


class TrendEngine:
    """Detect and rank trending topics from social and search sources."""

    sources = ["Reddit", "TikTok", "Instagram", "Google Trends"]

    def detect_trends(self, seed: str = "AI Automation") -> List[TrendItem]:
        """Generate deterministic-like demo trend rows for a given seed topic."""
        items: List[TrendItem] = []
        for source in self.sources:
            for i in range(1, 4):
                engagement = round(random.uniform(0.4, 1.0), 3)
                items.append(TrendItem(source=source, topic=f"{seed} trend {i} ({source})", engagement=engagement))
        return sorted(items, key=lambda x: x.engagement, reverse=True)
