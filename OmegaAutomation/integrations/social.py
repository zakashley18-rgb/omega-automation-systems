"""Social content generation integration module."""

from __future__ import annotations

from typing import Dict

from OmegaAutomation.ai.openai_client import OpenAITextService


class SocialMediaGenerator:
    """Generate platform-specific social posts."""

    platforms = ["Twitter", "Instagram", "TikTok"]

    def __init__(self, text_service: OpenAITextService | None = None) -> None:
        self.text_service = text_service or OpenAITextService()

    def generate_posts(self, topic: str) -> Dict[str, str]:
        """Return one ready-to-post message per platform."""
        posts: Dict[str, str] = {}
        for platform in self.platforms:
            fallback = f"{topic} | {platform} post: quick insight + actionable tip + CTA"
            prompt = (
                f"Write a short {platform} post about: {topic}. "
                "Use a practical tone with one CTA. Keep it concise."
            )
            posts[platform] = self.text_service.generate(prompt=prompt, fallback=fallback)
        return posts
