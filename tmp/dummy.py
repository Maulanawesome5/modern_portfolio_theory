from pymysql.connections import Connection
from pymysql import *
import pandas as pd

# membuat koneksi ke MySQL
koneksi = Connection(
    host="localhost",
    user="root",
    password="",
    database="saham_indonesia",
    port=3306
)
kursor = koneksi.cursor() # Membuat kursor untuk mengeksekusi program
koneksi.commit() # Commit segala query yang di eksekusi
koneksi.close() # Menutup commit setelah query di eksekusi

# directory file harga saham (sample)
IHSG = "D:/LATIHAN PEMROGRAMAN/(DATA SAHAM)/Master Data/IDX_Composite_master_data.xlsx"

# membuat dataframe dengan modul pandas
df = pd.read_excel(IHSG)
print(df)

