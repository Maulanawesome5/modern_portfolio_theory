# dummy program untuk membuat modern portfolio theory
from tkinter import *
from pymysql import *
import tkinter

# top level widget
root = Tk()
root.title("Optimasi Portofolio Saham")
root.iconbitmap("D:/Aji/[ICON FILE]/business-color_stock_icon-icons.com_53431.ico")
root.geometry("400x400")

# MySQL Parameter
koneksi = Connection(host='localhost', user='root', database='saham_indonesia')
kursor = koneksi.cursor()

def pilihSektor():
    # MySQL Parameter
    koneksi = Connection(host='localhost', user='root', database='saham_indonesia')
    kursor = koneksi.cursor()
    
    sektor_window = Toplevel()
    sektor_window.title('Pilih Sektor Saham')
    sektor_window.iconbitmap("D:/Aji/[ICON FILE]/business-color_stock_icon-icons.com_53431.ico")
    sektor_window.geometry("400x400")

    # query the database
    kursor.execute("SELECT kode_sektor, nama_sektor FROM daftar_sektor;") # tabel data akan dikonversi menjadi tuple
    records = kursor.fetchall()
    # print(records) # tabel data akan dikonversi menjadi tuple
    # print(records[0:]) # (('IDX:A', 'Energi'), ('IDX:B', 'Barang Baku').....('IDX:Z', 'Produk Investasi Tercatat'))
    # print(records[0][0]) # IDX:A
    # print(records[0][0:]) # ('IDX:A', 'Energi', 'IDX')


    # Loop thru result
    printRecords = ""
    ind = 0
    
    for record in printRecords:
        Label(master=sektor_window, text=printRecords)
        Label.grid()

    # cancel_option = Button(master=sektor_window, text="Cancel Options",command=sektor_window.destroy)
    # cancel_option.grid(row=1, column=0)
    
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


# def chooseSector():
#     # second window harus dibuat di dalam fungsi, agar muncul
#     # ketika tombol ditekan, bukan muncul bersamaan dengan root window
#     sektor_window = Toplevel()
#     sektor_window.title('Pilih Sektor Saham')
#     sektor_window.iconbitmap("D:/Aji/[ICON FILE]/business-color_stock_icon-icons.com_53431.ico")
#     sektor_window.geometry("400x400")
    
#     r = IntVar()
#     r.set("2")

#     NAMA_SEKTOR = [
#         "Barang Baku",
#         "Energi",
#         "Infrastruktur",
#         "Keuangan",
#         "Kesehatan",
#         "Non-Primer",
#         "Perindustrian",
#         "Primer",
#         "Properti",
#         "Teknologi",
#         "Transportasi"
#     ]
    
#     row_index = 0
#     sektor = StringVar(master=sektor_window)
#     sektor.set("Barang Baku")

#     for nama in NAMA_SEKTOR:
#         # Radiobutton(master=sektor_window, text=nama).grid()
#         # Checkbutton(
#         #     master=sektor_window,
#         #     text=nama,
#         #     variable=sektor
#         # ).grid(row=row_index, column=0, sticky=W, padx=10, pady=3)
        
#         Radiobutton(
#             master=sektor_window,
#             text=nama,
#             variable=r,
#             value=r
#         ).grid(row=row_index, column=0, sticky=W, padx=10, pady=3)
        
#         row_index += 1

#     # namaSektor_Label = Label(master=sektor_window, text=namaSektor)
#     # namaSektor_Label.grid(row=0, column=0)

#     add_option = Button(master=sektor_window, text="Save Options")
#     add_option.grid(row=row_index, column=0)

#     cancel_option = Button(
#         master=sektor_window,
#         text="Cancel Options",
#         command=sektor_window.destroy
#     )
#     cancel_option.grid(row=row_index, column=1)