"""OpenAI integration with dotenv loading and safe fallbacks."""

from __future__ import annotations

import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

try:
    from openai import OpenAI
except Exception:  # Keep compatibility when openai isn't installed yet.
    OpenAI = None  # type: ignore[assignment]


class OpenAITextService:
    """Small wrapper around OpenAI text generation with graceful degradation."""

    def __init__(self, model: str = "gpt-4o-mini") -> None:
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        self.client = OpenAI(api_key=self.api_key) if self.api_key and OpenAI else None

    def generate(self, prompt: str, fallback: str) -> str:
        """Generate text via OpenAI; return fallback on missing key/errors."""
        if not self.client:
            return fallback

        try:
            response = self.client.responses.create(
                model=self.model,
                input=prompt,
                temperature=0.4,
            )
            text = response.output_text.strip()
            return text or fallback
        except Exception:
            return fallback

    def key_configured(self) -> bool:
        """Expose key status for dashboard diagnostics."""
        return bool(self.api_key)
