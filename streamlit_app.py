import os

import plotly.express as px
import streamlit as st
from pandas import read_csv

from src.df_transforms import add_empty_dates, cast_df
from src.google_drive import get_google_sheet

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title="Progress tracker",
    page_icon=":woman_climbing:",  # This is an emoji shortcode. Could be a URL too.
)

spreadsheet_id = "10TIgTG7NW2RIHw3AaoMExAj5v1HVSWawaZG1mQsk9zg"
out_dir = "tmp/"


os.makedirs(out_dir, exist_ok=True)
filepath = get_google_sheet(spreadsheet_id, out_dir, "raw_data.csv")

raw_df = read_csv("./tmp/raw_data.csv")
casted_df = cast_df(raw_df)
df = add_empty_dates(casted_df)

# Set the title that appears at the top of the page.
"""
# :woman_climbing: Progress tracker

**Welcome to Ruth's progress tracker!**
This page reads from a view-only Google Sheet and displays the data.
"""

st.subheader("Daily session view", divider="red")

session_fig = px.bar(
    df,
    x="date",
    y=["pull_up_session", "indoor_session", "outdoor_session", "hang_session"],
    height=400,
    labels={"value": "Number of Sessions", "variable": "Session Type"},
)

st.plotly_chart(session_fig)

# -----------------------------------------------------------------------------

st.subheader("Max V grade", divider="orange")

max_v_fig = px.line(df, x="date", y="max_v_grade", height=400)

st.plotly_chart(max_v_fig)
# -----------------------------------------------------------------------------
