import tkinter as tk
from turtle import bgcolor

window = tk.Tk()
window.title("Sistema de Ventas Bazar")
window.geometry("800x200")


frmTitulo = tk.Frame(master=window,height=100, bg="white")
frmTitulo.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

lblTitulo = tk.Label(
    master=frmTitulo, 
    text="Sistema de Ventas",
    bg="white",
    padx=50,
    pady=50, 
    font=("Verdana", 18))
lblTitulo.pack()

btnIngresar = tk.Button(master=frmTitulo, text="Ingresar", font=("Verdana", 14))
btnIngresar.pack()

window.mainloop()


