from tkinter import *

# main window
root = Tk()
root.title("Aplikasi Nonton Bokep Online Gratis Tanpa Iklan")
root.geometry("300x100")

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

def klikBangsat():
    # second widget
    window_2 = Toplevel()
    window_2.title("Aplikasi Video Call Sex")
    window_2.geometry("400x400")
    
    kode_sektor = StringVar()
    kode_sektor.set("")

    for text, namasektor, topping in ngentotList:
        Radiobutton(
            master=window_2,
            text=[text, namasektor],
            variable=kode_sektor,
            value=topping
        ).grid(column=0, sticky=W, padx=10, pady=2)

    def clicked(value):
        myLabel = Label(master=window_2, text=value)
        myLabel.grid(column=1, row=0, sticky=W)
    
    saveButton = Button(master=window_2, text="Save Option", command=lambda: clicked(kode_sektor.get()))
    saveButton.grid(column=0, row=12, padx=10, pady=2, sticky=W)

    quitButton = Button(master=window_2, text="Cancel", command=window_2.destroy)
    quitButton.grid(column=0, row=12, sticky=N+S)


myButton = Button(master=root, text="Pencet Goblok !", command=klikBangsat)
myButton.pack()

root.mainloop()