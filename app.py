from __future__ import annotations

import streamlit as st

from app.db import DatabaseConfigError, initialize_database
from app.session import initialize_session_state, login_user, render_sidebar_user
from app.users import authenticate_user


st.set_page_config(page_title="SIBAS", page_icon="S", layout="wide")
initialize_session_state()


def render_login() -> None:
    st.title("SIBAS")
    st.subheader("Student Information and Biometric Attendance System")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login", use_container_width=True)

    if not submitted:
        return

    try:
        initialize_database()
        user = authenticate_user(username, password)
    except DatabaseConfigError as exc:
        st.error(str(exc))
        return
    except Exception as exc:
        st.error("Could not connect to the authentication database.")
        st.caption(str(exc))
        return

    if user is None:
        st.error("Invalid username or password.")
        return

    login_user(user)
    st.rerun()


def render_home() -> None:
    user = st.session_state.user
    render_sidebar_user()

    st.title("SIBAS Dashboard")
    st.write(f"Welcome, **{user['full_name']}**.")
    st.info("Choose an available page from the sidebar to continue.")

    if user["role"] == "Administrator":
        st.page_link("pages/1_Administrator.py", label="Administrator dashboard")
    elif user["role"] == "Lecturer":
        st.page_link("pages/2_Lecturer.py", label="Lecturer dashboard")
    elif user["role"] == "Student":
        st.page_link("pages/3_Student.py", label="Student dashboard")


if st.session_state.authenticated:
    render_home()
else:
    render_login()

