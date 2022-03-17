from tkinter import *
import pandas_datareader as web

# main window
root = Tk()
root.title("Aplikasi Nonton Bokep Online Gratis Tanpa Iklan")
root.geometry("500x500")

# Fetch data
ngentotTuple = (
    ('IDX:A', 'Energi', 'IDX'),
    ('IDX:B', 'Barang Baku', 'IDX'),
    ('IDX:C', 'Perindustrian', 'IDX'),
    ('IDX:D', 'Barang Konsumen Primer', 'IDX'),
    ('IDX:E', 'Barang Konsumen Non-Primer', 'IDX'),
    ('IDX:F', 'Kesehatan', 'IDX'),
    ('IDX:G', 'Keuangan', 'IDX'),
    ('IDX:H', 'Properti & Real Estate', 'IDX'),
    ('IDX:I', 'Teknologi', 'IDX'),
    ('IDX:J', 'Infrastruktur', 'IDX'),
    ('IDX:K', 'Transportasi & Logistik', 'IDX'),
    ('IDX:Z', 'Produk Investasi Tercatat', 'IDX')
)

# Casting Fetch data
ngentotList = list(ngentotTuple)

"""
def klikBangsat():
    # second widget
    window_2 = Toplevel()
    window_2.title("Aplikasi Video Call Sex")
    window_2.geometry("400x400")
    
    kode_sektor = StringVar()
    kode_sektor.set(ngentotList[0])

    # Label Widget
    pilihSektor_Label = Label(master=window_2, text="Pilih sektor")
    pilihSektor_Label.grid(column=0, row=0, padx=10, pady=5, sticky=W)

    # Dropdown Menu
    daftar_sektor = OptionMenu(master=window_2, variable=kode_sektor, *ngentotList)
    daftar_sektor.grid(column=1, row=0, padx=10, pady=5, sticky=W)
    
    # for text, namasektor, topping in ngentotList:
    #     Radiobutton(
    #         master=window_2,
    #         text=[text, namasektor],
    #         variable=kode_sektor,
    #         value=topping
    #     ).grid(column=0, sticky=W, padx=10, pady=2)

    def clicked():
        myLabel = Label(master=window_2, text=kode_sektor.get())
        myLabel.grid(column=2, row=0, sticky=W, padx=10, pady=10)
    
    saveButton = Button(master=window_2, text="Save Option", command=clicked)
    saveButton.grid(column=0, row=12, padx=10, pady=2, sticky=W)

    quitButton = Button(master=window_2, text="Cancel", command=window_2.destroy)
    quitButton.grid(column=0, row=12, sticky=N+S)


myButton = Button(master=root, text="Pencet Goblok !", command=klikBangsat)
myButton.pack()
"""

def call_dataframe():
    df = web.DataReader(['PWON.JK', 'APLN.JK'], 'yahoo', start=startDate.get(), end=endDate.get())

    df_label = Label(master=root, text=df)
    df_label.grid(column=0, row=3)


def cekTipeData():
    # Menangkap nilai tanggal yang dimasukkan dari Entry Widget
    tanggalMulai = startDate.get()
    tanggalAkhir = endDate.get()
    
    
    result_Label = Label(master=root, text=tanggalMulai + "\n" + tanggalAkhir)
    result_Label.grid(column=2, row=2, padx=10, pady=5)

    print(type(tanggalAkhir))

    startDate.delete(0, END)
    endDate.delete(0, END)    


# Melihat data tanggal yang dimasukkan dari Entry Widget
inputTanggal = Label(master=root, text="Tanggal Transaksi")
inputTanggal.grid(column=0, row=0, padx=10, pady=5, sticky=W)

startDate = Entry(master=root)
startDate.grid(column=1, row=0, padx=10, pady=5, sticky=W)

dateLabel = Label(master=root, text="s/d")
dateLabel.grid(column=2, row=0, padx=10, pady=5)

preview = Button(master=root, text="Preview", command=cekTipeData)
preview.grid(column=2, row=1, padx=10, pady=5)

preview = Button(master=root, text="View Dataframe", command=call_dataframe)
preview.grid(column=2, row=2, padx=10, pady=5)

endDate = Entry(master=root)
endDate.grid(column=3, row=0, padx=10, pady=5, sticky=E)




root.mainloop()