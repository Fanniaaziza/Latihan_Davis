import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Function to establish a database connection using pymysql
@st.cache(allow_output_mutation=True)
def get_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="", 
        database="db_Adventureworks"
    )
    return conn

# Buat engine SQLAlchemy
engine = create_engine('mysql+pymysql://root:@localhost:3306/dump-dw_aw')

# Query SQL untuk mengambil total penjualan pertahun
query = """
SELECT CalendarYear AS Year, SUM(factfinance.Amount) AS TotalSales
FROM dimtime
JOIN factfinance ON dimtime.TimeKey = factfinance.TimeKey
GROUP BY CalendarYear
ORDER BY CalendarYear
"""

# Baca data ke dalam DataFrame
df_comparison_year = pd.read_sql(query, engine)

# Menampilkan DataFrame
st.write("# Perbandingan Total Penjualan Pertahun")
st.write(df_comparison_year)

# Plot perbandingan total penjualan per tahun
plt.figure(figsize=(10, 6))
plt.plot(df_comparison_year['Year'], df_comparison_year['TotalSales'], marker='o')
plt.title('Perbandingan Total Penjualan Pertahun')
plt.xlabel('Tahun')
plt.ylabel('Total Penjualan')
plt.grid(True)

# Menampilkan plot menggunakan st.pyplot()
st.pyplot()
