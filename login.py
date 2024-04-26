import streamlit as st
import base64
import pandas as pd
from Videos import session

# Main login page
def main():
    st.set_page_config(
        page_title="Automatic Construction Site Monitoring: Advanced Video Analytics for Activity Detection",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    if "logged_in" not in st.session_state:
        form = st.form(key="my_form")

        form.subheader("Automatic Construction Site Monitoring: Advanced Video Analytics for Activity Detection")

        user = form.text_input("Username")
        password = form.text_input("Password", type="password", autocomplete="new-password")

        if form.form_submit_button("Login"):
            # Check if username and password are correct

            st.session_state["user"] = user
            st.session_state["password"] = password
            st.session_state["logged_in"] = True
            st.experimental_rerun()


    else:
        st.sidebar.subheader("Navigation")
        page = st.sidebar.radio("Go to", ["Start Session", "Logout"])

        if page == "Start Session":
            run_videos_page()  # Function to run the video analysis page

        elif page == "Logout":
            del st.session_state["logged_in"]
            st.experimental_rerun()


def run_videos_page():
    session()


if __name__ == "__main__":
    main()
