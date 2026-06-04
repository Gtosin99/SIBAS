from __future__ import annotations

import streamlit as st


def initialize_session_state() -> None:
    st.session_state.setdefault("authenticated", False)
    st.session_state.setdefault("user", None)


def login_user(user: dict) -> None:
    st.session_state.authenticated = True
    st.session_state.user = user


def logout_user() -> None:
    st.session_state.authenticated = False
    st.session_state.user = None


def current_user() -> dict | None:
    return st.session_state.get("user")


def require_login() -> dict:
    initialize_session_state()
    user = current_user()
    if not st.session_state.authenticated or user is None:
        st.warning("Please log in to continue.")
        st.page_link("app.py", label="Go to login")
        st.stop()
    return user


def require_role(*allowed_roles: str) -> dict:
    user = require_login()
    if user["role"] not in allowed_roles:
        st.error("You do not have permission to access this page.")
        st.stop()
    return user


def render_sidebar_user() -> None:
    user = current_user()
    if not user:
        return

    st.sidebar.write(f"Signed in as **{user['full_name']}**")
    st.sidebar.caption(user["role"])
    if st.sidebar.button("Logout", use_container_width=True):
        logout_user()
        st.rerun()

