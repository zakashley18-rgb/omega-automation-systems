"""Compatibility exports for existing dashboard imports."""

from OmegaAutomation.automation.content_store import ContentStatusStore
from OmegaAutomation.automation.factories import (
    AffiliateProductEngine,
    AppIdeaGenerator,
    BookFactory,
    ShortsFactory,
    VideoFactory,
)
from OmegaAutomation.integrations.social import SocialMediaGenerator as SocialMediaPipeline
from OmegaAutomation.trends.engine import TrendEngine, TrendItem

__all__ = [
    "AffiliateProductEngine",
    "AppIdeaGenerator",
    "BookFactory",
    "ContentStatusStore",
    "ShortsFactory",
    "SocialMediaPipeline",
    "TrendEngine",
    "TrendItem",
    "VideoFactory",
]
