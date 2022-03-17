# dummy program untuk membuat modern portfolio theory
from tkinter import *
from tkinter import ttk
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
root = tkinter.Tk()
root.title("Optimasi Portofolio Saham")
root.iconbitmap("D:/Aji/[ICON FILE]/business-color_stock_icon-icons.com_53431.ico")


# top level frame
root_frame = Frame(
    master=root,
    background="#535353",
    padx=10,
    pady=10
)
root_frame.grid(column=0, row=0, sticky=(N, W, E, S), columnspan=10, rowspan=10)

# MySQL Parameter
koneksi = Connection(host='localhost', user='root', database='saham_indonesia')
kursor = koneksi.cursor()

# method untuk memilih sektor
def pilihSektor():
    # second widget untuk memilih jenis sektor
    sektor_window = tkinter.Toplevel()
    sektor_window.title('Pilih Sektor Saham')
    sektor_window.iconbitmap("D:/Aji/[ICON FILE]/business-color_stock_icon-icons.com_53431.ico")
    # sektor_window.geometry("400x400")
    
    sektor_window_frame = Frame(master=sektor_window, background="#535353", padx=10, pady=10)
    sektor_window_frame.grid(column=0, row=0, sticky=(N, W, E, S), columnspan=10, rowspan=10)

    # MySQL Parameter
    koneksi = Connection(host='localhost', user='root', database='saham_indonesia')
    kursor = koneksi.cursor()
    
    # Sintaks query
    kursor.execute("SELECT * FROM daftar_sektor;")
    records = kursor.fetchall()
    # print(records)

    kode_sektor = IntVar()
    kode_sektor.set(1)
    
    # Loop thru results
    print_records = list(records) # Mengkonversi fetch data yang bertipe tuple menjadi list

    for text, namasektor, topping in print_records:
        Radiobutton(
            master=sektor_window_frame,
            text=[text, namasektor],
            variable=kode_sektor,
            value=topping,
            foreground="#FFFFFF",
            background="#535353",
            activeforeground="#FFFFFF",
            activebackground="#535353"
        ).grid(column=0, sticky=W, padx=10, pady=2)

    def clicked(value):
        myLabel = Label(master=sektor_window_frame, text=topping)
        myLabel.grid(column=1, row=0, sticky=W)
    
    saveButton = Button(master=sektor_window_frame, text="Save Option", command=lambda: clicked(kode_sektor.get),background="#6A6A6A", activebackground="#707070", foreground="#FFFFFF", activeforeground="#FFFFFF")
    saveButton.grid(column=0, row=12, padx=10, pady=2, sticky=W)

    quitButton = Button(master=sektor_window_frame, text="Cancel", command=sektor_window.destroy, background="#6A6A6A", activebackground="#707070", foreground="#FFFFFF", activeforeground="#FFFFFF")
    quitButton.grid(column=0, row=12, sticky=E)

    # myCheckBox = Checkbutton(master=sektor_window)
    
    # MySQL Parameter
    koneksi.commit()
    koneksi.close()


# method untuk memilih ticker saham setelah memilih sektor
def pilihTickerSaham():
    # second widget untuk memilih jenis sektor
    tickerSaham_window = Toplevel()
    tickerSaham_window.title('Pilih Ticker Saham')
    tickerSaham_window.iconbitmap("D:/Aji/[ICON FILE]/business-color_stock_icon-icons.com_53431.ico")
    tickerSaham_window.geometry("400x400")
    
    # MySQL Parameter
    koneksi = Connection(host='localhost', user='root', database='saham_indonesia')
    kursor = koneksi.cursor()
    

    saveButton = Button(master=tickerSaham_window, text="Save Option")
    saveButton.grid(column=0, row=12, padx=10, pady=2, sticky=W)

    quitButton = Button(master=tickerSaham_window, text="Cancel", command=tickerSaham_window.destroy)
    quitButton.grid(column=0, row=12, sticky=N+S)
    
    # MySQL Parameter
    koneksi.commit()
    koneksi.close()


# Label widget
sektorSaham = Label(master=root_frame, text="Pilih Sektor Saham", background="#535353", foreground="#FFFFFF")
sektorSaham.grid(row=1, column=0, sticky=W, padx=10, pady=5)
sahamLabel = Label(master=root_frame, text="Pilih Kode Saham", background="#535353", foreground="#FFFFFF")
sahamLabel.grid(row=2, column=0, sticky=W, padx=10, pady=5)
investLabel = Label(master=root_frame, text="Jumlah Investasi", background="#535353", foreground="#FFFFFF")
investLabel.grid(row=3, column=0, sticky=W, padx=10, pady=2)
waktuPembelian = Label(master=root_frame, text="Tanggal Transaksi", background="#535353", foreground="#FFFFFF")
waktuPembelian.grid(row=4, column=0, sticky=W, padx=10, pady=5)

# Button widget
sektor_select = Button(master=root_frame, text="Daftar Sektor", command=pilihSektor, background="#6A6A6A", activebackground="#707070", foreground="#FFFFFF", activeforeground="#FFFFFF")
sektor_select.grid(row=1, column=1, sticky=W)
ticker_select = Button(master=root_frame, text="Ticker Saham", command=pilihTickerSaham, background="#6A6A6A", activebackground="#707070", foreground="#FFFFFF", activeforeground="#FFFFFF")
ticker_select.grid(row=2, column=1, sticky=W)
kalkulasi_button = Button(master=root_frame, text="Calculate Portfolio's", background="#6A6A6A", activebackground="#707070", foreground="#FFFFFF", activeforeground="#FFFFFF")
kalkulasi_button.grid(row=5, column=1, sticky=W)
exit_button = Button(master=root_frame, text="Quit Apps", command=quit, anchor=CENTER, background="#6A6A6A", activebackground="#707070", foreground="#FFFFFF", activeforeground="#FFFFFF")
exit_button.grid(row=5, column=1, sticky=E)

# Input kedalam program
investEntry = Entry(
    master=root_frame,
    width=35,
    background="#2D2D2D",
    foreground="#FFFFFF",
    insertbackground="#FFFFFF"
)
investEntry.grid(row=3, column=1)

awalBeli = Entry(
    master=root_frame,
    width=15,
    background="#2D2D2D",
    foreground="#FFFFFF",
    insertbackground="#FFFFFF"
)
awalBeli.insert(0, "e.g. 2020/12/31")
awalBeli.grid(row=4, column=1, sticky=W)

sampaiDengan = Label(master=root_frame, text="s/d", background="#535353", foreground="#FFFFFF")
sampaiDengan.grid(row=4, column=1)

akhirBeli = Entry(
    master=root_frame,
    width=15,
    background="#2D2D2D",
    foreground="#FFFFFF",
    insertbackground="#FFFFFF"
)
akhirBeli.insert(0, "e.g. 2021/12/31")
akhirBeli.grid(row=4, column=1, sticky=E)



# MySQL Parameter
koneksi.commit()
koneksi.close()
# tkinter Parameter
root.mainloop()