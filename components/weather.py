import streamlit as st
import requests

def analyze_weather_for_crops(temp_c, humidity, weather_desc):
    """Acts as an AI advisor to recommend crops based on atmospheric conditions."""
    temp = float(temp_c)
    hum = float(humidity)
    
    advice = {
        "status": "",
        "recommendation": "",
        "crops": []
    }
    
    # Analyze Temperature and Humidity
    if "rain" in weather_desc.lower() or "shower" in weather_desc.lower():
        advice["status"] = "🌧️ Active Rainfall / High Moisture"
        advice["recommendation"] = "Avoid chemical spraying today. Good time for transplanting water-heavy crops."
        advice["crops"] = ["Paddy (Rice)", "Sugarcane", "Jute", "Tea"]
        
    elif temp > 35:
        advice["status"] = "🔥 High Heat Stress"
        advice["recommendation"] = "Ensure adequate irrigation. Protect young saplings with shade nets if possible."
        advice["crops"] = ["Cotton", "Millets (Bajra/Jowar)", "Watermelon", "Sorghum"]
        
    elif temp < 20:
        advice["status"] = "❄️ Cool & Favorable"
        advice["recommendation"] = "Excellent conditions for winter crops. Minimal heat stress on plants."
        advice["crops"] = ["Wheat", "Mustard", "Chickpea (Chana)", "Potato", "Cabbage"]
        
    elif 20 <= temp <= 35 and hum > 60:
        advice["status"] = "🌱 Warm & Humid (Ideal Growth)"
        advice["recommendation"] = "Prime growing conditions. Monitor closely for fungal diseases due to high humidity."
        advice["crops"] = ["Maize", "Tomato", "Banana", "Turmeric", "Groundnut"]
        
    else:
        advice["status"] = "🌤️ Moderate & Dry"
        advice["recommendation"] = "Stable weather. Maintain regular irrigation schedules."
        advice["crops"] = ["Onion", "Sunflower", "Pulses", "Citrus Fruits"]
        
    return advice

def render_weather_widget():
    st.header("🌤️ AI Weather & Crop Advisor")
    
    # --- LOCATION SEARCH BAR ---
    city = st.text_input("📍 Enter City/Place in India", value="Mysuru", placeholder="e.g., Mysuru, Bengaluru, Delhi")
    
    if city:
        with st.spinner(f"Scanning atmospheric conditions for {city}..."):
            try:
                # Professional, keyless weather endpoint
                url = f"https://wttr.in/{city.replace(' ', '+')}?format=j1"
                res = requests.get(url, timeout=5)
                
                if res.status_code == 200:
                    data = res.json()
                    current = data['current_condition'][0]
                    
                    st.success(f"📡 Real-time weather synchronized for **{city.title()}**.")
                    
                    # Sleek SaaS-style Metric Cards
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        with st.container(border=True):
                            st.metric(label="🌡️ Temperature", value=f"{current['temp_C']} °C")
                            st.caption(f"Feels like {current['FeelsLikeC']} °C")
                    with col2:
                        with st.container(border=True):
                            st.metric(label="💧 Humidity", value=f"{current['humidity']}%")
                            st.caption(f"Condition: {current['weatherDesc'][0]['value']}")
                    with col3:
                        with st.container(border=True):
                            st.metric(label="💨 Wind Speed", value=f"{current['windspeedKmph']} km/h")
                            st.caption(f"Direction: {current['winddir16Point']}")
                            
                    # --- NEW: AI CROP ADVISOR SECTION ---
                    st.divider()
                    st.subheader("🤖 Agricultural AI Analysis")
                    
                    advice = analyze_weather_for_crops(current['temp_C'], current['humidity'], current['weatherDesc'][0]['value'])
                    
                    with st.container(border=True):
                        st.markdown(f"**Atmospheric Status:** {advice['status']}")
                        st.markdown(f"**Farming Recommendation:** {advice['recommendation']}")
                        
                        st.markdown("**Best Crops to Grow/Plant in these conditions:**")
                        # Display suggested crops as nice little tags
                        crop_tags = " ".join([f"`{crop}`" for crop in advice['crops']])
                        st.markdown(crop_tags)
                        
                else:
                    st.error("Unable to locate atmospheric data. Please verify the city spelling.")
            except Exception:
                st.warning("⚠️ Weather radar timeout. Please try again.")