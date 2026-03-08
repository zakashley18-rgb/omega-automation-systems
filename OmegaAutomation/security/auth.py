"""Simple Streamlit login helper for dashboard access control."""

from __future__ import annotations

import os

import streamlit as st
from dotenv import load_dotenv

load_dotenv()


class DashboardAuth:
    """Session-state based login using environment-configurable credentials."""

    def __init__(self) -> None:
        # Defaults are intentionally simple for local Windows setup.
        self.valid_user = os.getenv("OMEGA_DASHBOARD_USER", "admin")
        self.valid_password = os.getenv("OMEGA_DASHBOARD_PASSWORD", "admin123")

    def require_login(self) -> bool:
        """Render login UI and return True only for authenticated sessions."""
        if "authenticated" not in st.session_state:
            st.session_state.authenticated = False

        if st.session_state.authenticated:
            return True

        st.subheader("Dashboard Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == self.valid_user and password == self.valid_password:
                st.session_state.authenticated = True
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

        return False
