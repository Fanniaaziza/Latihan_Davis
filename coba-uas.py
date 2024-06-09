import pymysql

# Fungsi untuk menguji koneksi
def test_mysql_connection(host, port, user, password, database):
    try:
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        return conn
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

# Panggil fungsi test_mysql_connection untuk menguji koneksi
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
