from pymysql.connections import Connection
from pymysql import *

try:
    # membuat koneksi ke MySQL
    # karena saya menggunakan panel XAMPP, maka tinggal menyambungkan saja
    # Membuat koneksi ke database yang ada
    koneksi = Connection(
        host="localhost",
        user="root",
        password="",
        database="saham_indonesia",
        port=3306
    )
    kursor = koneksi.cursor() # Membuat kursor untuk mengeksekusi program
    
    # execute SQL query using execute() method.
    kursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = kursor.fetchone()

    print("Database version : %s " %data)

    koneksi.commit() # Commit segala query yang di eksekusi
    koneksi.close() # Menutup commit setelah query di eksekusi

except:
    koneksi.rollback() # Jika gagal terhubung
    print("Database tidak terhubung bro !")


