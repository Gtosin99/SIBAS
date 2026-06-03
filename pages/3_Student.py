from __future__ import annotations

import streamlit as st

from app.session import render_sidebar_user, require_role


st.set_page_config(page_title="Student | SIBAS", page_icon="S", layout="wide")

user = require_role("Student")
render_sidebar_user()

st.title("Student Dashboard")
st.write(f"Welcome, **{user['full_name']}**.")

st.header("Profile")
st.info("Student profile details will be shown here.")

st.header("Attendance")
st.info("Course attendance percentages and eligibility status will be shown here.")

