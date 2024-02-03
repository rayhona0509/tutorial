import tkinter as tk
# from tkinter import*  hohlasak buni yozamz
oyna=tk.Tk()
# {
oyna.title("40-att-22")
oyna.geometry("500x320")
oyna.configure(background="white")

label=tk.Label(oyna, text="UZ-ENG Lug'at",
                font=("Algerian",18),
                foreground="red",
                background="white"
                )
label.pack(pady=15)
uz_entry=tk.Entry(oyna,
                font=("Algerian",18),
                foreground="purple",
                background="white" )
uz_entry.pack()
def tarjimon():
    lugat={
        "salom":"hello",
        "quyosh":"sun",
        "qizil":"red",
        "dars":"lesson"
                }
    suz=uz_entry.get()
    if lugat.get(suz):
        tarjimasi=lugat[suz]
        tarjima.configure(text=tarjimasi)
    else:
        tarjima.configure(text="bunday suz bazada mavjud emas")

button=tk.Button(oyna,text="tarjima qil",command=tarjimon)
button.pack(pady=15)

tarjima=tk.Label(oyna,
                text="tarjimasi",
                font=("Algerian",18),
                foreground="purple",
                background="white")
# }
tarjima.pack()
oyna.mainloop()
