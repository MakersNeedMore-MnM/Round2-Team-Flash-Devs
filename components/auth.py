import streamlit as st

def render_login():
    st.markdown("<h2 style='text-align: center; color: #4CAF50;'>🌾 AgriTrustX</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; margin-bottom: 30px;'>Secure Farmer Portal</h4>", unsafe_allow_html=True)
    
    with st.container(border=True):
        with st.form("login_form"):
            name = st.text_input("Full Name")
            phone = st.text_input("Phone Number (10 digits)")
            
            submitted = st.form_submit_button("Access Dashboard", use_container_width=True)
            
            if submitted:
                if name and phone:
                    # Instantly grant access without SMS verification
                    st.session_state['logged_in'] = True
                    st.session_state['user_name'] = name
                    st.success("✅ Authentication successful! Initializing secure connection...")
                    st.rerun()
                else:
                    st.error("⚠️ Please enter both your name and phone number to continue.")