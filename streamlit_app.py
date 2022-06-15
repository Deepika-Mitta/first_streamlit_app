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
fruits_selected = my_fruits_list.loc[fruits_selected]

#display table on web page
streamlit.dataframe(my_fruit_list)
