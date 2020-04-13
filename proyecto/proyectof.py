from tkinter import *
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera calculadora :´)")
ventana.geometry("500x200")
ventana.configure(background="#009670")

'''lineas->'''
la = tk.Label(text='CALCULADORA SERPIENTE', bg="#009670", fg='black', font=('', 10)).place(x=170, y=20)
l1 = tk.Label(text="Numero 1 = ", background="light gray").place(x=80, y=80)
l2 = tk.Label(text="Numero 2 = ", background="light gray").place(x=80, y=100)
l3 = tk.Label(text="Total = ", background="light gray").place(x=255, y=90)

'''variable->'''
Var = tk.DoubleVar()

'''entradas->'''
Total = tk.Entry(ventana, textvariable=Var, width=6).place(x=305, y=91)
entrada1 = tk.Entry(ventana, width=10)
entrada1.place(x=155, y=80)
entrada2 = tk.Entry(ventana, width=10)
entrada2.place(x=155, y=100)


def suma():
    uno = float(entrada1.get())
    dos = float(entrada2.get())
    suma = (uno + dos)
    return Var.set(suma)
def suma():
    uno = float(entrada1.get())
    dos = float(entrada2.get())
    suma = (uno + dos)

    return Var.set(suma)
def resta():
    uno = float(entrada1.get())
    dos = float(entrada2.get())
    resta = (uno - dos)
    return Var.set(resta)
def multiplicar():
    uno = float(entrada1.get())
    dos = float(entrada2.get())
    multiplicar = (uno * dos)
    return Var.set(multiplicar)
def dividir():
    uno = float(entrada1.get())
    dos = float(entrada2.get())
    division = (uno / dos)
    return Var.set(division)

'''botones->'''
boton_sumar = tk.Button(ventana, text="Sumar", width=9, command=suma).place(x=100, y=150)
boton_restar = tk.Button(ventana, text='Restar', width=9, command=resta).place(x=180, y=150)
boton_multiplicar = tk.Button(ventana, text='Multiplicar', width=9, command=multiplicar).place(x=260, y=150)
boton_dividir = tk.Button(ventana, text='Dividir', width=9, command=dividir).place(x=340, y=150)
ventana.mainloop()