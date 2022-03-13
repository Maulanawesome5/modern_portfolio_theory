from pymysql.connections import Connection
from pymysql import *
from tkinter import *
import pandas as pd

# membuat koneksi ke MySQL
koneksi = Connection(
    host="localhost",
    user="root",
    password="",
    database="saham_indonesia",
    port=3306
)
kursor = koneksi.cursor() # Membuat kursor untuk mengeksekusi program

# GUI Widget
root = Tk()
root.geometry('400x400')

# Method 
def pilihSektor():
    # membuat koneksi ke MySQL
    koneksi = Connection(
        host="localhost",
        user="root",
        database="saham_indonesia",
        port=3306
    )
    kursor = koneksi.cursor() # Membuat kursor untuk mengeksekusi program

    # second level widget
    scnd_widget = Toplevel()
    scnd_widget.geometry('400x400')

    # Slidebar widget
    slideWidget = Scrollbar(
        master=scnd_widget,
        orient=VERTICAL
    )
    slideWidget.grid(row=0, column=0)

    # kursor.execute("SELECT kode_sektor FROM daftar_sektor;")
    # daftar_sektor = kursor.fetchall() # akan otomatis dikonversi menjadi tipe data tuple
    
    # Query the database
    kursor.execute("SELECT * FROM daftar_sektor;")
    records = kursor.fetchall()
    print(records)

    # Loop thru results
    print_records = ''
    variables = IntVar(master=scnd_widget)
    
    # for i in range(10):
        
    
    query_label = Label(master=scnd_widget, text=print_records)
    query_label.grid(row=0, column=0, columnspan=2)

    koneksi.commit() # Commit segala query yang di eksekusi
    koneksi.close() # Menutup commit setelah query di eksekusi


myLabel = Label(master=root, text="Pilih Sektor Saham")
myLabel.grid(row=0, column=0)

myButton = Button(master=root, text="Klik Saya!", command=pilihSektor)
myButton.grid(row=0, column=1)



koneksi.commit() # Commit segala query yang di eksekusi
koneksi.close() # Menutup commit setelah query di eksekusi
root.mainloop()