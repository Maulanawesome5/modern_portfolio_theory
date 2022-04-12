from pymysql import *
from fitur_daftar_sektor import *

koneksi = Connection(host="localhost", user="root", database="saham_indonesia")
kursor = koneksi.cursor()

# execute kode saham
kursor.execute("""SELECT kodeSaham FROM daftar_saham_indonesia ORDER BY '{Kode_Sektor}';""")
Query_Kode_Saham = kursor.fetchall()

# execute nama emiten
kursor.execute("""SELECT namaEmiten FROM daftar_saham_indonesia ORDER BY '{Kode_Sektor}';""")
Query_Nama_Saham = kursor.fetchall()

# empty string
Kode_Saham = ''
Nama_Emiten = ''

for kode in Query_Kode_Saham:
    Kode_Saham += kode[0] + '\n'

for nama in Query_Nama_Saham:
    Nama_Emiten += nama[0] + '\n'

print(len(Kode_Saham), len(Nama_Emiten))

koneksi.commit()
koneksi.close()
