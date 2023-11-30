import streamlit
import snowflake.connector
import pandas as pd
import requests
from urllib.error import URLError

streamlit.title("First Streamlit App Title for Practice")
streamlit.title("New Healthy Diner")
streamlit.header(' 🥣 Brekfast Menu - Header')
streamlit.text("This is a text")
streamlit.text("This is another text  🐔 🥑🍞 ")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

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

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())



fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)


# new section added in Badge 2 lesson 12
streamlit.header('Fruityvice Fruit Advice')
try:
  fruit_choice = streamlit.text_input('what fruit would you like info about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get info")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error()

    
# function definition
def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
      fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
      return fruityvice_normalized
#section to display fruityvice api repsonse
streamlit.header("Fruityvice Fruit Advice")
try:
  fruit_choice = streamlit.text_input('What fruit would you like info about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get info")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#move fruit load list query and load into a button action
streamlit.header("The fruit load list contains : ")
#snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
#add a button to load the fruit
if streamlit.button('Get fruit load list'):
  my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)








fruityvice_response1 = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
fruityvice_normalized1 = pd.json_normalize(fruityvice_response1.json())

streamlit.dataframe(fruityvice_normalized1)


# Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response2= requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized2 = pd.json_normalize(fruityvice_response2.json())

streamlit.dataframe(fruityvice_normalized2)

#don't run anything past here while we troubleshoot

streamlit.stop()

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
selected_fruit = streamlit.multiselect("What fruits would you like information about? ", my_data_rows)

streamlit.write("Thanks for selecting ", selected_fruit[0])

# inserting more values in the snowflake table from streamlit
my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')");

