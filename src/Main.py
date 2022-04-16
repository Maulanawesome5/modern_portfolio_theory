from tkinter import BOTH, CENTER, LEFT, TOP, ttk
from pymysql import *
from pandas_datareader import DataReader
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

### MySQL Connection
Koneksi = Connection(host="localhost", user="root", database="saham_indonesia")
Kursor = Koneksi.cursor()

## Mengambil data daftar sektor bursa efek indonesia
Kursor.execute("""SELECT * FROM daftar_sektor;""")
Daftar_Sektor = Kursor.fetchall()
# print(Daftar_Sektor, "\n")

# variabel list kosong
Kode_Sektor = []
Nama_Sektor = []
for i in range(len(Daftar_Sektor)):
    Kode_Sektor.append(Daftar_Sektor[i][0])
    Nama_Sektor.append(Daftar_Sektor[i][1])

# print(Kode_Sektor, "\n")
# print(Nama_Sektor, "\n")

## Mengambil data daftar saham berdasarkan sektor yang dipilih
def Select_Stocks():
    ### MySQL Connection
    Koneksi = Connection(host="localhost", user="root", database="saham_indonesia")
    Kursor = Koneksi.cursor()
    Kursor.execute(f"SELECT * FROM daftar_saham_indonesia WHERE sektor_usaha = '{Input_Sektor.get()}';")
    Daftar_Saham = Kursor.fetchall()
    # print(Daftar_Saham, "\n")

    global Ticker_Saham
    global Nama_Emiten

    # variabel list kosong
    Ticker_Saham = []
    Nama_Emiten = []
    for i in range(len(Daftar_Saham)):
        Ticker_Saham.append(Daftar_Saham[i][3])
        Nama_Emiten.append(Daftar_Saham[i][4])

    # print(Ticker_Saham, "\n", len(Ticker_Saham))
    # print(Nama_Emiten, "\n", len(Nama_Emiten))

    Koneksi.commit()
    Koneksi.close()

    # Second window untuk menampilkan daftar saham
    # Second window untuk menampilkan daftar saham
    Window_Saham = tkinter.Toplevel()
    Window_Saham.title(f"Daftar Saham Sektor {Input_Sektor.get()}")
    Window_Saham.iconbitmap('D:/LATIHAN PEMROGRAMAN/(METODE PENELITIAN)/icon/business_stock.ico')

    Frame_Window_Saham = tkinter.Frame(master=Window_Saham, background="#535353", height=300, width=400)
    Frame_Window_Saham.pack(fill=BOTH, anchor=CENTER, side=TOP)

    Mini_Frame = tkinter.Frame(
        master=Frame_Window_Saham, width=40, height=1, background="#535353", relief=tkinter.GROOVE, border=2,
    ) # Mini frame untuk mengatur layout 2 button
    # Mini_Frame.pack(fill=BOTH, anchor=CENTER, side=TOP)
    Mini_Frame.grid(column=1, row=0)

    for i in range(len(Daftar_Saham)):
        # Pilihan_Saham = tkinter.Checkbutton(
        #     master=Frame_Window_Saham, background="#535353", foreground="#ffffff", padx=10, 
        #     selectcolor="#2d2d2d", activebackground="#535353", activeforeground="#ffffff",
        #     text=(str(Ticker_Saham[i]) + "\t" + str(Nama_Emiten[i])), variable=Ticker_Saham[i],
        #     onvalue=Ticker_Saham[i]
        # )
        # Pilihan_Saham.grid(column=0, row=i, sticky=tkinter.W)

        Pilihan_Saham = tkinter.Label(master=Frame_Window_Saham, text=(str(Ticker_Saham[i]) + "\t" + str(Nama_Emiten[i])),
            background="#535353", foreground="#ffffff", activebackground="#535353", activeforeground="#ffffff", justify=LEFT
        )
        Pilihan_Saham.grid(column=0, row=i, sticky=tkinter.W)

    Get_Option_Saham = tkinter.Button(
        master=Mini_Frame, text="Ambil Data Saham", background="#535353", foreground="#ffffff", activebackground="#707070", activeforeground="#ffffff", 
        command=call_dataframe
    )
    Get_Option_Saham.grid(column=0, row=0, sticky=tkinter.W)

    Unselect_Option_Saham = tkinter.Button(master=Mini_Frame, text="Batalkan", background="#535353", foreground="#ffffff", activebackground="#707070", activeforeground="#ffffff", command=Window_Saham.destroy)
    Unselect_Option_Saham.grid(column=1, row=0, sticky=tkinter.E)

