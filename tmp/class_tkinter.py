import tkinter as tk

class Application(tk.Frame): # Inherit dari class Frame package tkinter

    # Class Constructor
    def __init__(self, master=None):
        tk.Frame.__init__(self, master) # Memanggil constructor untuk super class Frame
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()

    def createWidgets(self):
        # Membuat root window resizeable
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Label widget
        self.firstLabel = tk.Label(self, text='Nama Lengkap')
        self.firstLabel.grid(column=0, row=0, sticky=tk.W, padx=10, pady=5)
        self.firstLabel = tk.Label(self, text='Nomor KTP/Passpor')
        self.firstLabel.grid(column=0, row=1, sticky=tk.W, padx=10, pady=5)
        self.firstLabel = tk.Label(self, text='Tempat Tanggal Lahir')
        self.firstLabel.grid(column=0, row=2, sticky=tk.W, padx=10, pady=5)
        self.firstLabel = tk.Label(self, text='Alamat Sekarang')
        self.firstLabel.grid(column=0, row=3, sticky=tk.W, padx=10, pady=5)
        self.firstLabel = tk.Label(self, text='Pekerjaan')
        self.firstLabel.grid(column=0, row=4, sticky=tk.W, padx=10, pady=5)

        # Membuat Entry widget (menggunakan while loop)
        indexNumber = 0
        rowNumber = 0

        while indexNumber < 5:
            formEntry = tk.Entry(self, width=40)
            formEntry.grid(column=1, row=rowNumber, sticky=tk.W, padx=10, pady=5)

            # increment
            indexNumber += 1
            rowNumber += 1

        # Button widget
        self.quitButton = tk.Button(self, text='Quit', command=self.quit) # membuat tombol quit
        self.quitButton.grid(column=2, row=0, sticky=tk.N+tk.S+tk.E+tk.W, padx=10, pady=5) # meletakkan tombol pada aplikasi


# end class

app = Application() # instantiate class Application
app.master.title('Sample Application')
app.mainloop()