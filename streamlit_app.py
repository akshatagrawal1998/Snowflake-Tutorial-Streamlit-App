import streamlit

streamlit.title("First Streamlit App Title for Practice")
streamlit.title("Second title")
streamlit.header('This is a header')
streamlit.text("This is a text")
streamlit.text("This is another text")

import pandas
df = pd.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(df)
