from __future__ import annotations

import streamlit as st

from app.session import render_sidebar_user, require_role


st.set_page_config(page_title="Lecturer | SIBAS", page_icon="S", layout="wide")

user = require_role("Lecturer")
render_sidebar_user()

st.title("Lecturer Dashboard")
st.write(f"Welcome, **{user['full_name']}**.")

st.header("Attendance Sessions")
st.info("Class session creation and attendance CSV upload will be built here.")

st.header("Attendance Corrections")
st.info("Manual attendance overrides for owned sessions will be built here.")

