from __future__ import annotations

import streamlit as st

from OmegaAutomation.automation.platform import (
    AffiliateProductEngine,
    AppIdeaGenerator,
    BookFactory,
    ContentStatusStore,
    ShortsFactory,
    SocialMediaPipeline,
    TrendEngine,
    VideoFactory,
)

st.set_page_config(page_title="Omega Automation Dashboard", layout="wide")
st.title("Omega Automation - Verification Dashboard")

store = ContentStatusStore()
trend_engine = TrendEngine()
video_factory = VideoFactory()
shorts_factory = ShortsFactory()
social_pipeline = SocialMediaPipeline()
book_factory = BookFactory()
app_idea_generator = AppIdeaGenerator()
affiliate_engine = AffiliateProductEngine()

st.sidebar.header("System Modules")
st.sidebar.write(
    """
- TREND ENGINE
- VIDEO FACTORY
- SHORTS FACTORY
- SOCIAL MEDIA PIPELINE
- BOOK FACTORY
- APP IDEA GENERATOR
- AFFILIATE PRODUCT ENGINE
"""
)

tab_trends, tab_script, tab_video, tab_chapter, tab_app, tab_social = st.tabs(
    [
        "Detect Trends",
        "Generate Script",
        "Generate Video",
        "Generate Chapter",
        "Generate App Idea",
        "Generate Social Media Post",
    ]
)

with tab_trends:
    st.subheader("TREND ENGINE")
    seed = st.text_input("Seed topic", value="AI Automation")
    if st.button("Detect trends"):
        results = trend_engine.detect_trends(seed)
        st.dataframe([r.__dict__ for r in results], width="stretch")
        store.add_entry("trend", seed, "generated", "Ranked trends across Reddit/TikTok/Instagram/Google Trends")

with tab_script:
    st.subheader("VIDEO FACTORY")
    idea = st.text_input("Video idea", value="AI Automation Business")
    if st.button("Generate script and title"):
        title = video_factory.generate_title(idea)
        script = video_factory.generate_script(title)
        thumbnail = video_factory.generate_thumbnail_prompt(title)
        voiceover = video_factory.generate_voiceover(script)
        st.markdown(f"**Title:** {title}")
        st.code(script)
        st.markdown(f"**Thumbnail Prompt:** {thumbnail}")
        st.markdown(f"**Voiceover Status:** {voiceover}")
        store.add_entry("script", title, "generated", "Script/title/thumbnail/voiceover created")

with tab_video:
    st.subheader("VIDEO + SHORTS FACTORY")
    script_input = st.text_area("Script", value="Hook, value, CTA")
    if st.button("Generate video and short"):
        video_path = video_factory.build_video(script_input)
        short_result = shorts_factory.create_short("Automation highlights")
        st.success(f"Video build placeholder written to: {video_path}")
        st.info(short_result)
        store.add_entry("video", "Automation video", "built", f"Video path: {video_path}")

with tab_chapter:
    st.subheader("BOOK FACTORY")
    chapter_script = st.text_area("Script to convert", value="This chapter explains automation strategy.")
    if st.button("Generate chapter + ebook"):
        chapter = book_factory.script_to_chapter(chapter_script)
        ebook_path = book_factory.compile_ebook([chapter])
        st.code(chapter)
        st.success(f"Ebook compiled at: {ebook_path}")
        store.add_entry("book", "Automation ebook", "compiled", f"Path: {ebook_path}")

with tab_app:
    st.subheader("APP IDEA GENERATOR + AFFILIATE ENGINE")
    niche = st.text_input("Niche", value="Creator Economy")
    if st.button("Generate app idea"):
        app_idea = app_idea_generator.generate(niche)
        products = affiliate_engine.find_products(niche)
        review = affiliate_engine.generate_review_script(products[0]["name"])
        st.json(app_idea)
        st.write("Trending affiliate products:", products)
        st.code(review)
        store.add_entry("app_idea", app_idea["idea"], "generated", "Includes features and tasks")

with tab_social:
    st.subheader("SOCIAL MEDIA PIPELINE")
    topic = st.text_input("Post topic", value="Automate your content pipeline")
    if st.button("Generate social posts"):
        posts = social_pipeline.generate_posts(topic)
        for platform, text in posts.items():
            st.markdown(f"**{platform}:** {text}")
        store.add_entry("social_post", topic, "generated", "Posts for Twitter/Instagram/TikTok")

st.divider()
st.subheader("Content Status Log")
st.dataframe(store.read_all(), width="stretch")
