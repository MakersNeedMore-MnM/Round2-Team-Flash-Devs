import streamlit as st
import time
import random

def render_crop_doctor():
    st.header("🩺 AI Crop Doctor")
    st.markdown("Upload a photo of a diseased leaf, and our AI will analyze it instantly.")
    
    uploaded_file = st.file_uploader("Take a picture or upload an image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Crop Image", width=300)
        
        if st.button("🔍 Scan with AI", type="primary"):
            with st.spinner("Analyzing cell structure and disease patterns..."):
                # Simulates the processing time of a real AI model
                time.sleep(2) 
                
                # Mock AI outcomes for the hackathon presentation
                diseases = ["Leaf Blight", "Powdery Mildew", "Rust", "Aphid Infestation"]
                detected = random.choice(diseases)
                
                st.error(f"⚠️ **Pathogen Detected:** {detected}")
                
                st.subheader("💊 Recommended Treatment Plan")
                col1, col2 = st.columns(2)
                
                with col1:
                    with st.container(border=True):
                        st.markdown("**🌱 Organic Remedy**")
                        st.write("Spray Neem Oil extract (10,000 ppm) mixed with water. Apply during early morning or late evening to prevent leaf burn.")
                with col2:
                    with st.container(border=True):
                        st.markdown("**🧪 Chemical Remedy**")
                        st.write("Apply Copper Oxychloride (50% WP) at 2.5g per litre of water. Maintain a 15-day waiting period before harvest.")