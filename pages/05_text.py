import streamlit as st

# Give your app a title
st.title("Streamlit Rocks")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Markdown
st.markdown("This is a bold text **text**")
st.markdown("This is a [link](https://www.streamlit.io)")
st.markdown("# Header1")
st.markdown("## Header2")
st.markdown("### Header3")

# Divider
st.divider()

# Caption
st.caption("This is a caption")

# Code block
st.code("""
import numpy as np
pd.read_csv(my_file.csv)
""")

# LaTeX
st.latex("x = 2^2")

# Output data
st.write("Some text")