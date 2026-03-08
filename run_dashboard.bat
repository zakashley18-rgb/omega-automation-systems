@echo off
REM Launcher for Omega Automation dashboard on Windows.
cd /d %~dp0
python -m streamlit run dashboard\verification_dashboard.py
