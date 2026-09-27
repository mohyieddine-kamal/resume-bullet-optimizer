from optimizer import optimize_bullet
import streamlit as st

st.title("Resume Bullet Point Optimizer")
bullet_point = st.text_area("Enter your resume bullet point:")
if st.button("Optimize"):
    if not bullet_point:
        st.warning("Please enter a bullet point to optimize.")
    else:
        with st.spinner("En cours..."):
            optimized_bullet = optimize_bullet(bullet_point)
        st.success("Optimized Bullet Point:")
        st.write(optimized_bullet)
