# dummy program untuk membuat modern portfolio theory
from tkinter import *
from pandas_datareader import DataReader
from pymysql import *
import tkinter

# top level widget
root = tkinter.Tk()
root.title("Optimasi Portofolio Saham")
root.iconbitmap("D:/Aji/[ICON FILE]/business-color_stock_icon-icons.com_53431.ico")

# top level frame
root_frame = Frame(master=root, background="#535353", padx=10, pady=10)
root_frame.grid(column=0, row=0, sticky=(N, W, E, S), columnspan=10, rowspan=10)

# MySQL Parameter
koneksi = Connection(host='localhost', user='root', database='saham_indonesia')
kursor = koneksi.cursor()

def Show_Label():
    showLabel = Label(master=root_frame, text=kodesektor, background="#535353", foreground="#FFFFFF")
    showLabel.grid(column=2, row=0, padx=10, pady=5, sticky=W)

# method untuk memilih sektor
def pilihSektor():
    # second widget untuk memilih jenis sektor
    sektor_window = tkinter.Toplevel()
    sektor_window.title('Pilih Sektor Saham')
    sektor_window.iconbitmap("D:/Aji/[ICON FILE]/business-color_stock_icon-icons.com_53431.ico")

    # karena mengakses daftar kode sektor beserta namanya dari DBMS MySQL sangat merepotkan
    # maka sebagai gantinya saya buat manual agar bisa di tampilkan sebagai checkbox
    # hasil centang/seleksi dari checkbox akan di include pada method pandas_datareader
    Kode_Sektor = ['IDX:A', 'IDX:B', 'IDX:C', 'IDX:D', 'IDX:E', 'IDX:F', 'IDX:G', 'IDX:H', 'IDX:I', 'IDX:J', 'IDX:K', 'IDX:Z']
    Nama_Sektor = [
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

    # Dummy variable untuk melakukan beberapa task
    indexNumber = 0
    rowNumber = 0
    global kodesektor
    global namasektor
    kodesektor = StringVar(sektor_window, value=Kode_Sektor)
    kodesektor.set('IDX:H')

    # Loop thru results
    for i in range(12):
        kodesektor = Kode_Sektor[indexNumber]
        namasektor = Nama_Sektor[indexNumber]

        # check button widget
        cek_kode_sektor = Checkbutton(
            master=sektor_window,
            text=kodesektor,
            variable=kodesektor
        )
        cek_kode_sektor.grid(column=0, row=rowNumber, pady=5, padx=2, sticky=W)

        # Label widget
        nama_sektorLabel = Label(master=sektor_window, text=namasektor)
        nama_sektorLabel.grid(column=1, row=rowNumber, pady=5, padx=1, sticky=W)

        # Button widget
        saveButton = Button(
            master=sektor_window,
            text="Save Option",
            command=Show_Label
        )
        saveButton.grid(column=1, row=12, padx=10, pady=5, sticky=W)
        quitButton = Button(
            master=sektor_window,
            text="Cancel",
            command=sektor_window.destroy,
            width=10
        )
        quitButton.grid(column=1, row=12, padx=10, pady=5, sticky=E)

        rowNumber += 1
        indexNumber += 1


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


# method untuk memanggil dataframe
def call_dataframe():
    df = DataReader(
        [], # nanti diisi ticker saham berupa tipe data string yang digabung dalam satu list
        'yahoo',
        start=startDate.get(),
        end=endDate.get()
    )

    # menampilkan dataframe
    df_label = Label(master=root, text=df)
    df_label.grid()


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
investEntry = Entry(master=root_frame, width=35, background="#2D2D2D", foreground="#FFFFFF", insertbackground="#FFFFFF")
investEntry.grid(row=3, column=1)

startDate = Entry(master=root_frame, width=15, background="#2D2D2D", foreground="#FFFFFF", insertbackground="#FFFFFF")
startDate.insert(0, "e.g. 2020/12/31")
startDate.grid(row=4, column=1, sticky=W)

sampaiDengan = Label(master=root_frame, text="s/d", background="#535353", foreground="#FFFFFF")
sampaiDengan.grid(row=4, column=1)

endDate = Entry(master=root_frame, width=15, background="#2D2D2D", foreground="#FFFFFF", insertbackground="#FFFFFF")
endDate.insert(0, "e.g. 2021/12/31")
endDate.grid(row=4, column=1, sticky=E)





# MySQL Parameter
koneksi.commit()
koneksi.close()
# tkinter Parameter
root.mainloop()