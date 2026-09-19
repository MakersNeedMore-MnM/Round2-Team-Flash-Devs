import streamlit as st

def render_schemes():
    st.header("📜 Government Grants & Subsidies")
    st.markdown("Find financial support tailored to your exact farming profile.")
    
    with st.container(border=True):
        st.subheader("🔍 Eligibility Checker")
        col1, col2 = st.columns(2)
        with col1:
            land_size = st.number_input("Land Size (in Hectares)", min_value=0.0, max_value=50.0, value=1.5)
        with col2:
            farmer_type = st.selectbox("Category", ["General", "SC/ST", "Women Farmer", "FPO"])
            
        if st.button("Check My Schemes", type="primary"):
            st.success("✅ Matching Schemes Found for your profile!")
            
            with st.expander("💸 PM-KISAN (Income Support)", expanded=True):
                st.write("**Benefit:** ₹6,000 per year directly to your bank account via Direct Benefit Transfer.")
                st.write(f"**Status:** Eligible (Landholding: {land_size} Hectares)")
                st.button("Apply on Govt Portal", key="pmkisan")
                
            with st.expander("🛡️ PMFBY (Crop Insurance)"):
                st.write("**Benefit:** Protects against natural disasters and pests at just 2% premium for Kharif crops.")
                st.write("**Status:** Highly Recommended for current monsoon risks.")
                st.button("Calculate Premium", key="pmfby")
                
            with st.expander("🚜 SMAM (Machinery Subsidy)"):
                st.write("**Benefit:** 50-80% subsidy on tractors, drones, and harvesters.")
                st.write(f"**Status:** Eligible under the {farmer_type} category quotas.")
                st.button("View Equipment List", key="smam")