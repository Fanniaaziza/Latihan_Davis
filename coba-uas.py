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
        print(f"Error connecting to MySQL: {e}")
        return None

# Panggil fungsi untuk menguji koneksi ke database AdventureWorks (AW)
conn = test_mysql_connection(
    host="localhost",  # Ganti dengan host MySQL Anda
    port=3306,         # Ganti dengan port MySQL Anda
    user="root",       # Ganti dengan username MySQL Anda
    password="",       # Ganti dengan password MySQL Anda
    database="AdventureWorks"  # Ganti dengan nama database AdventureWorks
)

# Periksa apakah koneksi berhasil
if conn:
    print("Connection to AdventureWorks database successful.")
else:
    print("Failed to connect to AdventureWorks database.")
