import streamlit as st

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
    
    st.title("💪🏻 AI Real-time Gym Trainer")
    st.markdown("### Welcome! Please enter a username to continue.")

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Username", placeholder="Enter your username")
        submit_button = st.form_submit_button("Start Training", width="stretch")

    if submit_button:
        if not username:
            st.error("Username cannot be empty. Please enter a valid username.")
            return False

        st.session_state["username"] = username
        st.session_state["user_id"] = "1"

    return False