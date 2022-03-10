from pymysql.connections import Connection
from pymysql import *
from tkinter import *

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

    kursor.execute("SELECT * FROM daftar_sektor;")
    kdsektor = kursor.fetchall()


    # second level eidget
    scnd_widget = Toplevel()
    scnd_widget.geometry('400x400')

    kodeSektor = ""
    namaSektor = ""
    rowNumber = 0
    
    while rowNumber <= 12:
        rowNumber += 1


    myLabel = Label(master=scnd_widget, text="")
    myLabel.grid(row=0, column=0)

    # myButton = Button(master=scnd_widget, text="Klik Saya!", command=pilihSektor)
    # myButton.grid(row=0, column=1)

    koneksi.commit() # Commit segala query yang di eksekusi
    koneksi.close() # Menutup commit setelah query di eksekusi


myLabel = Label(master=root, text="Pilih Sektor Saham")
myLabel.grid(row=0, column=0)

myButton = Button(master=root, text="Klik Saya!", command=pilihSektor)
myButton.grid(row=0, column=1)



koneksi.commit() # Commit segala query yang di eksekusi
koneksi.close() # Menutup commit setelah query di eksekusi
root.mainloop()