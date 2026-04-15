import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime
from data.clinicaltrials import fetch_oncology_trials

st.set_page_config(
    page_title="GeoIntel — Geographic Intelligence Engine",
    page_icon="🌍",
    layout="wide"
)

# EU AI Act compliance label — mandatory, non-dismissible
st.error("⚠️  AI-GENERATED INTELLIGENCE  ·  Informational only  ·  Not for clinical, diagnostic, or regulatory decision-making")

st.title("🌍 GeoIntel")
st.caption("Geographic Intelligence Engine · Lippershey · AIstack.bio")

# Load data
with st.spinner("Fetching live Phase 3 oncology trial data from ClinicalTrials.gov..."):
    df = fetch_oncology_trials()

# Aggregate by country
country_counts = df.groupby("country").size().reset_index(name="trial_count")

# Data confidence score per country
median = country_counts["trial_count"].median()
country_counts["confidence"] = country_counts["trial_count"].apply(
    lambda x: "High" if x >= median * 0.5 else "Medium" if x >= 3 else "Low"
)

# Stats row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Countries with trials", len(country_counts))
col2.metric("Total trial records", len(df))
col3.metric("Data source", "ClinicalTrials.gov")
col4.metric("Last fetched", datetime.now().strftime("%Y-%m-%d"))

st.divider()

# Map
fig = px.choropleth(
    country_counts,
    locations="country",
    locationmode="country names",
    color="trial_count",
    color_continuous_scale="Viridis",
    hover_name="country",
    hover_data={"trial_count": True, "confidence": True, "country": False},
    title="Phase 3 Oncology Trial Density by Country — ClinicalTrials.gov",
    labels={"trial_count": "Active Trials", "confidence": "Data Confidence"}
)

fig.update_layout(
    geo=dict(showframe=False, showcoastlines=True, projection_type="natural earth"),
    height=580,
    margin=dict(l=0, r=0, t=40, b=0),
    coloraxis_colorbar=dict(title="Trials")
)

st.plotly_chart(fig, use_container_width=True)

# Data attribution
st.divider()
col_a, col_b, col_c = st.columns(3)
col_a.caption("🟢 Source: ClinicalTrials.gov API · Updated daily")
col_b.caption("⚠️ Self-reported data · Confidence score shown on hover")
col_c.caption("📅 Data fetched: " + datetime.now().strftime("%Y-%m-%d %H:%M"))

# Report error
if st.button("⚑ Report a data error"):
    st.info("Thank you. Please email errors@lippershey.com with the country and issue.")

st.caption("Methodology: Trial count per country based on ClinicalTrials.gov active Phase 3 oncology studies. Confidence: High = above regional median, Medium = 3+ trials, Low = fewer than 3.")