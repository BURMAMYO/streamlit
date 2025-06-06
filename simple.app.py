import streamlit as st
import numpy as np
import pandas as pd
import time

# Show Streamlit version and a welcome title
st.write("Streamlit Version = {}".format(st.__version__))
st.title("Hello, Daw Su Mon, It is your heart beat when you were using FaceBook!")

# Create a sidebar progress bar and status text
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

# Initialize chart with random data
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

# Update the chart in a loop
for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text(f"{i}% Complete")
    progress_bar.progress(i)
    chart.add_rows(new_rows)
    time.sleep(0.1)

# Clear the progress bar after completion
progress_bar.empty()

# Add a re-run button
st.button("Re-run")

# Display a number and a simple DataFrame
st.write(1234)
st.write(pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
}))
