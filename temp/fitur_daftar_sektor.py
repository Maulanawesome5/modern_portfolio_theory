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

print(Kode_Sektor, '\n', type(Kode_Sektor))

# method untuk memanggil window baru yang berisi pilihan kode sektor
def Pilih_Sektor():
    koneksi = Connection(host="localhost", user="root", database="saham_indonesia")
    kursor = koneksi.cursor()
    
    kursor.execute("SELECT nama_sektor FROM daftar_sektor;")
    Query_Nama_Sektor = kursor.fetchall()

    Nama_Sektor = '' # empty string
    for namasektor in Query_Nama_Sektor:
        Nama_Sektor += namasektor[0] + '\n'

    L_kode_sektor = Label(master=root, text=Nama_Sektor)
    L_kode_sektor.pack()

    koneksi.commit()
    koneksi.close()

# window tkinter
root = Tk()
root.title('Lihat sektor saham')

B_pilih_sektor = Button(master=root, text='Tekan ini..!', command=Pilih_Sektor)
B_pilih_sektor.pack()

root.mainloop()

""" ===== SEKTOR YANG TERSEDIA DIDALAM DBMS =====
    IDX:A Energi
    IDX:F Kesehatan
    IDX:H Properti & Real Estate
    IDX:I Teknologi
    IDX:J Infrastruktur
    IDX:K Transportasi & Logistik
"""
