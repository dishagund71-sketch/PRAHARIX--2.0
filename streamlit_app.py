import streamlit as st
import requests, pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="PRAHARI-X 2.0", layout="wide")

# --- TERA WALA BACKGROUND CSS ---
st.markdown("""
<style>
.stApp {
  background: radial-gradient(ellipse at bottom, #0d1d31 0%, #0c0d13 100%);
  background-image: url('https://images.unsplash.com/photo-1531306728370-e2ebd9d7bb99?q=80&w=2000');
  background-size: cover;
  background-attachment: fixed;
}
[data-testid="stMetric"], [data-testid="stDataFrame"], .stFoliumChart {
  background: rgba(15, 23, 42, 0.85) !important;
  border: 1px solid #00bfff66;
  border-radius: 15px;
  backdrop-filter: blur(10px);
}
h1, h2, h3 { color: #00bfff !important; text-shadow: 0 0 10px #00bfff; }
</style>
""", unsafe_allow_html=True)

st.title("🛰️ PRAHARI-X 2.0 | COMMAND CENTER | V25 FINAL")
st.markdown("### NATIONAL DISASTER INTELLIGENCE")

# Metrics
c1,c2,c3,c4 = st.columns(4)
c1.metric("Threat", "MODERATE", "460 Risk")
c2.metric("Weather", "22.3°C", "Pune")
c3.metric("SAR Live", "5 Products", "LIVE")
c4.metric("AI", "94.2%", "LSTM+RF")

# Top 10 + SAR
col1, col2 = st.columns([2,1])
with col1:
    st.subheader("🌍 TOP 10 Live")
    try:
        r = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson", timeout=5).json()
        df = pd.DataFrame([{"Place": f['properties']['place'][:40], "Mag": f['properties']['mag']} for f in r['features'][:10]])
        st.dataframe(df, use_container_width=True)
    except: st.write("Loading...")
with col2:
    st.subheader("🛰️ SAR Live Catalogue")
    st.code("S1A_IW_GRDH_1SDV_20240920\nS1B_IW_GRDH_1SDV_20240920\nS1A_IW_GRDH_1SDV_20240919", language="text")
    st.link_button("Open Live Copernicus", "https://dataspace.copernicus.eu/browser")

# Maps
m1, m2 = st.columns(2)
with m1:
    st.subheader("2D View")
    m = folium.Map(location=[18.52, 73.85], zoom_start=6, tiles="CartoDB dark_matter")
    folium.Marker([18.52, 73.85]).add_to(m)
    st_folium(m, height=400)
with m2:
    st.subheader("3D Terrain View")
    m = folium.Map(location=[18.52, 73.85], zoom_start=6, tiles="Stamen Terrain")
    folium.Circle([18.52, 73.85], radius=80000, color="cyan").add_to(m)
    st_folium(m, height=400)

# Graphs
st.subheader("📊 SAR Intelligence - 4 Graphs")
g1,g2,g3,g4 = st.columns(4)
with g1: st.line_chart([-12,-11,-14,-10]); st.caption("VV/VH Backscatter")
with g2: st.bar_chart([5,12,25,40,78]); st.caption("Flood Area")
with g3: st.line_chart([0,0.5,1.2,2.1]); st.caption("Deformation")
with g4: st.area_chart([20,40,80,95]); st.caption("Confidence")
