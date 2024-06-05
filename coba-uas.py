import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Buat koneksi ke database
engine = create_engine('mysql+pymysql://root:@localhost:3306/dump-dw_aw')

# Query SQL untuk mengambil total penjualan per tahun
query_yearly_sales = """
SELECT CalendarYear AS Year, SUM(factfinance.Amount) AS TotalSales
FROM dimtime
JOIN factfinance ON dimtime.TimeKey = factfinance.TimeKey
GROUP BY CalendarYear
ORDER BY CalendarYear
"""

# Baca data ke dalam DataFrame
df_yearly_sales = pd.read_sql(query_yearly_sales, engine)

# Plot perbandingan total penjualan per tahun
st.write("# Perbandingan Total Penjualan Pertahun")
st.line_chart(df_yearly_sales.set_index('Year'))

# Query SQL untuk mengambil data penjualan per wilayah atau region
query_sales_by_region = '''
SELECT
    st.SalesTerritoryRegion AS Country,
    SUM(fs.SalesAmount) AS TotalSales
FROM
    factinternetsales fs
JOIN
    dimsalesterritory st ON fs.SalesTerritoryKey = st.SalesTerritoryKey
GROUP BY
    st.SalesTerritoryRegion
'''

# Baca ke DataFrame
df_sales_by_region = pd.read_sql(query_sales_by_region, engine)

# Buat visualisasi Proporsi Penjualan per Wilayah atau Region (Pie Chart)
st.write("# Proporsi Penjualan per Wilayah atau Region")
fig, ax = plt.subplots()
ax.pie(df_sales_by_region['TotalSales'], labels=df_sales_by_region['Country'], autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Membuat pie chart menjadi lingkaran
st.pyplot(fig)

# Query SQL untuk mengambil data penjualan per kategori produk
query_sales_by_category = '''
SELECT
    pc.EnglishProductCategoryName AS ProductCategory,
    SUM(fs.SalesAmount) AS TotalSales
FROM
    factinternetsales fs
JOIN
    dimproduct p ON fs.ProductKey = p.ProductKey
JOIN
    dimproductsubcategory psc ON p.ProductSubcategoryKey = psc.ProductSubcategoryKey
JOIN
    dimproductcategory pc ON psc.ProductCategoryKey = pc.ProductCategoryKey
GROUP BY
    pc.EnglishProductCategoryName
'''

# Baca ke DataFrame
df_sales_by_category = pd.read_sql(query_sales_by_category, engine)

# Buat visualisasi Komposisi Penjualan per Kategori Produk (Bar Chart)
st.write("# Komposisi Penjualan per Kategori Produk")
fig, ax = plt.subplots()
ax.bar(df_sales_by_category['ProductCategory'], df_sales_by_category['TotalSales'], color='blue')
ax.set(title='Komposisi Penjualan per Kategori Produk',
       ylabel='Total Penjualan',   
       xlabel='Kategori Produk')
plt.xticks(rotation=45)
st.pyplot(fig)

# Query SQL untuk mengambil data penjualan per wilayah dan produk
query_sales_by_region_product = '''
SELECT
    st.SalesTerritoryRegion AS Country,
    pc.EnglishProductCategoryName AS ProductCategory,
    SUM(fs.SalesAmount) AS TotalSales
FROM
    factinternetsales fs
JOIN
    dimsalesterritory st ON fs.SalesTerritoryKey = st.SalesTerritoryKey
JOIN
    dimproduct p ON fs.ProductKey = p.ProductKey
JOIN
    dimproductsubcategory psc ON p.ProductSubcategoryKey = psc.ProductSubcategoryKey
JOIN
    dimproductcategory pc ON psc.ProductCategoryKey = pc.ProductCategoryKey
GROUP BY
    st.SalesTerritoryRegion, pc.EnglishProductCategoryName
'''

# Baca ke DataFrame
df_sales_by_region_product = pd.read_sql(query_sales_by_region_product, engine)

# Buat visualisasi Bubble Plot Hubungan Wilayah dan Penjualan (Bubble Plot)
st.write("# Bubble Plot Hubungan Wilayah dan Penjualan")
fig, ax = plt.subplots(figsize=(10, 6))
for country in df_sales_by_region_product['Country'].unique():
    df_temp = df_sales_by_region_product[df_sales_by_region_product['Country'] == country]
    ax.scatter(df_temp['Country'], df_temp['ProductCategory'], s=df_temp['TotalSales']/500, label=country)
ax.set(title='Bubble Plot Hubungan Wilayah dan Penjualan',
       ylabel='Kategori Produk',
       xlabel='Wilayah')
ax.legend()
st.pyplot(fig)
