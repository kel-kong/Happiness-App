# happiness.py

import streamlit as st
import mysql.connector
import pandas as pd
import altair as alt
import os
import toml
import pymysql.cursors


# Initialize connection.
# Uses st.experimental_singleton to only run once.
# @st.experimental_singleton
# def init_connection():
#     return  mysql.connector.connect(host="localhost", port = 3306, user="root",
#         password="mango123",
#         database="happiness"
#         )

# conn = init_connection()

# # Perform query.
# # Uses st.experimental_memo to only rerun when the query changes or after 10 min.
# @st.experimental_memo(ttl=600)
# def run_query(query):
#     with conn.cursor() as cur:
#         cur.execute(query)
#         return cur.fetchall()

# rows = run_query("SELECT * FROM `2015`;")

# # Print results.
# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")

# # Reading data
# toml_data = toml.load("secrets.toml")
# # saving each credential into a variable
# HOST_NAME = toml_data['mysql']['host']
# DATABASE = toml_data['mysql']['database']
# PASSWORD = toml_data['mysql']['password']
# USER = toml_data['mysql']['user']
# PORT = toml_data['mysql']['port']

# conn = pymysql.connect(
#     host=HOST_NAME,
#     port=int(3306),
#     user=USER,
#     password=PASSWORD,
#     db=DATABASE,
#     cursorclass=pymysql.cursors.DictCursor)

# df = pd.read_sql_query("SELECT * FROM `2015`",
#     conn)
# df.tail(10)

# makes the slider for the user to choose country, starting year, ending year, and/or region
# to get country options: get unique values of countries
# countries_df = pd.read_sql_query("SELECT DISTINCT `Country` FROM `happiness`.`2015`", conn)
# countries_list = df['Country'].to_list()
countries_list = ['H', 'D', 'F']
country = st.selectbox("Select a country:", countries_list)
starting_year = st.slider("Select starting year:", min_value = 2015, max_value = 2019, step = 1)
ending_year = st.slider("Select ending year:", min_value = 2015, max_value = 2019, step = 1)
st.write("Starting Year", starting_year)
st.write("Ending Year", ending_year)


