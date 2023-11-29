import streamlit

streamlit.title("First Streamlit App Title for Practice")
streamlit.title("Second title")
streamlit.header('This is a header')
streamlit.text("This is a text")
streamlit.text("This is another text")

import pandas as pd
df = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(df)

# let's create a pick list here so that user can pick the fruit they want to include
selected_fruits = streamlit.multiselect("Pick some fruits : ", list(df.index))

#display the table on page
streamlit.dataframe(selected_fruits)

