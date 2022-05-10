# happiness.py

import streamlit as st
import pandas as pd
import altair as alt
import os
import toml
import pymysql
import mysql.connector


# Reading data
# toml_data = toml.load("secrets.toml")
# # saving each credential into a variable
# HOST_NAME = toml_data['mysql']['host']
# DATABASE = toml_data['mysql']['database']
# PASSWORD = toml_data['mysql']['password']
# USER = toml_data['mysql']['user']
# PORT = toml_data['mysql']['port']

# conn = pymysql.connect(
#     host= "localhost", #"localhost"
#     port= 3306, 
#     user= "root", #"root"
#     password= "cricket123",
#     db= "happiness", #"Happiness"
#     )

# conn = mysql.connector.connect(
# 	host = "localhost", 
# 	user = "root",
# 	passwd = "cricket123",
# 	database = "happiness")

# df = pd.read_sql_query("SELECT * FROM happiness.`2015`", conn)
# df.tail(10)

# TITLE 
st.title("Happiness")
st.subheader("A Functional **_but_** Non-Functional App 🤠")
# makes the slider for the user to choose country, starting year, ending year, and/or region
# to get country options: get unique values of countries
starting_year = st.slider("Select starting year:", min_value = 2015, max_value = 2019, step = 1)
ending_year = st.slider("Select ending year:", min_value = 2016, max_value = 2019, step = 1)

country_region = st.radio("Choose the area type:", ['Country', 'Region'])
if country_region == "Country":
	# countries_df = pd.read_sql_query("SELECT DISTINCT `Country` FROM `happiness`.`2015` ORDER BY `Country` ASC;", conn)
	# countries_list = df['Country'].to_list()
	countries_list = ['Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Belarus', 'Belgium', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Estonia', 'Ethiopia', 'Finland', 'France', 'Gabon', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Cyprus', 'Norway', 'Oman', 'Pakistan', 'Palestinian Territories', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somaliland region', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
	country = st.selectbox("Select a country:", countries_list)
	st.write("Country:", country)
	# query1 = "SELECT happiness.`" + starting_year + "`.`country`, happiness.`" + starting_year + "`.`Happiness Rank` - happiness.`" + ending_year + "`.`Happiness Rank` AS 'Happiness Rank Difference' FROM happiness.`" + ending_year + "` INNER JOIN happiness.`" + starting_year + "` ON happiness.`" + ending_year + "`.`Country` = happiness.`" + starting_year + "`.`Country` WHERE happiness.`" + ending_year + "`.`Country` = '" + country + "'"
	# df = pd.read_sql_query(query1, conn)
	# st.dataframe(df)


elif country_region == "Region":
	# regions_df = pd.read_sql_query("SELECT DISTINCT `Region` FROM `happiness`.`2015` ORDER BY `Region` ASC;", conn)
	# regions_list = regions_df['Region'].to_list()
	regions_list = ['Australia and New Zealand', 'Central and Eastern Europe', 'Eastern Asia', 'Latin America and Caribbean', 'Middle East and Northern Africa', 'North America', 'Southeastern Asia', 'Southern Asia', 'Sub-Saharan Africa', 'Western Europe']
	region = st.selectbox("Select a region to get the average:", regions_list)
	st.write("Region:", region)
	# query2 = "SELECT happiness.`" + starting_year + "`.`region`, AVG(happiness.`" + starting_year + "`.`Happiness Rank` - happiness.`" + ending_year + "`.`Happiness Rank`) AS 'Happiness Rank Difference' FROM happiness.`" + ending_year + "` INNER JOIN happiness.`" + starting_year + "` ON happiness.`" + ending_year + "`.`Country` = happiness.`" + starting_year + "`.`Country` WHERE happiness.`" + starting_year + "`.`region` = '" + region + "' GROUP BY `" + starting_year + "`.`region`"
	# df = pd.read_sql_query(query2, conn)
	# st.dataframe(df)

	






