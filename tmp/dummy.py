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
master_data_directory = "D:/LATIHAN PEMROGRAMAN/(DATA SAHAM)/Master Data"

# membuat dataframe dengan modul pandas
ihsg = pd.read_excel(master_data_directory+"/IDX_Composite_master_data.xlsx")
print(ihsg)

apln = pd.read_excel(master_data_directory+"/APLN_master_data.xlsx")
print(apln)
