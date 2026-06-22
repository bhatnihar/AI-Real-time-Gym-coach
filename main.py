import streamlit as st
import os
from services.auth.login_wall import render_login_wall
from services.state.session_defaults import initial_session_defaults
from services.config.workout_config import EXERCISE_OPTIONS
from services.ui.style_loader import load_css, inject_local_font

def main():
    st.set_page_config(
         
        initial_sidebar_state="expanded", 
        layout="centered"
    )

    load_css(os.path.join(os.getcwd(), "static", "style.css"))
    inject_local_font(os.path.join(os.getcwd(), "static", "AdobeClean.otf"), "AdobeClean")

    if not render_login_wall():
        return
    
    initial_session_defaults()

    workout_started = st.session_state.get("workout_started", False)

    with st.sidebar:
        st.title("💪🏻 Personal AI Coach")

        if st.session_state.username:
            st.caption(f"👤Login as {st.session_state.username}")
        
        st.divider()

        st.subheader("Workout Plan")

        if not workout_started:
            st.selectbox("Exercise", options=EXERCISE_OPTIONS, key="plan_exercise")

            st.number_input("Sets", min_value=0, max_value=50, step=1, key="plan_sets")

            st.number_input("Reps per Set", min_value=0, max_value=100, step=1, key="plan_reps")

            st.markdown("")

            start_session_button = st.button("Start Workout", width="stretch", key="start_workout_button") 

            if start_session_button:
                st.session_state["workout_started"] = True
                st.rerun()
        else:
            exercise = st.session_state.get("plan_exercise")
            sets = st.session_state.get("plan_sets")
            reps = st.session_state.get("plan_reps")

            print(exercise, sets, reps)

            st.info(f"{exercise} -- {sets} Sets / {reps} Reps")

            end_session_button = st.button("End Workout", width="stretch", key="end_session_button")

            if end_session_button:
                st.session_state["workout_started"] = False
                st.rerun()

        if workout_started:
            st.divider()

            exercise = st.session_state.get("plan_exercise")
            total_reps = st.session_state.get("reps")
            current_set_reps = st.session_state.get("current_set_reps") 
            reps_per_set = st.session_state.get("plan_reps")
            sets_completed = st.session_state.get("sets_completed")
            target_sets = st.session_state.get("plan_sets")

            st.subheader("Progress")

            st.metric("Total Reps", f"{total_reps}")
            st.metric("Current Set Reps", f"{current_set_reps} / {reps_per_set}")
            st.metric("Sets Completed", f"{sets_completed} / {target_sets}")

            st.divider()

            if exercise == "Squats":
                st.subheader("Squat Metrics")
                st.metric("Knee Angle", f"{st.session_state.get('knee_angle')}°")
                st.metric("Back Angle", f"{st.session_state.get('back_angle')}°")
                st.metric("Depth Status", st.session_state.get("depth_status"))

            if exercise == "Push-ups":
                st.subheader("Push-up Metrics")
                st.metric("Elbow Angle", f"{st.session_state.get('elbow_angle')}°")
                st.metric("Body Alignment", st.session_state.get("body_alignment"))
                st.metric("Hip Position", st.session_state.get("hip_status"))

            if exercise == "Lunges":
                st.subheader("Lunge Metrics")
                st.metric("Front Knee Angle", f"{st.session_state.get('front_knee_angle')}°")
                st.metric("Torso Angle", f"{st.session_state.get('torso_angle')}°")
                st.metric("Balance Status", st.session_state.get("balance_status"))

            if exercise == "Bicep Curls":
                st.subheader("Bicep Curl Metrics")
                st.metric("Elbow Angle", f"{st.session_state.get('elbow_angle')}°")
                st.metric("Swing Status", st.session_state.get("swing_status"))
                st.metric("Extension Status", st.session_state.get("extension_status"))

            if exercise == "Shoulder Press":
                st.subheader("Shoulder Press Metrics")
                st.metric("Elbow Angle", f"{st.session_state.get('elbow_angle')}°")
                st.metric("Shoulder Status", st.session_state.get("shoulder_status"))
                st.metric("Back Arch Status", st.session_state.get("back_arch_status"))

        

            
if __name__ == "__main__":
    main()

