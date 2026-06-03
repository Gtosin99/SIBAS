from __future__ import annotations

import streamlit as st

from app.session import render_sidebar_user, require_role


st.set_page_config(page_title="Administrator | SIBAS", page_icon="S", layout="wide")

user = require_role("Administrator")
render_sidebar_user()

st.title("Administrator Dashboard")
st.write(f"Welcome, **{user['full_name']}**.")

st.header("User Management")
st.info("User creation, updates, deactivation, and deletion will be built here.")

st.header("Reports")
st.info("System-wide attendance reports will be built here.")

