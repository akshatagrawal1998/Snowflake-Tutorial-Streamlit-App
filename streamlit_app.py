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



fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


import requests
fruityvice_response1 = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
fruityvice_normalized1 = pd.json_normalize(fruityvice_response1.json())

streamlit.dataframe(fruityvice_normalized1)


# Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response2= requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized2 = pd.json_normalize(fruityvice_response2.json())

streamlit.dataframe(fruityvice_normalized2)


import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

# querying from snowflake table using streamlit

my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit list contains")
streamlit.text(my_data_row)

streamlit.header("The fruit list contains - one row")
streamlit.dataframe(my_data_row)

# let's fetch all rows instead of just one
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit list contains - all rows")
streamlit.dataframe(my_data_rows)


# challenge lab
# let's create a pick list here so that user can pick the fruit they want to include
selected_fruits_index = streamlit.multiselect("What fruits would you like information about? ", my_data_row)

