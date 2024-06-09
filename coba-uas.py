import streamlit as st
import pymysql
import pandas as pd

# Fungsi untuk membuat koneksi database
def get_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="", 
            database="dump-dw_aw"
        )
        return conn
    except pymysql.MySQLError as e:
        st.error("Failed to connect to the database.")
        st.error(f"Error: {e}")
        return None

# Ambil koneksi
conn = get_connection()

# Periksa koneksi
if conn is not None:
    st.success("Connection to the database was successful.")
else:
    st.error("Failed to connect to the database.")
