from pymysql import *
from tkinter import *

koneksi = Connection(host="localhost", user="root", database="saham_indonesia")
kursor = koneksi.cursor()

# Query untuk memilih kolom kode_sektor saja
kursor.execute("""SELECT kode_sektor FROM daftar_sektor;""")
Query_Kode_Sektor = kursor.fetchall()
# print(Query_Kode_Sektor) # Hasilnya bertipe data nested tuple

Kode_Sektor = '' # empty string
for kodesektor in Query_Kode_Sektor:
    Kode_Sektor += kodesektor[0] + '\n'

koneksi.commit()
koneksi.close()

myTuple = (
    ('IDX:A',), ('IDX:B',), ('IDX:C',),
    ('IDX:D',), ('IDX:E',), ('IDX:F',),
    ('IDX:G',), ('IDX:H',), ('IDX:I',),
    ('IDX:J',), ('IDX:K',), ('IDX:Z',)
)

# print(Kode_Sektor, '\n', type(Kode_Sektor))
print("Mencari kata IDX:A dengan indexing = ", str(myTuple[0]))
