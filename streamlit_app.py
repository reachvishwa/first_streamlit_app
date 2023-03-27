import streamlit;
import pandas;
import requests;
streamlit.title('My parents New Healthy Diner');
streamlit.header('Breakfast Menu');
streamlit.text('🥗Omega3 & 🥣 Blueberry 🥗Oatmeal');
streamlit.text('🥑Kale, 🍞Spinach and 🍞Rocket Smoothie');
streamlit.text('🐔Hard boiled Freerange Egg');


streamlit.header('Breakfast Favorites');
streamlit.text('🥗Omega3 & 🥣 Blueberry 🥗Oatmeal');
streamlit.text('🥑Kale, 🍞Spinach and 🍞Rocket Smoothie');
streamlit.text('🐔Hard boiled Freerange Egg');

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
my_fruit_list = my_fruit_list.set_index('Fruit');
# Display the table on the page.
streamlit.dataframe(my_fruit_list);

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']);
fruits_to_show = my_fruit_list.loc[fruits_selected];

# display the data frame
streamlit.dataframe(fruits_to_show);

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon");
streamlit.text(fruityvice_response);

streamlit.header("Fruityvice Fruit Advice!");
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "watermelon");
streamlit.text(fruityvice_response.json());


# write your own comment -what does the next line do? 
# transposes the json response into a tabular form
fruityvice_normalized = pandas.json_normalize();
# write your own comment - what does this do?
# displays data as a table with unique row identifier
streamlit.dataframe(fruityvice_normalized);
