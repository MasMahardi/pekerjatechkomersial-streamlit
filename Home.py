from pathlib import Path
import streamlit as st


# --- PATH SETTING ---
current_dir = Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
# --- PAGE SETUP ---

introduction = st.Page(
    "views/0_Introduction.py",
    title="Introduction",
    icon=":material/home:",
    default=True,
)

python_tools = st.Page(
    "views/2_Portofolio.py",
    title="Python Automation Tool",
    icon=":material/service_toolbox:",
)

data_analytic = st.Page(
    "views/1_data_analytic.py",
    title="Data Science/ Data Analytic",
    icon=":material/analytics:",
)

cv = st.Page(
    "views/3_Curriculum_Vitae.py",
    title="Curriculum Vitae",
    icon=":material/mail:",
)

blog = st.Page(
    "views/4_blog.py",
    title="Blog",
    icon=":material/article:",
)

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Home": [introduction, cv],
        "Portofolio": [python_tools, data_analytic, blog],
    }
)

# --- RUN NAVIGATION ---
pg.run()
