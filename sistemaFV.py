from math import ceil
import tkinter
#raiz
raiz = tkinter.Tk()
raiz.title("Sistema FV")
raiz.geometry("700x500")
raiz.resizable(0,0)
raiz.config(bg="black")
#frame
frame = tkinter.Frame(raiz)
frame.pack(fill="both",expand="True") #se empaqueta el frame dentro de la raiz
frame.config(bg="blue")
#label Titulo
etiqueta = tkinter.Label(frame,text="Sistema Fotovoltaico aislado")
etiqueta.config(fg="black",font=("Cortana",25))
etiqueta.pack()
#E requerida
etiqueta = tkinter.Label(frame,text="Energía requerida (Wh)")
etiqueta.config(fg="black",font=("Cortana",15))
etiqueta.pack()
entrada = tkinter.Entry(frame)
entrada.config(justify="center",width=50)
entrada.pack()
#label
texto = "HSP(hora solar pico)"
etiqueta = tkinter.Label(frame,text=texto)
etiqueta.config(fg="black",font=("Cortana",15))
etiqueta.pack()
#entry
entrada = tkinter.Entry(frame)
entrada.config(justify="center",width=50)
entrada.pack()
#button
boton = tkinter.Button(frame,text="Calcular")
boton.config(fg="black")
boton.pack()


consumo_Energia = int(input("Ingrese la energía que requiere para su sistema solar (Wh): "))
hsp = int(input("Ingrese la HSP del lugar (horas): "))
wp = int(input("Ingrese la potencia del módulo solar a utilizar (W): "))
price = int(input("Precio de cada módulo solar($): "))
#cantidad de módulos necesarias para la demanda energética
num_modulos = ceil((consumo_Energia*1.3)/(wp*hsp))
costo_modulos = num_modulos * price
print(f"Para su requerimiento se necesitan {num_modulos} módulos solares de {wp} W y estos tienen un costo total de ${costo_modulos}")

vol_sistema = int(input("Elige el voltaje del sistema (12V,24V,48V): "))
#Banco de baterías
vol_bateria = int(input("Voltaje de la batería (V): "))
Ah_bateria = int(input("Capacidad de la batería (Ah): "))
precio_bateria = int(input("Precio de la batería ($): "))
peso_bateria = int(input("Peso de la batería (kg): "))

eff_inversor = 0.9 
prom_energia_dia = consumo_Energia / eff_inversor  #Wh

 #capacidad del banco
autonomia = 2  #dias
factor_temp = 1.05   #(se agrega un 5%)
DoD = 0.9   #(Litio: 0.9 | Plomo: 0.5)
cap_banco = (prom_energia_dia*autonomia*factor_temp) / DoD   #(Wh)
Ah_banco = cap_banco / vol_sistema
Wh_banco = vol_sistema * Ah_banco

series_baterias = ceil(vol_sistema / vol_bateria)  #numero de baterias en serie           | La función ceil() redondea los valores que tengan decimal a el siguiente entero
paralelos_baterias = ceil(Ah_banco / Ah_bateria)  #numero de baterias en paralelo
total_baterias = series_baterias*paralelos_baterias
precio_banco = precio_bateria * total_baterias
peso_banco = peso_bateria * total_baterias
print(f"Se necesitan {total_baterias} baterías, {series_baterias} baterías en serie y {paralelos_baterias} en paralelo.")
print(f"Las {total_baterias} baterías suministran {vol_sistema}V con {Ah_banco:.2f}Ah ({Wh_banco:.2f}Wh) y estas tienen un precio de ${precio_banco} y un peso de {peso_banco} kg.")

#controlador de carga

raiz.mainloop()