import numpy as np
import pandas as pd
import streamlit as st
import time

# st.write("Here's our first attempt at using data to create a table:")

# Write a data frame
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

# Widget - Selectbox for options
option = st.selectbox(
    'Which number do you like best?',
    df['first column'])

'You selected: ', option

# dataframe = pd.DataFrame(np.random.randn(10, 20),
#                          index=('row %d' % i for i in range(10)),
#                          columns=('col %d' % i for i in range(20)))
# st.dataframe(dataframe.style.highlight_max(axis=0))

# Draw a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# Plot a map
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 100] + [37.76, -122.4],
#     columns=['lat', 'lon'])
# st.map(map_data)

# Widget - Checkbox to show/hide data
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    chart_data

# Layout - Sidebar
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

x = st.sidebar.slider('x', )  # 👈 this is a widget
st.sidebar.write(x, 'squared is', x * x)

st.sidebar.text_input("Your name", key="name")

# You can access the value at any point with:
st.sidebar.write(st.session_state.name)

# Layout - Columns
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

# Show progress
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'
