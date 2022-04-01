# dummy program untuk membuat modern portfolio theory
from tkinter import *
from tkinter import ttk
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

# method untuk memilih sektor
def Pilih_Sektor():
    global sektor_label
    global Nama_Sektor

    Kode_Sektor = 'IDX:H'
    Nama_Sektor = 'Properti & Real Estate'

    sektor_label = Label(
        master=root_frame, 
        text=Kode_Sektor + "\t" + Nama_Sektor, 
        background="#535353", 
        foreground="#FFFFFF", 
        textvariable=Kode_Sektor
    )
    sektor_label.grid(column=2, row=1, sticky=W, padx=10, pady=5)

# method untuk memilih kode saham berdasarkan sektor
def Pilih_Ticker():
    Kode_Sektor = 'IDX:H'

    Second_Top = Toplevel()
    Second_Top.title(f'Daftar Saham Sektor Properti')
    # Second_Top.resizable(width=False, height=False)
    Second_Top.grid_columnconfigure(index=0, weight=1)
    Second_Top.grid_rowconfigure(index=0, weight=1)

    # MySQL Parameter
    koneksi = Connection(host='localhost', user='root', database='saham_indonesia')
    kursor = koneksi.cursor()

    kursor.execute(f"""SELECT kodeSaham, namaEmiten FROM daftar_saham_indonesia WHERE kode_sektor = '{Kode_Sektor}';""")
    query = kursor.fetchall()

    show_query = '' # empty string
    ticker_only = '' # empty string
    # Lakukan loop untuk unpacking seluruh record data
    for data in query:
        show_query += str(data[0]) + "\t" + str(data[1]) + '\n'

    # Ticker_Label = Label(master=Second_Top, text=show_query, justify='left', padx=10, pady=5)
    # Ticker_Label.grid(column=0, row=0, sticky=W)

    Ticker = Listbox(master=Second_Top, listvariable=show_query)
    Ticker.grid(column=0, row=0, sticky=(W+E))

    scrollbar = ttk.Scrollbar(master=Second_Top, orient=VERTICAL, command=Ticker.yview)
    scrollbar.grid(column=1, row=0, sticky=(N+S))

    Ticker['yscrollcommand'] = scrollbar.set(first=0, last=0)

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
sektor_select = Button(master=root_frame, text="Daftar Sektor", background="#6A6A6A", activebackground="#707070", foreground="#FFFFFF", activeforeground="#FFFFFF",command=Pilih_Sektor)
sektor_select.grid(row=1, column=1, sticky=W)
ticker_select = Button(
    master=root_frame, 
    text="Ticker Saham", 
    background="#6A6A6A", 
    activebackground="#707070", 
    foreground="#FFFFFF", 
    activeforeground="#FFFFFF",
    command=Pilih_Ticker
)
ticker_select.grid(row=2, column=1, sticky=W)
kalkulasi_button = Button(
    master=root_frame, 
    text="Calculate Portfolio's", 
    background="#6A6A6A", 
    activebackground="#707070", 
    foreground="#FFFFFF", 
    activeforeground="#FFFFFF"
)
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