import random
import streamlit as st

# @st.cache_data ensures the prices don't constantly change when the user types in the search bar
@st.cache_data
def get_fallback_prices():
    markets = [
        "Azadpur Mandi, Delhi", "Vashi APMC, Mumbai", "Lasalgaon Mandi, Nashik", 
        "Byadgi Mandi, Karnataka", "Yeshwantpur, Bengaluru", "Unjha Mandi, Gujarat", 
        "Mandsaur Mandi, MP", "Guntur APMC, Andhra", "Erode Mandi, Tamil Nadu",
        "Kochi Spices Market, Kerala", "Ozar Mandi, Maharashtra", "Kurnool Mandi, AP"
    ]

    # Massive 100+ Crop Catalog categorized by base price ranges (₹ / Qtl)
    crop_categories = {
        "Grains & Cereals": (1500, 3500, [
            "Paddy (Rice)", "Wheat", "Maize (Corn)", "Bajra (Pearl Millet)", "Jowar (Sorghum)", 
            "Ragi (Finger Millet)", "Barley", "Oats", "Basmati Rice", "Sona Masuri Rice", "Brown Rice"
        ]),
        "Pulses & Dals": (4000, 9000, [
            "Bengal Gram (Chana)", "Black Gram (Urad)", "Green Gram (Moong)", "Red Gram (Tur/Arhar)", 
            "Lentil (Masoor)", "Horse Gram", "Cowpea (Lobia)", "Moth Bean", "Rajma (Kidney Beans)"
        ]),
        "Vegetables": (800, 4000, [
            "Onion", "Potato", "Tomato", "Cabbage", "Cauliflower", "Brinjal (Eggplant)", "Okra (Bhindi)", 
            "Bitter Gourd", "Bottle Gourd", "Carrot", "Radish", "Capsicum", "Green Chilli", "Spinach", 
            "Coriander Leaves", "Fenugreek Leaves", "Beetroot", "Cucumber", "Pumpkin", "French Beans", "Sweet Potato"
        ]),
        "Fruits": (3000, 12000, [
            "Apple", "Banana", "Mango", "Grapes", "Orange", "Papaya", "Pomegranate", "Guava", "Pineapple", 
            "Watermelon", "Muskmelon", "Sweet Lime (Mosambi)", "Lemon", "Litchi", "Strawberry", "Cherry", 
            "Sapota (Chikoo)", "Custard Apple", "Pear", "Plum"
        ]),
        "Spices & Condiments": (10000, 80000, [
            "Turmeric", "Cumin (Jeera)", "Coriander Seed", "Black Pepper", "Cardamom (Small)", "Cardamom (Large)", 
            "Clove", "Fenugreek Seed", "Fennel Seed", "Nutmeg", "Mace", "Tamarind", "Dry Red Chilli", 
            "Garlic", "Ginger", "Ajwain", "Mustard Seed", "Poppy Seed", "Saffron"
        ]),
        "Commercial & Plantation": (3000, 50000, [
            "Cotton", "Jute", "Sugarcane", "Tobacco", "Tea Leaves", "Coffee Beans", "Rubber", 
            "Arecanut (Betel Nut)", "Coconut", "Cashewnut", "Almond", "Walnut"
        ]),
        "Oilseeds": (4000, 8000, [
            "Groundnut", "Soyabean", "Sunflower Seed", "Sesame Seed", "Safflower", "Castor Seed", "Linseed"
        ])
    }

    records = []
    
    # Generate realistic data for all 100+ crops
    for category, (low_price, high_price, crops) in crop_categories.items():
        for crop in crops:
            records.append({
                "commodity": crop,
                "modal_price": str(random.randint(low_price, high_price)),
                "market": random.choice(markets)
            })
            
    # Shuffle the list so the dashboard looks different every time the server boots up
    random.shuffle(records)
    return records