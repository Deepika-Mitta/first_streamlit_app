import streamlit

streamlit.title("My Mom's New Healthy Diner")

streamlit.header("Breakfast Favourites")

streamlit.text("🥣 omega 3 & Blueberry Oatmeal")

streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")

streamlit.text("🐔 Hard-Boiled Free-Range Egg")

streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#pick list to pick a fruit a they want
fruits_selected = streamlit.multiselect("Pick a fruits: ", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display table on web page
streamlit.dataframe(fruits_to_show)

#New section to display FruityVice API response
streamlit.header("FruityVice Fruit Advice!")
fruit_choice = streamlit.text_input('what fruit would you like information about?', 'kiwi')
streamlit.write('The user entered', fruit_choice)
                 
import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json()) #just writes the data to the screen

#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)

