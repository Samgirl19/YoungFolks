import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# input in terminal: streamlit run dashboard.py
st.title("Water Quality Dashboard")

st.header("Internship Ready Software Development")
st.subheader("Prof. Gregory Reis")
st.divider()

# Load CSV (must be in repo root)
df = pd.read_csv("biscayneBay_waterquality.csv")

# Clean column names (prevents subtle bugs)
df.columns = df.columns.str.strip()

tab1, tab2, tab3, tab4 = st.tabs(
    ["Descriptive Statistics",
     "2d Plots",
     "3d Plots",
     "More"]
)

with tab1:
    st.info("Working on this")
    st.dataframe(df)
    st.caption("Raw Data")
    st.divider()
    st.dataframe(df.describe())
    st.caption("Descriptive Statistics")

with tab2:
    fig1 = px.line(
        df,
        x="Time",
        y="Temperature (c)",
        color="pH"
    )
    st.plotly_chart(fig1)

with tab3:
    fig3 = px.scatter_3d(
        df,
        x="Longitude",
        y="Latitude",
        z="Total Water Column (m)",
        color="Temperature (c)"
    )
    fig3.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig3)

with tab4:
    st.warning("NASA's Astronomy Picture Of the Day")

    # Use Streamlit secrets (or DEMO_KEY fallback)
    api_key = st.secrets.get("NASA_API_KEY", "DEMO_KEY")
    url = "https://api.nasa.gov/planetary/apod"

    try:
        response = requests.get(url, params={"api_key": api_key})
        response.raise_for_status()
        data = response.json()

        if data.get("media_type") == "image":
            st.image(data["url"])

        st.subheader(data["title"])
        st.caption(data["date"])
        st.write(data["explanation"])

    except Exception as e:
        st.error(f"Error fetching NASA APOD: {e}")
