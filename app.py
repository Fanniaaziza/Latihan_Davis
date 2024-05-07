import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Membaca database
data = pd.read_csv("tips.csv")

# Menampilkan judul di halaman web
st.title('Scatter Plot')

# Scatter plot dengan day melawan tip
plt.scatter(data['day'], data['tip'])

# Menambahkan Judul Plot
plt.title("Scatter Plot")

# Mengatur label X dan Y
plt.xlabel('Day')
plt.ylabel('Tip')

# Menampilkan plot menggunakan Streamlit
st.pyplot(plt)
