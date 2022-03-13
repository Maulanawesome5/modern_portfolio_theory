# dummy program untuk membuat modern portfolio theory
from tkinter import *
from pymysql import *
import tkinter

"""
Tabel 1. daftar_saham_indonesia
____________________________________________________________________________________________________________________
id | kode_sektor |      sektor_usaha        | kodeSaham |         namaEmiten           | tglListing  | papanBursa   |
1  |IDX:A        |Energi                    |ADMR       |Adaro Minerals Indonesia Tbk  | 2022 Jan 03 | Pengembangan |
153|IDX:H        |Properti & Real Estate    |URBN       |Urban Jakarta Propertindo Tbk | 2018 Dec 10 | Pengembangan |


Tabel 2. daftar_sektor
___________________________________________
id | kode_sektor |   nama_sektor  | bursa |
1  |IDX:A        |Energi          |IDX    |
2  |IDX:B        |Barang Baku     |IDX    |

Tabel 3. sektorenergi
_________________________________________________________________________________________________________________________________
id | kode_sektor |      sektor_usaha        | kodeSaham |         namaEmiten           | tglListing  |jumlahSaham | papanBursa   |
1  |IDX:A        |Energi                    |ADMR       |Adaro Minerals Indonesia Tbk  | 2022 Jan 03 | 1234567890 | Pengembangan |
73 |IDX:A        |Energi                    |WOWS       |Ginting Jaya Energi Tbk       | 2019 Nov 10 | 1234567890 | Pengembangan |

Tabel 4. sektorproperti
id | kode_sektor |      sektor_usaha        | kodeSaham |         namaEmiten           | tglListing  |jumlahSaham | papanBursa   |
1  |IDX:H        |Properti & Real Estate    |ADCP       |Adhi Commuter Properti Tbk    | 2022 Jan 03 | 1234567890 | Pengembangan |
80 |IDX:H        |Properti & Real Estate    |URBN       |Urban Jakarta Propertindo Tbk | 2019 Nov 10 | 1234567890 | Pengembangan |
"""

# top level widget
root = Tk()
root.title("Optimasi Portofolio Saham")
root.iconbitmap("D:/Aji/[ICON FILE]/business-color_stock_icon-icons.com_53431.ico")
root.geometry("400x400")

# MySQL Parameter
koneksi = Connection(host='localhost', user='root', database='saham_indonesia')
kursor = koneksi.cursor()

# method untuk memilih sektor
def pilihSektor():
    # second widget untuk memilih jenis sektor
    sektor_window = Toplevel()
    sektor_window.title('Pilih Sektor Saham')
    sektor_window.iconbitmap("D:/Aji/[ICON FILE]/business-color_stock_icon-icons.com_53431.ico")
    sektor_window.geometry("400x400")

    # MySQL Parameter
    koneksi = Connection(host='localhost', user='root', database='saham_indonesia')
    kursor = koneksi.cursor()
    
    # Sintaks query
    kursor.execute("SELECT * FROM daftar_sektor;")
    records = kursor.fetchall()
    print(records)

    kode_sektor = StringVar()
    kode_sektor.set("IDX:")
    
    # Loop thru results
    print_records = list(records)

    for text, namasektor, topping in print_records:
        Radiobutton(
            master=sektor_window,
            text=[text, namasektor],
            variable=kode_sektor,
            value=topping
        ).grid(column=0, sticky=W, padx=10, pady=2)

    def clicked(value):
        myLabel = Label(master=sektor_window, text=value)
        myLabel.grid(column=1, row=0, sticky=W)
    
    saveButton = Button(master=sektor_window, text="Save Option", command=lambda: clicked(kode_sektor.get))
    saveButton.grid(column=0, row=12, padx=10, pady=2, sticky=W)

    quitButton = Button(master=sektor_window, text="Cancel", command=sektor_window.destroy)
    quitButton.grid(column=0, row=12, sticky=N+S)

    # myCheckBox = Checkbutton(master=sektor_window)
    
    # MySQL Parameter
    koneksi.commit()
    koneksi.close()


# Label widget
sektorSaham = Label(master=root, text="Pilih Sektor Saham")
sektorSaham.grid(row=0, column=0, sticky=W, padx=10, pady=5)
sahamLabel = Label(master=root, text="Pilih Kode Saham")
sahamLabel.grid(row=1, column=0, sticky=W, padx=10, pady=5)
investLabel = Label(master=root, text="Jumlah Investasi")
investLabel.grid(row=2, column=0, sticky=W, padx=10, pady=2)
waktuPembelian = Label(master=root, text="Tanggal Transaksi")
waktuPembelian.grid(row=3, column=0, sticky=W, padx=10, pady=5)

# Button widget
sektor_select = Button(master=root, text="Click Here", command=pilihSektor)
sektor_select.grid(row=0, column=1, sticky=W)
ticker_select = Button(master=root, text="Click Here", command=pilihSektor)
ticker_select.grid(row=1, column=1, sticky=W)
kalkulasi_button = Button(master=root, text="Calculate Portfolio's")
kalkulasi_button.grid(row=5, column=1, sticky=W)
exit_button = Button(master=root, text="Quit Apps", command=quit, anchor=CENTER)
exit_button.grid(row=5, column=1, sticky=E)

# Input kedalam program
pilihSektor = Radiobutton()
investEntry = Entry(
    master=root,
    width=35,
)
investEntry.grid(row=2, column=1)
tanggalBeli = ""


# MySQL Parameter
koneksi.commit()
koneksi.close()
# tkinter Parameter
root.mainloop()