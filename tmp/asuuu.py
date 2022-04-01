from tkinter import *
from pandas_datareader import *

kode_sektor = ['IDX:A', 'IDX:B', 'IDX:C', 'IDX:D', 'IDX:E', 'IDX:F', 'IDX:G', 'IDX:H', 'IDX:I', 'IDX:J', 'IDX:K', 'IDX:Z']
nama_sektor = [
    'Energi',
    'Barang Baku',
    'Perindustrian',
    'Barang Konsumen Primer',
    'Barang Konsumen Non-Primer',
    'Kesehatan',
    'Keuangan',
    'Properti & Real Estate',
    'Teknologi',
    'Infrastruktur',
    'Transportasi & Logistik',
    'Produk Investasi Tercatat'
]

# tkinter GUI syntax
root = Tk()
root.title('First Window')

# menampilkan opsi checkbox
header_label = Label(master=root, text="Pilih Kode Sektor")
header_label.grid(column=0, row=0, padx=10, pady=5, sticky=W)

# method menampilkan loop angka
def pilihSektor():
    # second widget untuk memilih jenis sektor
    sektor_window = Toplevel()
    sektor_window.title('Second Window')

    # karena mengakses daftar kode sektor beserta namanya dari DBMS MySQL sangat merepotkan
    # maka sebagai gantinya saya buat manual agar bisa di tampilkan sebagai checkbox
    # hasil centang/seleksi dari checkbox akan di include pada method pandas_datareader
    kode_sektor = ['IDX:A', 'IDX:B', 'IDX:C', 'IDX:D', 'IDX:E', 'IDX:F', 'IDX:G', 'IDX:H', 'IDX:I', 'IDX:J', 'IDX:K', 'IDX:Z']
    nama_sektor = [
        'Energi',
        'Barang Baku (coming soon)',
        'Perindustrian (coming soon)',
        'Barang Konsumen Primer (coming soon)',
        'Barang Konsumen Non-Primer (coming soon)',
        'Kesehatan',
        'Keuangan (coming soon)',
        'Properti & Real Estate',
        'Teknologi',
        'Infrastruktur',
        'Transportasi & Logistik',
        'Produk Investasi Tercatat (coming soon)'
    ]

    # Parameter untuk looping
    indexNumber = 0
    valueNumber = 0
    rowNumber = 0
    kolomList = 0

    # Loop thru results
    for i in range(12):
        kodesektor = kode_sektor[indexNumber]
        namasektor = nama_sektor[indexNumber]

        # check button widget
        kode_sektorLabel = Checkbutton(
            master=sektor_window,
            text=kodesektor,
            # background="#535353",
            # activeforeground="#FFFFFF",
            variable=StringVar(sektor_window, kodesektor)
        )
        kode_sektorLabel.grid(column=0, row=rowNumber, pady=5, padx=2, sticky=W)

        # Label widget
        nama_sektorLabel = Label(master=sektor_window, text=namasektor)
        nama_sektorLabel.grid(column=1, row=rowNumber, pady=5, padx=1, sticky=W)

        # Button widget
        saveButton = Button(
            master=sektor_window,
            text="Save Option",
            command=simpanKodeSektor
        )
        saveButton.grid(column=1, row=12, padx=10, pady=5, sticky=W)
        quitButton = Button(
            master=sektor_window,
            text="Cancel",
            command=sektor_window.destroy,
            width=10
        )
        quitButton.grid(column=1, row=12, padx=10, pady=5, sticky=E)

        valueNumber += 1
        rowNumber += 1
        indexNumber += 1

# Setelah kode sektor dicentang, maka pada window ticker saham yang tampil hanya dari sektor terpilih
def simpanKodeSektor():
    kode_sektor_label = Label(
        master=root,
        textvariable=kode_sektorLabel
    )
    kode_sektor_label.grid(column=2, row=1, padx=10, pady=5)

start_button = Button(master=root, text='Pencet Goblok !!', command=pilihSektor)
start_button.grid(column=1, row=0, padx=10, pady=5, sticky=W)

# menyimpan hasil centang opsi

# menampilkan opsi yang dipilih





# tkinter GUI syntax
root.mainloop()
