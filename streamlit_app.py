import streamlit

streamlit.title("First Streamlit App Title for Practice")
streamlit.title("New Healthy Diner")
streamlit.header(' 🥣 Brekfast Menu - Header')
streamlit.text("This is a text")
streamlit.text("This is another text  🐔 🥑🍞 ")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
df = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(df)

# let's create a pick list here so that user can pick the fruit they want to include
selected_fruits_index = streamlit.multiselect("Pick some fruits : ", list(df.index))

streamlit.dataframe(df.iloc[selected_fruits_index])

# now let's change the indexes from 0,1,2,.. to fruits column
df = df.set_index('Fruit')

# let's create a pick list here so that user can pick the fruit they want to include
selected_fruits_index = streamlit.multiselect("Pick some fruits : ", list(df.index))
# now since we have a categprical column as index, we'll use loc instead of iloc
streamlit.dataframe(df.loc[selected_fruits_index])



# let's put a pick list here so that user can pick the fruit they want to include
streamlit.multiselect("Pick fruits : ", list(df.index),['Avocado','Strawberries'])




# Let's Call the Fruityvice API from Our Streamlit App!

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
