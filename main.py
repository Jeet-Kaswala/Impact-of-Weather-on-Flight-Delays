# import streamlit as st
# import pandas as pd
# import numpy as np
# import pickle
# import joblib

# # -----------------------------------------
# # 1. Page Configuration & ATC Theme Styling
# # -----------------------------------------
# st.set_page_config(
#     page_title="Aviation Weather Risk System", 
#     page_icon="✈️", 
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS for dark-mode Aviation/Radar feel
# st.markdown("""
#     <style>
#     .stApp {
#         background-color: #0E1117;
#         color: #C6D4E1;
#     }
#     h1, h2, h3 {
#         color: #4DB6AC;
#         font-family: 'Courier New', Courier, monospace;
#     }
#     .risk-low {
#         background-color: #1B5E20;
#         padding: 20px;
#         border-radius: 10px;
#         text-align: center;
#         color: white;
#     }
#     .risk-medium {
#         background-color: #F57F17;
#         padding: 20px;
#         border-radius: 10px;
#         text-align: center;
#         color: white;
#     }
#     .risk-high {
#         background-color: #B71C1C;
#         padding: 20px;
#         border-radius: 10px;
#         text-align: center;
#         color: white;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # -----------------------------------------
# # 2. Load Models (Cached for Performance)
# # -----------------------------------------
# @st.cache_resource
# def load_assets():
#     with open('data_preprocessing.pkl', 'rb') as f:
#         preprocessor = joblib.load(f)
#     with open('aviation_model.pkl', 'rb') as f:
#         model = joblib.load(f)
#     return preprocessor, model

# preprocessor, model = load_assets()

# # -----------------------------------------
# # 3. Sidebar: Static Flight Details
# # -----------------------------------------
# st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3125/3125713.png", width=100)
# st.sidebar.title("Flight Dispatch Parameters")

# origin = st.sidebar.selectbox("Origin Airport", ['SJC', 'DFW', 'JFK', 'LAX', 'ORD', 'ATL', 'CLT'])
# dest = st.sidebar.selectbox("Destination Airport", ['DFW', 'SJC', 'LAX', 'JFK', 'ORD', 'ATL', 'IND', 'CLE'])
# carrier = st.sidebar.selectbox("Operating Carrier", ['AA', 'DL', 'UA', 'WN', 'AS', 'B6'])
# dep_hour = st.sidebar.slider("Scheduled Departure Hour", 0, 23, 8)
# distance = st.sidebar.number_input("Flight Distance (miles)", 100, 5000, 1438)

# st.sidebar.markdown("---")
# st.sidebar.subheader("Aircraft Specifications")
# manufacturer = st.sidebar.selectbox("Manufacturer", ['Airbus', 'Boeing', 'Embraer', 'Bombardier'])
# icao_type = st.sidebar.text_input("ICAO Type", 'A319')
# width = st.sidebar.selectbox("Cabin Width", ['Narrow-body', 'Wide-body'])
# ran = st.sidebar.selectbox("Aircraft Range", ['Short Range', 'Medium Range', 'Long Range'])

# # -----------------------------------------
# # 4. Main UI: Meteorological Conditions
# # -----------------------------------------
# st.title("🛰️ Weather Impact Analysis Terminal")
# st.markdown("Adjust meteorological thresholds to evaluate the probability of a delay ≥ 15 minutes or flight cancellation.")

# tab1, tab2, tab3 = st.tabs(["Thermodynamics & Wind", "Visibility & Cloud Cover", "Engineered Indicators"])

# with tab1:
#     col1, col2 = st.columns(2)
#     with col1:
#         st.subheader("Temperature Profiling")
#         temp = st.slider("Temperature (°C)", -30.0, 50.0, 7.78)
#         dew_point = st.slider("Dew Point (°C)", -30.0, 50.0, 3.89)
#         rel_humidity = st.slider("Relative Humidity (%)", 0.0, 100.0, 76.4)
#         humidity_level = st.selectbox("Humidity Category", ['Low', 'Moderate', 'High', 'Very High'], index=2)
    
#     with col2:
#         st.subheader("Wind Dynamics")
#         wind_spd = st.slider("Wind Speed (knots)", 0.0, 100.0, 0.0)
#         wind_gust = st.slider("Wind Gust (knots)", 0.0, 100.0, 0.0)
#         wind_dir = st.number_input("Wind Direction (degrees)", 0.0, 360.0, 0.0)
#         wind_direction_cat = st.selectbox("Wind Direction Label", ['North', 'South', 'East', 'West', 'Variable'])

# with tab2:
#     col3, col4 = st.columns(2)
#     with col3:
#         st.subheader("Visibility & Pressure")
#         visibility = st.slider("Visibility (miles)", 0.0, 10.0, 10.0)
#         visibility_cat = st.selectbox("Visibility Category", ['Low', 'Moderate', 'High'], index=1)
#         altimeter = st.slider("Altimeter (inHg)", 28.00, 31.00, 30.02)
#         active_weather = st.number_input("Active Weather Code (0=Clear, 1=Storm)", 0.0, 5.0, 0.0)
        
