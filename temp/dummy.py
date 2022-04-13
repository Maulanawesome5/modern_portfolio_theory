from pymysql import *
from tkinter import *
from tkinter import ttk

koneksi = Connection(host="localhost", user="root", database="saham_indonesia")
kursor = koneksi.cursor()

## Query untuk mengambil seluruh data dari tabel daftar_sektor
kursor.execute("""SELECT * FROM daftar_sektor;""")
Daftar_Sektor = kursor.fetchall()

## Parameter untuk commit dan menutup koneksi SQL setelah proses fetch
koneksi.commit()
koneksi.close()

""" REFERENSI SINTAKS JIKA ADA YANG BINGUNG
print(f"Data posisi ke [0] = {Daftar_Sektor[0]}") # hasilnya ('IDX:A', 'Energi', 'IDX')
print(f"Data posisi ke [0][0] = {Daftar_Sektor[0][0]}") # hasilnya IDX:A
print(f"Data posisi ke [0][1] = {Daftar_Sektor[0][1]}") # hasilnya Energi
print(f"Data posisi ke [0][2] = {Daftar_Sektor[0][2]}") # hasilnya IDX
    Warning: Daftar_Sektor[boleh increment][mentok sampai 2]
"""


# print(f"Daftar Sektor Emiten Bursa Efek Indonesia \n{Daftar_Sektor}") # Hasilnya bertipe data nested tuple
# print(len(Daftar_Sektor)) # Jumlah isi data = 12

## Akses daftar_sektor yang bertipe data nested tuple
# for i in range(len(Daftar_Sektor)):
#     print(f"Data posisi ke {i} = {Daftar_Sektor[i]}")

Kode_Sektor = []
Nama_Sektor = []

for i in range(len(Daftar_Sektor)):
    j = 0
    if j <= 1:
        Kode_Sektor.append(Daftar_Sektor[i][0])
        Nama_Sektor.append(Daftar_Sektor[i][1])
    # Kode_Sektor,Nama_Sektor.insert(Daftar_Sektor[i][1])

print(Kode_Sektor) # Hasilnya ['IDX:A', 'IDX:B', 'IDX:C', 'IDX:D', 'IDX:E', 'IDX:F', 'IDX:G', 'IDX:H', 'IDX:I', 'IDX:J', 'IDX:K', 'IDX:Z']
print(Nama_Sektor) # Hasilnya ['Energi', 'Barang Baku', 'Perindustrian', 'Barang Konsumen Primer', 'Barang Konsumen Non-Primer', 'Kesehatan', 'Keuangan', 'Properti & Real Estate', 'Teknologi', 'Infrastruktur', 'Transportasi & Logistik', 'Produk Investasi Tercatat']

## Program GUI
root = Tk()
root.geometry('300x300')
root.title('Uji Coba Fitur Sektor')

myLabel = Label(master=root, text="Uji coba memilih isi Combobox")
myLabel.pack()

List_Sektor = ttk.Combobox(master=root, width=30, height=1, justify=LEFT, values=Nama_Sektor, textvariable=Kode_Sektor)
List_Sektor.pack()


def Cek_Hasil():
    Pilihan = Label(master=root, text=List_Sektor.get())
    Pilihan.pack()


def Daftar_Saham():
    koneksi = Connection(host="localhost", user="root", database="saham_indonesia")
    kursor = koneksi.cursor()
    kursor.execute(f"SELECT kodeSaham, namaEmiten FROM daftar_saham_indonesia WHERE sektor_usaha = '{List_Sektor.get()}';")
    daftarSaham = kursor.fetchall()

    # second = Toplevel()
    # second.title(f"Pilih Saham Sektor {List_Sektor.get()}")

    print(daftarSaham)
    
    # myLabel = Label(master=root, text=daftarSaham)
    # myLabel.pack()

    koneksi.commit()
    koneksi.close()


myButton = Button(master=root, text="Tampilkan pilihan", command=Cek_Hasil)
myButton.pack()

pilih_kode_saham = Button(master=root, text="Pilih Saham", command=Daftar_Saham)
pilih_kode_saham.pack()

root.mainloop()