# method untuk memanggil dataframe
def call_dataframe():
    df = DataReader(
        [], # nanti diisi ticker saham berupa tipe data string yang digabung dalam satu list
        'yahoo',
        start=startDate.get(),
        end=endDate.get()
    )

### MySQL Connection
Koneksi.commit()
Koneksi.close()


### GUI Apps
## Top Level Widget
Main_Window = tkinter.Tk()
Main_Window.title('Optimasi Portofolio Saham')
Main_Window.iconbitmap('D:/LATIHAN PEMROGRAMAN/(METODE PENELITIAN)/icon/business_stock.ico')
Main_Frame = tkinter.Frame(master=Main_Window, background="#535353", height=300, width=400)
Main_Frame.pack(fill=BOTH, anchor=CENTER, side=TOP)

## Label Widget
Label_Sektor = tkinter.Label(master=Main_Frame, background="#535353", foreground="#ffffff", justify=LEFT, text="Sektor Emiten")
Label_Saham = tkinter.Label(master=Main_Frame, background="#535353", foreground="#ffffff", justify=LEFT, text="Daftar Saham")
Label_Investasi = tkinter.Label(master=Main_Frame, background="#535353", foreground="#ffffff", justify=LEFT, text="Jumlah Investasi")
Label_Tanggal = tkinter.Label(master=Main_Frame, background="#535353", foreground="#ffffff", justify=LEFT, text="Tanggal Transaksi")
Label_Sektor.grid(column=0, row=0, padx=10, pady=5, sticky=tkinter.W)
Label_Saham.grid(column=0, row=1, padx=10, pady=5, sticky=tkinter.W)
Label_Investasi.grid(column=0, row=2, padx=10, pady=5, sticky=tkinter.W)
Label_Tanggal.grid(column=0, row=3, padx=10, pady=5, sticky=tkinter.W)

## Input widget
Input_Sektor = ttk.Combobox(master=Main_Frame, width=37, height=1, justify=LEFT, values=Nama_Sektor, textvariable=Kode_Sektor)
Input_Sektor.grid(column=1, row=0, padx=10, pady=5, sticky=tkinter.W)

Pilih_Saham = tkinter.Button(master=Main_Frame, text="Pilih Saham", background="#535353", foreground="#ffffff", activebackground="#707070", activeforeground="#ffffff", command=Select_Stocks)
Pilih_Saham.grid(column=1, row=1, padx=10, pady=5, sticky=tkinter.W)

Input_Modal_Investasi = tkinter.Entry(master=Main_Frame, width=40, background="#2D2D2D", foreground="#FFFFFF", insertbackground="#FFFFFF")
Input_Modal_Investasi.grid(column=1, row=2, padx=10, pady=5, sticky=tkinter.W)

# Tanggal transaksi
Mini_Frame = tkinter.Frame(master=Main_Frame, width=40, height=1, background="#535353") # Mini frame untuk mengatur layout 3 widget dalam satu kolom
Mini_Frame.grid(column=1, row=3, padx=10, pady=5, sticky=tkinter.W)

startDate = tkinter.Entry(master=Mini_Frame, width=15, background="#2D2D2D", foreground="#FFFFFF", insertbackground="#FFFFFF")
startDate.insert(0, "e.g. 2020/12/31")
startDate.grid(column=0, row=0, sticky=tkinter.W)

sampaiDengan = tkinter.Label(master=Mini_Frame, text="s/d", background="#535353", foreground="#FFFFFF", width=7)
sampaiDengan.grid(column=1, row=0, sticky=tkinter.W)

endDate = tkinter.Entry(master=Mini_Frame, width=15, background="#2D2D2D", foreground="#FFFFFF", insertbackground="#FFFFFF")
endDate.insert(0, "e.g. 2021/12/31")
endDate.grid(column=2, row=0, sticky=tkinter.W)

## Process Widget
Button_Frame = tkinter.Frame(master=Main_Frame, width=40, height=1, background="#535353")
Button_Frame.grid(column=1, row=4, padx=10, pady=5, sticky=tkinter.W)

Optimum_Button = tkinter.Button(master=Button_Frame, text="Optimasi Saham", background="#535353", foreground="#FFFFFF", activebackground="#707070", activeforeground="#ffffff")
Optimum_Button.grid(column=0, row=0, sticky=tkinter.W)

Exit_Button = tkinter.Button(master=Button_Frame, text="Keluar Aplikasi", background="#535353", foreground="#FFFFFF", activebackground="#707070", activeforeground="#ffffff", width=12, command=quit)
Exit_Button.grid(column=1, row=0, sticky=tkinter.E, padx=50)






### GUI Apps
Main_Window.mainloop()