#     with col4:
#         st.subheader("Cloud Ceilings")
#         lowest_cloud = st.number_input("Lowest Cloud Layer (ft)", 0.0, 40000.0, 2000.0)
#         cloud_cover = st.slider("Cloud Cover (Oktas)", 0.0, 8.0, 1.0)
#         n_cloud_layer = st.slider("Number of Cloud Layers", 0.0, 5.0, 1.0)
#         total_cloud = st.slider("Total Cloud Metric", 0.0, 10.0, 1.0)

# with tab3:
#     st.markdown("*(These metrics are typically auto-calculated by the Data Engineering pipeline)*")
#     col5, col6 = st.columns(2)
#     with col5:
#         temp_dew_diff = st.number_input("Temp-Dew Point Depression", -10.0, 50.0, round(temp - dew_point, 2))
#         weather_sev = st.number_input("Weather Severity Index", 0.0, 100.0, 7.64)
#         cloud_encoded = st.number_input("Cloud Cover Encoded", 0, 10, int(cloud_cover))
#     with col6:
#         wind_intensity = st.number_input("Wind Intensity Index", 0.0, 50.0, 0.0)
#         low_cloud = st.number_input("Low Level Cloud", 0.0, 1.0, 1.0)
#         mid_cloud = st.number_input("Mid Level Cloud", 0.0, 1.0, 0.0)
#         high_cloud = st.number_input("High Level Cloud", 0.0, 1.0, 0.0)

# # -----------------------------------------
# # 5. Prediction Execution
# # -----------------------------------------
# st.markdown("---")
# if st.button("🚀 Execute Risk Evaluation", use_container_width=True):
    
#     # 1. Assemble exactly 32 columns required by the preprocessor
#     input_dict = {
#         'DEP_HOUR': dep_hour,
#         'OP_UNIQUE_CARRIER': carrier,
#         'ORIGIN': origin,
#         'DEST': dest,
#         'DISTANCE': distance,
#         'MANUFACTURER': manufacturer,
#         'ICAO TYPE': icao_type,
#         'RANGE': ran,
#         'WIDTH': width,
#         'WIND_DIR': wind_dir,
#         'WIND_SPD': wind_spd,
#         'WIND_GUST': wind_gust,
#         'VISIBILITY': visibility,
#         'TEMPERATURE': temp,
#         'DEW_POINT': dew_point,
#         'REL_HUMIDITY': rel_humidity,
#         'ALTIMETER': altimeter,
#         'LOWEST_CLOUD_LAYER': lowest_cloud,
#         'N_CLOUD_LAYER': n_cloud_layer,
#         'LOW_LEVEL_CLOUD': low_cloud,
#         'MID_LEVEL_CLOUD': mid_cloud,
#         'HIGH_LEVEL_CLOUD': high_cloud,
#         'CLOUD_COVER': cloud_cover,
#         'ACTIVE_WEATHER': active_weather,
#         'WEATHER_SEVERITY': weather_sev,
#         'TEMP_DEW_DIFF': temp_dew_diff,
#         'WIND_INTENSITY': wind_intensity,
#         'VISIBILITY_CATEGORY': visibility_cat,
#         'HUMIDITY_LEVEL': humidity_level,
#         'WIND_DIRECTION': wind_direction_cat,
#         'TOTAL_CLOUD': total_cloud,
#         'CLOUD_COVER_ENCODED': cloud_encoded
#     }
    
#     input_df = pd.DataFrame([input_dict])
    
#     try:
#         # 2. Pass through ColumnTransformer
#         processed_data = preprocessor.transform(input_df)
        
#         # 3. Predict with VotingClassifier
#         prediction = model.predict(processed_data)[0]
#         probability = model.predict_proba(processed_data)[0][1] * 100
        
#         # 4. Display Results beautifully
#         st.subheader("Evaluation Results")
#         if probability < 40:
#             st.markdown(f"<div class='risk-low'><h2>✅ LOW RISK ({probability:.1f}%)</h2>Normal operations expected. Weather conditions are within safe operational thresholds.</div>", unsafe_allow_html=True)
#         elif 40 <= probability < 70:
#             st.markdown(f"<div class='risk-medium'><h2>⚠️ MEDIUM RISK ({probability:.1f}%)</h2>Moderate probability of delay. Possible operational disruptions or holding patterns.</div>", unsafe_allow_html=True)
#         else:
#             st.markdown(f"<div class='risk-high'><h2>🚨 HIGH RISK ({probability:.1f}%)</h2>High probability of delay or cancellation. High chance of schedule disruption. Consider rerouting.</div>", unsafe_allow_html=True)
            
#     except Exception as e:
#         st.error(f"Pipeline Error: Please check data types. Detailed error: {e}")
