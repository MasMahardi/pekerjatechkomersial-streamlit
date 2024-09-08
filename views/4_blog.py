import streamlit as st
import os


# --- CONTENT MANAGEMENT SYSTEM ---
content_files = {
    ("2024", "September"): "views/2024/2024_September.py",
    ("2024", "October"): "views/2024/2024_October.py",
    ("2025", "January"): "views/2025/2025_January.py",
    ("2025", "February"): "views/2025/2025_February.py"
    # Add entries for other year/month combinations
}

# Create a sidebar with year and month selection
st.sidebar.title("Journey of My Post")
year = st.sidebar.selectbox("Year", ["2024","2025"])
month = st.sidebar.selectbox("Month", ["September", "October","January","February"])

selected_file = content_files.get((year, month))

if selected_file:
    if os.path.exists(selected_file):
        with open(selected_file, 'r') as f:
            content = f.read()
        exec (content)
    else:
        st.error(f"File not found: {selected_file}")
else:
    st.warning("Please select a valid year and month combination.")
