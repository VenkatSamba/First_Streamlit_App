import streamlit

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Favorites')

streamlit.text('🥣Omega 3 & Bule berry  oatmeal')

streamlit.text('🥗kale,spinach & rocket smoothe')

streamlit.text('🐔Hard boiled free range egg')

streamlit.text('🥑Avacado Toast')

streamlit.header('🍌🥭Build your own Fruit Smoothie🥝🍇')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
