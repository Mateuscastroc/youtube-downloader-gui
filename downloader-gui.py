from tkinter import *

gui_interface = Tk()

gui_interface.title("YouTube downloader")

label_link_yt = Label(gui_interface, text="Link do video")
label_link_yt.grid(column=0, row=0, padx=2, pady=2)
label_path = Label(gui_interface, text="Pasta de destino")
label_path.grid(column=0, row=2, padx=6, pady=2)

gui_interface.mainloop()


#Definindo o layout da aplicação. imagine como um grid
