import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/sample.csv')

# Line chart
# st.line_chart(df, x="year", y=["col1", "col2", "col3"])
#
# # Area chart
# st.area_chart(df, x="year", y=["col1", "col2"])
#
# # Bar chart
# st.bar_chart(df, x="year", y=["col1", "col2", "col3"])

# Map
geo_df = pd.read_csv('data/sample_map.csv')
st.map(geo_df)

# Matplotlib
fig, ax = plt.subplots()
ax.plot(df.year, df.col3)
ax.set_title("Sales figures")
ax.set_xlabel("Year")
ax.set_title("Sales")
fig.autofmt_xdate()

st.pyplot(fig)