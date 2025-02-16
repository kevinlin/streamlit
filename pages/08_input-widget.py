import streamlit as st
import pandas as pd
from streamlit import number_input

# Button
primary_btn = st.button(type="primary", label="Primary")
secondary_btn = st.button(type="secondary", label="Secondary")

if primary_btn:
    st.write("Primary button clicked!")

if secondary_btn:
    st.write("Secondary button clicked!")

# Checkbox
st.divider()
checkbox = st.checkbox("Remember me")

if checkbox:
    st.write("I will remember you")
else:
    st.write("I will forget you")

# Radio button
st.divider()

df = pd.read_csv('data/sample.csv')

radio = st.radio("Select a column", df.columns[1:], index=0)
st.write(f"You selected: {radio}")

# Selectbox
st.divider()

select = st.selectbox("Select a column", df.columns[1:], index=0)
st.write(select)

# Multiselect
st.divider()

multiselect = st.multiselect("Select columns", df.columns[1:], max_selections=2)
st.write(multiselect)

# Slider
st.divider()

slider = st.slider("Select a value", 0, 100, 50)
st.write(slider)

# Text input
st.divider()

text_input = st.text_input("Enter your name", placeholder="Johen Doh")
st.write(f"Hello, {text_input}")

# Number input
st.divider()

num_input = st.number_input("Enter a number", min_value=0, max_value=100, value=50, step=5)
st.write(num_input)

# Text area
st.divider()

text_area = st.text_area("Enter your message", height=200, placeholder="Hello there!")
st.write(text_area)
