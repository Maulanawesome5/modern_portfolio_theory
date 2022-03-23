import tkinter

main_window = tkinter.Tk()
main_window.geometry('400x400')

"""
Membuat dummy program untuk menangkap opsi dari checkbutton
1. Membuat top level widget
2. Membuat Label untuk keterangan
3. Membuat Button untuk menampilkan second window
4. Membuat Button untuk menampilkan hasil centang dari checkbutton
"""

def Show_Label():
    showLabel = tkinter.Label(master=main_window, text=str(indexNumber) + " " + kodesektor)
    showLabel.grid(column=2, row=0, sticky=tkinter.W)

def Pilih_Sektor():
    second_window = tkinter.Toplevel()
    Kode_Sektor = ['IDX:A', 'IDX:F', 'IDX:H']
    Nama_Sektor = ['Energi', 'Kesehatan', 'Properti & Real Estate']

    global kodesektor
    global indexNumber

    kodesektor = tkinter.StringVar(second_window, value=Kode_Sektor)
    kodesektor.set('IDX:A')

    # Loop parameter
    indexNumber = 0
    rowNumber = 0

    for i in range(3):
        kodesektor = Kode_Sektor[indexNumber]
        namasektor = Nama_Sektor[indexNumber]

        cek_kode_sektor = tkinter.Checkbutton(
            master=second_window,
            text=kodesektor,
            variable=kodesektor
        )
        cek_kode_sektor.grid(column=0, row=rowNumber, sticky=tkinter.W)

        cek_nama_sektor = tkinter.Label(master=second_window, text=namasektor)
        cek_nama_sektor.grid(column=1, row=rowNumber, sticky=tkinter.W)

        # increment
        indexNumber += 1
        rowNumber += 1

    # Button
    simpan_pilihan = tkinter.Button(
        master=second_window, text="Simpan Opsi", command=Show_Label
    )
    simpan_pilihan.grid(column=1, row=3, sticky=tkinter.W, rowspan=70)
    batalkan_pilihan = tkinter.Button(
        master=second_window, text="Batalkan", command=second_window.destroy
    )
    batalkan_pilihan.grid(column=1, row=3, sticky=tkinter.E, rowspan=70)


mylabel = tkinter.Label(master=main_window, text="Pilih Kode Sektor")
mylabel.grid(column=0, row=0, padx=10, pady=5, sticky=tkinter.W)

openCheckbutton = tkinter.Button(
    master=main_window,
    text="Press Here..!",
    width=13,
    command=Pilih_Sektor
)
openCheckbutton.grid(column=1, row=0, padx=10, pady=5, sticky=tkinter.W)

preview_Option = tkinter.Button(master=main_window, text="Apa yang Dipilih?")
preview_Option.grid(column=1, row=1, padx=10, pady=5, sticky=tkinter.W)

preview_Option_Label = tkinter.Label(master=main_window)
preview_Option_Label.grid(column=0, row=1, padx=10, pady=5, sticky=tkinter.W)





main_window.mainloop()
