import streamlit as st
import base64
from components.auth import render_login
from components.market import render_market_widget
from components.weather import render_weather_widget
from components.crop_doctor import render_crop_doctor
from components.schemes import render_schemes
from components.khata import render_khata

# Must be the first Streamlit command
st.set_page_config(
    page_title="AgriTrustX",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_base64_of_bin_file(bin_file):
    """Reads a local image file and converts it to a base64 string for CSS injection."""
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

def apply_glassmorphism_ui():
    """Injects custom CSS to create a futuristic Glassmorphism UI using a local image."""
    
    img_base64 = get_base64_of_bin_file("background.png")
    
    if img_base64:
        bg_css = f'background-image: url("data:image/png;base64,{img_base64}");'
    else:
        bg_css = 'background-color: #0e1117;'
    
    st.markdown(f"""
    <style>
    /* Full-screen tech-agriculture background */
    .stApp {{
        {bg_css}
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Frosted Glass effect for the main container */
    .block-container {{
        background: rgba(15, 25, 35, 0.75) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 2rem !important;
        margin-top: 2rem !important;
        margin-bottom: 2rem !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.6);
    }}

    /* FORCE HIGH CONTRAST TEXT FOR MOBILE & DESKTOP */
    .block-container h1, .block-container h2, .block-container h3, 
    .block-container p, .block-container span, .block-container label, 
    [data-baseweb="radio"] label span {{
        color: #FFFFFF !important;
    }}
    
    /* Input field label text styling */
    .stTextInput label p {{
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }}

    /* Transparent Sidebar with Blur */
    [data-testid="stSidebar"] {{
        background-color: rgba(10, 15, 20, 0.8) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    /* Hide Streamlit's default top header line */
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0) !important;
    }}
    
    /* Style Tabs to look like elevated glass buttons */
    div[data-baseweb="tab-list"] {{
        gap: 10px;
        background-color: transparent;
    }}
    div[data-baseweb="tab"] {{
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px 12px 0px 0px;
        padding: 10px 20px;
        transition: all 0.3s ease-in-out;
    }}
    div[data-baseweb="tab"]:focus, div[data-baseweb="tab"]:hover, div[aria-selected="true"] {{
        outline: none;
        background-color: rgba(76, 175, 80, 0.4);
        border-bottom: 2px solid #4CAF50 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# Initialize Session State Variables
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ""
if 'language' not in st.session_state:
    st.session_state['language'] = "English"

def logout():
    """Safely clears the session and returns to the login screen."""
    st.session_state['logged_in'] = False
    st.session_state['user_name'] = ""
    st.rerun()

def main():
    # Instantly apply the futuristic UI
    apply_glassmorphism_ui()
    
    if not st.session_state['logged_in']:
        render_login()
    else:
        # --- SIDEBAR CONFIGURATION & LOCALIZATION ---
        with st.sidebar:
            st.markdown("<h2 style='color: #4CAF50;'>✨ AgriTrustX</h2>", unsafe_allow_html=True)
            st.markdown("---")
            
            # --- THE TRILINGUAL TOGGLE ---
            st.session_state['language'] = st.radio(
                "🌐 Language / ಭಾಷೆ / भाषा",
                ["English", "ಕನ್ನಡ (Kannada)", "हिंदी (Hindi)"],
                index=["English", "ಕನ್ನಡ (Kannada)", "हिंदी (Hindi)"].index(st.session_state['language'])
            )
            st.markdown("---")
            
            # Dynamic Translations based on Toggle
            lang = st.session_state['language']
            
            if lang == "ಕನ್ನಡ (Kannada)":
                profile_title = "ರೈತರ ಪ್ರೊಫೈಲ್ (Farmer Profile)"
                alert_text = "📱 SMS ಎಚ್ಚರಿಕೆಗಳು: ನಿಷ್ಕ್ರಿಯಗೊಳಿಸಲಾಗಿದೆ"
                logout_text = "ಸುರಕ್ಷಿತ ಲಾಗ್ಔಟ್ (Secure Logout)"
                welcome_msg = f"ನಿಮ್ಮ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್‌ಗೆ ಸುಸ್ವಾಗತ, {st.session_state['user_name']}"
                tab_names = [
                    "📊 ಮಾರುಕಟ್ಟೆ ಮಾಹಿತಿ (Market)", 
                    "🌤️ ಹವಾಮಾನ ರಕ್ಷಣೆ (Weather)", 
                    "🩺 ಬೆಳೆ ವೈದ್ಯ (Crop Doctor)", 
                    "📜 ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು (Schemes)", 
                    "📒 ಸ್ಮಾರ್ಟ್ ಖಾತಾ (Khata)"
                ]
            elif lang == "हिंदी (Hindi)":
                profile_title = "किसान प्रोफ़ाइल (Farmer Profile)"
                alert_text = "📱 SMS अलर्ट: अक्षम (Admin Mode)"
                logout_text = "सुरक्षित लॉगआउट (Secure Logout)"
                welcome_msg = f"आपके डैशबोर्ड में आपका स्वागत है, {st.session_state['user_name']}"
                tab_names = [
                    "📊 मंडी भाव (Market)", 
                    "🌤️ मौसम सुरक्षा (Weather)", 
                    "🩺 एआई फसल डॉक्टर (Crop Doctor)", 
                    "📜 सरकारी योजनाएं (Schemes)", 
                    "📒 स्मार्ट खाता (Khata)"
                ]
            else:
                profile_title = "**Farmer Profile**"
                alert_text = "📱 SMS Alerts: Disabled (Admin Mode)"
                logout_text = "Secure Logout"
                welcome_msg = f"Welcome to your Dashboard, {st.session_state['user_name']}"
                tab_names = [
                    "📊 Market Intelligence", 
                    "🌤️ Weather Shield", 
                    "🩺 AI Crop Doctor", 
                    "📜 Gov Schemes", 
                    "📒 Smart Khata"
                ]
            
            st.markdown(profile_title)
            st.info(f"👤 {st.session_state['user_name']}")
            st.warning(alert_text)
            
            st.markdown("---")
            if st.button(logout_text, type="primary", use_container_width=True):
                logout()

        # --- MAIN DASHBOARD AREA ---
        st.title(welcome_msg)
        st.markdown("<br>", unsafe_allow_html=True)
            
        tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_names)
        
        with tab1:
            render_market_widget()
        with tab2:
            render_weather_widget()
        with tab3:
            render_crop_doctor()
        with tab4:
            render_schemes()
        with tab5:
            render_khata()

if __name__ == "__main__":
    main()