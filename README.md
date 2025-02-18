# 🧗‍♀️ Progress tracker

A Streamlit app that reads from a public google sheet and plots the data.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://inventory-tracker-template.streamlit.app/)

### How to run it on your own machine

1. Create virtual environment

   ```
   $ pyenv virtualenv 3.11 progress-tracker
   ```

2. Install the requirements

   ```
   $ pyenv activate progress-tracker
   $ pip install -r requirements.txt
   $ pre-commit install
   ```

3. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
