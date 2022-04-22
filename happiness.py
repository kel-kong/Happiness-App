# happiness.py

import streamlit as st
import mysql.connector
import pandas as pd
import altair as alt
import os
import toml
import pymysql.cursors


# # Initialize connection.
# # Uses st.experimental_singleton to only run once.
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

# Reading data
toml_data = toml.load("secrets.toml")
# saving each credential into a variable
HOST_NAME = toml_data['mysql']['host']
DATABASE = toml_data['mysql']['database']
PASSWORD = toml_data['mysql']['password']
USER = toml_data['mysql']['user']
PORT = toml_data['mysql']['port']

conn = pymysql.connect(
    host="localhost",
    port=PORT,
    user=USER,
    password=PASSWORD,
    db=DATABASE,
    cursorclass=pymysql.cursors.DictCursor)

df = pd.read_sql_query("SELECT * FROM `2015`",
    conn)
df.tail(10)