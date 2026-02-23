import streamlit as st
import pandas as pd
import plotly.express as px
from apis import apod_generator
import os

# input in terminal: streamlit run dashboard.py
st.title("Water Quality Dashboard")

st.header("Internship Ready Software Development")
st.subheader("Prof. Gregory Reis")
st.divider()

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

    url = "https://api.nasa.gov/planetary/apod?api_key=HbYkzkYIywGwqCOXAox9q0p3JtnPk6m3eZmnE7bW"
    api_key = os.getenv("NASA_API_KEY", "DEMO_KEY")

    response = apod_generator(url, api_key)

    st.image(response["url"])
    st.subheader(response["title"])
    st.caption(response["date"])
    st.write(response["explanation"])

    # TODO: using the streamlit methods
    # TODO: display teh APOD image and title and other features

load_dotenv(find_dotenv())

NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
URL = "https://api.nasa.gov/planetary/apod?api_key=HbYkzkYIywGwqCOXAox9q0p3JtnPk6m3eZmnE7bW"
print("NASA_API_KEY:", os.getenv("NASA_API_KEY"))

def apod_generator(url, api_key):
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

apod_data = apod_generator(URL, NASA_API_KEY)

print(apod_data["title"])
print(apod_data["hdurl"])
print(apod_data["date"])
print(apod_data["explanation"])


