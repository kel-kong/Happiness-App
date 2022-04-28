# happiness.py

import streamlit as st
import pandas as pd
import altair as alt
import os
import toml
import pymysql.cursors


# Reading data
toml_data = toml.load("secrets.toml")
# saving each credential into a variable
HOST_NAME = toml_data['mysql']['host']
DATABASE = toml_data['mysql']['database']
PASSWORD = toml_data['mysql']['password']
USER = toml_data['mysql']['user']
PORT = toml_data['mysql']['port']

conn = pymysql.connect(
    host=HOST_NAME, #"localhost"
    port=int(3306), 
    user=USER, #"root"
    password=PASSWORD,
    db=DATABASE, #"Happiness"
    cursorclass=pymysql.cursors.DictCursor)

df = pd.read_sql_query("SELECT * FROM happiness.`2015`", conn)
df.tail(10)

# TITLE 
st.title("Happiness")
st.subheader("A Functional **_but_** Non-Functional App 🤠")
# makes the slider for the user to choose country, starting year, ending year, and/or region
# to get country options: get unique values of countries
country_region = st.radio("Choose your player:", ['Country', 'Region'])
if country_region == "Country":
	# countries_df = pd.read_sql_query("SELECT DISTINCT `Country` FROM `happiness`.`2015` ORDER BY `Country` ASC;", conn)
	# countries_list = df['Country'].to_list()
	countries_list = ['testing', '1', '2', '3']
	country = st.selectbox("Select a country:", countries_list)
	st.write("Country:", country)

elif country_region == "Region":
	# regions_df = pd.read_sql_query("SELECT DISTINCT `Region` FROM `happiness`.`2015` ORDER BY `Region` ASC;", conn)
	# regions_list = regions_df['Region'].to_list()
	regions_list = ['testing', '1', '2', '3']
	region = st.selectbox("Select a region to get the average:", regions_list)
	st.write("Region:", region)

starting_year = st.slider("Select starting year:", min_value = 2015, max_value = 2019, step = 1)
ending_year = st.slider("Select ending year:", min_value = 2015, max_value = 2019, step = 1)

st.write("Starting Year:", starting_year)
st.write("Ending Year:", ending_year)

# if region =! 'None':
# 	query = "SELECT happiness.`" + starting_year + "`.`Happiness Rank` - happiness.`" + ending_year + "`.`Happiness Rank` AS 'Happiness Rank Difference' FROM happiness.`" + ending_year + "` INNER JOIN happiness.`" + starting_year + "` ON happiness.`" + ending_year + "`.`Country` = happiness.`" + starting_year + "`.`Country` WHERE happiness.`" + ending_year + "`.`Country` = '" + country + "'"

# 	df = pd.read_sql_query(query, conn)
# 	st.write(df)

# elif region == 'None':

# 	query = "SELECT "





