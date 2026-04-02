import streamlit as st
import pandas as pd
import ollama
import json
import folium
from streamlit_folium import st_folium
from gtts import gTTS  # NEW: Voice Engine
import io              # NEW: Memory management for audio

# Page Configuration
st.set_page_config(
    page_title="Project Sentinel",
    page_icon="🚨",
    layout="wide"
)
# Title
st.markdown(
    "<h1 style='text-align: center;'>🚨 Project Sentinel: Command Center</h1>",unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center;'>### Live Emergency Triage & Geospatial Mapping</h3>",unsafe_allow_html=True)
# Divider
st.markdown("---")
# App Memory (Session State)
if 'triage_complete' not in st.session_state:
    st.session_state.triage_complete = False
if 'processed_data' not in st.session_state:
    st.session_state.processed_data = None
# Hardcoded Coordinates
LOCATION_COORDS = {
    "Sector 62": [28.6208, 77.3639],
    "GL Bajaj Hostel": [28.4728, 77.4820],
    "Main Highway": [28.5500, 77.2500],
    "Central Park": [28.6328, 77.2197],
    "Ring Road, Old Warehouse": [28.5800, 77.2200]
}
# Load the Data
@st.cache_data
def load_data():
    df = pd.read_csv("data/mock_emergencies.csv")
    return df
df = load_data()
# Build the Top Layout
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("📡 Raw Inbound Crisis Feed")
    st.dataframe(df, use_container_width=True)
with col2:
    st.subheader("🧠 NLP Triage Engine")   
    if st.button("Run AI Triage Pipeline"):
        with st.spinner("Llama 3.2 is analyzing incoming data..."):
            severities = []
            locations = []       
            for index, row in df.iterrows():
                msg = row['message']               
                prompt = f"""
                You are a highly precise Emergency Dispatch AI operating in the Delhi NCR region.
                Analyze the incoming text. Use these STRICT rules:
                - Critical: Immediate threat to life, structural collapse, major fires.
                - Moderate: Severe property damage, waterlogging, impassable roads.
                - Low: Minor inconveniences, slow traffic, lost pets.

                Respond ONLY in valid JSON format with exactly two keys:
                "severity": (String) strictly 'Critical', 'Moderate', or 'Low'.
                "location": (String) extract specific sector, street, or landmark. If none, output 'None'.
                
                Message: "{msg}"
                """
                
                try:
                    response = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': prompt}], format='json')
                    clean_text = response['message']['content'].replace("```json", "").replace("```", "").strip()
                    response_data = json.loads(clean_text)
                    
                    severities.append(response_data.get('severity', 'Unknown'))
                    
                    loc = response_data.get('location', 'None')
                    if "Sector 62" in loc: loc = "Sector 62"
                    if "Bajaj" in loc: loc = "GL Bajaj Hostel"
                    if "Highway" in loc: loc = "Main Highway"
                    if "Park" in loc: loc = "Central Park"
                    if "Warehouse" in loc or "Ring Road" in loc: loc = "Ring Road, Old Warehouse"
                    
                    locations.append(loc)
                    
                except Exception as e:
                    severities.append("Error")
                    locations.append("Error")

            df['Severity'] = severities
            df['Extracted_Location'] = locations
            
            st.session_state.processed_data = df
            st.session_state.triage_complete = True

    if st.session_state.triage_complete:
        st.success("Triage Complete!")
        
        display_df = st.session_state.processed_data
        st.dataframe(display_df[['message', 'Severity', 'Extracted_Location']], use_container_width=True)
        
        # --- PHASE 3: THE LIVE MAP ---
        st.markdown("---")
        st.subheader("🗺️ Live Threat Map")
        
        m = folium.Map(location=[28.5355, 77.3910], zoom_start=11, tiles="cartodbdark_matter")
        
        for i, row in display_df.iterrows():
            loc_name = row['Extracted_Location']
            sev = row['Severity']
            
            if loc_name in LOCATION_COORDS:
                coords = LOCATION_COORDS[loc_name]
                
                if sev == "Critical":
                    color = "red"
                elif sev == "Moderate":
                    color = "orange"
                else:
                    color = "green"
                    
                folium.Marker(
                    location=coords,
                    popup=f"{sev}: {loc_name}",
                    icon=folium.Icon(color=color, icon="info-sign"),
                ).add_to(m)
        
        st_folium(m, width=1200, height=500)

        # --- PHASE 4: ACCESSIBILITY AUDIO DISPATCH ---
        st.markdown("---")
        st.subheader("🔊 Automated Accessibility Dispatch (Voice Alerts)")
        st.info("Generating localized audio warnings for vulnerable residents in affected zones...")
        
        # Only trigger alarms for Critical and Moderate threats
        alert_df = display_df[display_df['Severity'].isin(['Critical', 'Moderate'])]
        
        # Create columns so the audio players line up nicely
        audio_cols = st.columns(len(alert_df) if len(alert_df) > 0 else 1)
        
        col_index = 0
        for i, row in alert_df.iterrows():
            loc_name = row['Extracted_Location']
            sev = row['Severity']
            
            # The script the AI will read aloud
            warning_script = f"Attention. A {sev} emergency has been confirmed near {loc_name}. Please follow local evacuation protocols immediately."
            
            # Generate the audio file in memory
            tts = gTTS(text=warning_script, lang='en', slow=False)
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            
            # Display it in the dashboard
            with audio_cols[col_index]:
                st.markdown(f"**Target:** {loc_name} ({sev})")
                st.audio(fp, format="audio/mp3")
            col_index += 1

    else:
        st.info("Click the button above to run the local Llama 3 model and generate the threat map.")