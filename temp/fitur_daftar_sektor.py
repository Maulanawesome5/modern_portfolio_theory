from tkinter import ttk
from pymysql import *
from tkinter import *

koneksi = Connection(host="localhost", user="root", database="saham_indonesia")
kursor = koneksi.cursor()

## Query untuk mengambil seluruh data dari tabel daftar_sektor
kursor.execute("""SELECT * FROM daftar_sektor;""")
Daftar_Sektor = kursor.fetchall()

## Parameter untuk commit dan menutup koneksi SQL setelah proses fetch
koneksi.commit()
koneksi.close()

print(f"Daftar Sektor Emiten Bursa Efek Indonesia \n{Daftar_Sektor}") # Hasilnya bertipe data nested tuple
# print(len(Daftar_Sektor)) # Jumlah isi data = 12

Kode_Sektor = [] # list kosong untuk menampung kode_sektor
Nama_Sektor = [] # list kosong untuk menampung nama_sektor

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

# Fungsi / method untuk menunjukkan opsi yang dipilih melalui combobox
def Cek_Hasil():
    Pilihan = Label(master=root, text=List_Sektor.get())
    Pilihan.pack()

myButton = Button(master=root, text="Tampilkan pilihan", command=Cek_Hasil)
myButton.pack()



root.mainloop()