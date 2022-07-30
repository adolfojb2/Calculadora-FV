from distutils.command.config import config
from math import ceil
from tkinter import *
#raiz
raiz = Tk()
raiz.title("Sistema FV")
#se agrega el icono de la ventana
img = PhotoImage(file='C:\\Users\\BetinBracamontes\\OneDrive - Universidad del Magdalena\\2022\\PYTHON\\Sistema FV\\solar.png')
raiz.iconphoto(False,img)
#frame
myframe = Frame(raiz)
myframe.pack(fill=None, expand=False) #se empaqueta el frame dentro de la raiz
myframe.config(width=700, height=500)
#imagen principal
miImagen = PhotoImage(file='C:\\Users\\BetinBracamontes\\OneDrive - Universidad del Magdalena\\2022\\PYTHON\\Sistema FV\\solar.png')
Label(myframe,image=miImagen).grid(row=0,column=0,padx=10,pady=10,columnspan=2)
#E requerida
etiqueta1 = Label(myframe,text="Energía total requerida (Wh)")
etiqueta1.config(fg="black",font=("Cortana",12),justify="left")
etiqueta1.grid(row=1,column=0,padx=10,pady=10,sticky="e")
entrada1 = Entry(myframe)
entrada1.grid(row=1,column=1,padx=10,pady=10)
#HSP
etiqueta2 = Label(myframe,text="HSP (horas)")
etiqueta2.config(fg="black",font=("Cortana",12),justify="left")
etiqueta2.grid(row=2,column=0,padx=10,pady=10,sticky="e")
entrada2 = Entry(myframe)
entrada2.grid(row=2,column=1,padx=10,pady=10)
#Potencia Modulo Solar
etiqueta3 = Label(myframe,text="Potencia módulo (w)")
etiqueta3.config(fg="black",font=("Cortana",12),justify="left")
etiqueta3.grid(row=3,column=0,padx=10,pady=10,sticky="e")
entrada3 = Entry(myframe)
entrada3.grid(row=3,column=1,padx=10,pady=10)
#precio módulo solar
etiqueta4 = Label(myframe,text="Precio módulo ($)")
etiqueta4.config(fg="black",font=("Cortana",12),justify="left")
etiqueta4.grid(row=4,column=0,padx=10,pady=10,sticky="e")
entrada4 = Entry(myframe)
entrada4.grid(row=4,column=1,padx=10,pady=10)
#button
boton = Button(myframe,text="Calcular")
boton.config(fg="black")
boton.grid(row=5,column=0,padx=10,pady=10,columnspan=2)


# consumo_Energia = int(input("Ingrese la energía que requiere para su sistema solar (Wh): "))
# hsp = int(input("Ingrese la HSP del lugar (horas): "))
# wp = int(input("Ingrese la potencia del módulo solar a utilizar (W): "))
# price = int(input("Precio de cada módulo solar($): "))
# #cantidad de módulos necesarias para la demanda energética
# num_modulos = ceil((consumo_Energia*1.3)/(wp*hsp))
# costo_modulos = num_modulos * price
# print(f"Para su requerimiento se necesitan {num_modulos} módulos solares de {wp} W y estos tienen un costo total de ${costo_modulos}")

# vol_sistema = int(input("Elige el voltaje del sistema (12V,24V,48V): "))
# #Banco de baterías
# vol_bateria = int(input("Voltaje de la batería (V): "))
# Ah_bateria = int(input("Capacidad de la batería (Ah): "))
# precio_bateria = int(input("Precio de la batería ($): "))
# peso_bateria = int(input("Peso de la batería (kg): "))

# eff_inversor = 0.9 
# prom_energia_dia = consumo_Energia / eff_inversor  #Wh

#  #capacidad del banco
# autonomia = 2  #dias
# factor_temp = 1.05   #(se agrega un 5%)
# DoD = 0.9   #(Litio: 0.9 | Plomo: 0.5)
# cap_banco = (prom_energia_dia*autonomia*factor_temp) / DoD   #(Wh)
# Ah_banco = cap_banco / vol_sistema
# Wh_banco = vol_sistema * Ah_banco

# series_baterias = ceil(vol_sistema / vol_bateria)  #numero de baterias en serie           | La función ceil() redondea los valores que tengan decimal a el siguiente entero
# paralelos_baterias = ceil(Ah_banco / Ah_bateria)  #numero de baterias en paralelo
# total_baterias = series_baterias*paralelos_baterias
# precio_banco = precio_bateria * total_baterias
# peso_banco = peso_bateria * total_baterias
# print(f"Se necesitan {total_baterias} baterías, {series_baterias} baterías en serie y {paralelos_baterias} en paralelo.")
# print(f"Las {total_baterias} baterías suministran {vol_sistema}V con {Ah_banco:.2f}Ah ({Wh_banco:.2f}Wh) y estas tienen un precio de ${precio_banco} y un peso de {peso_banco} kg.")

# #controlador de carga

raiz.mainloop()