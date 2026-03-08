"""Core reusable content-generation factories for Omega Automation."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from OmegaAutomation.ai.openai_client import OpenAITextService


class VideoFactory:
    """Generate long-form YouTube assets."""

    def __init__(self, text_service: OpenAITextService | None = None) -> None:
        self.text_service = text_service or OpenAITextService()

    def generate_script(self, title: str) -> str:
        fallback = (
            f"Intro: Welcome to this deep dive on {title}.\n"
            "Body: Explain the opportunity, core steps, and practical examples.\n"
            "CTA: Ask viewers to subscribe for more automation workflows."
        )
        return self.text_service.generate(prompt=f"Create a YouTube script for: {title}", fallback=fallback)

    def generate_title(self, idea: str) -> str:
        fallback = f"{idea}: The Automation Blueprint for 2026"
        return self.text_service.generate(prompt=f"Create one catchy YouTube title for: {idea}", fallback=fallback)

    def generate_thumbnail_prompt(self, topic: str) -> str:
        return f"High contrast YouTube thumbnail for {topic}, futuristic UI, cinematic lighting"

    def generate_voiceover(self, script: str) -> str:
        return f"VOICEOVER_READY::{script[:120]}..."

    def build_video(self, script: str, output_path: str = "logs/generated_video.txt") -> str:
        """Store a placeholder artifact for a later MoviePy render pipeline."""
        Path(output_path).write_text(f"MoviePy pipeline placeholder\n\n{script}")
        return output_path


class ShortsFactory:
    """Build short vertical content from long-form ideas."""

    def create_short(self, topic: str) -> str:
        return f"Vertical short created for '{topic}' with hook -> value -> CTA format."


class BookFactory:
    """Convert scripts to chapters and compile local eBook files."""

    def script_to_chapter(self, script: str) -> str:
        return f"Chapter 1\n========\n{script}\n\nKey Takeaways\n- Repeatable system\n- Measurable outcomes"

    def compile_ebook(self, chapters: List[str], output_path: str = "logs/generated_ebook.txt") -> str:
        Path(output_path).write_text("\n\n".join(chapters))
        return output_path


class AppIdeaGenerator:
    """Generate app startup ideas for a chosen niche."""

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
    """Simple affiliate ideation module."""

    def find_products(self, niche: str) -> List[Dict[str, str]]:
        return [
            {"name": f"{niche} Toolkit Pro", "angle": "Best value starter stack"},
            {"name": f"{niche} Enterprise Suite", "angle": "Scale faster with automation"},
        ]

    def generate_review_script(self, product_name: str) -> str:
        return (
            f"Today we're reviewing {product_name}.\n"
            "Pros: fast setup, measurable ROI.\n"
            "Cons: learning curve for advanced workflows.\n"
            "Verdict: strong option for creators and operators."
        )
