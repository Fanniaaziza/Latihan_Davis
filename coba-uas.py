import pymysql
# Panggil fungsi untuk menguji koneksi ke database AdventureWorks (AW)
conn = test_mysql_connection(
    host="localhost", 
    port=3306,         
    user="root",      
    password="",       
    database="dump-dw_aw"  
)

# Periksa apakah koneksi berhasil
if conn:
    print("Connection to AdventureWorks database successful.")
else:
    print("Failed to connect to AdventureWorks database.")
