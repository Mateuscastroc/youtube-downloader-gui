from msilib.schema import RadioButton
from tkinter import *

menu = Tk()
menu.title('YouTube Downloader')

downloadOptions = StringVar()

downloadButton = Button(menu, text = "Download", command= print("Botao apertado"))
downloadButton.pack()
# videoLink.pack(

menu.geometry("600x300+1000+300")
menu.resizable(False, False)

videoOptionDownload = RadioButton(menu, text="Baixar video", variable = downloadOptions, value=1)
audioOptionDownload = RadioButton(menu, text="Baixar somente audio", variable = downloadOptions, value= 2)
videoOptionDownload.pack(padx = 5, pady = 5)
audioOptionDownload.pack(padx = 5, pady = 5)

linkVideoLabel = Label(menu, text='Download Video')
linkVideoLabel.pack()

linkEntry = Entry(menu)
linkEntry.pack()


menu.mainloop()
