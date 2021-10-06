from tkinter import *
from tkinter import ttk
import numpy.random.common
import numpy.random.bounded_integers
import numpy.random.entropy
import math
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk as itk
from math import pi
import numpy as np
from matplotlib import pyplot as plt
#def calculate(*args):
 #   try:
   #     value = float(feet.get())
    #    meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    #except ValueError:
    #    pass
class Application(ttk.Frame):
	def __init__(self, main_window):
		super().__init__(main_window)
		main_window.title("Configurar Accionamiento")
		main_window.geometry("300x200")
		main_window.configure(width=300, height=200)
		
	#	self.combo = ttk.Combobox(self,width=50,state="readonly")
	#	self.combo.place(x=0, y=0)
	#	self.combo["values"] = ["Seleccione fuente","Fuente DC Directa","Puente 1F Completo Controlado", "Puente 1F Incompleto Controlado", "Puente 3F Completo Controlado", "Puente 3F Incompleto Controlado","Puente 3F Completo Controlado con Diodo Descarga","Chopper 4 Cuadrantes"]
	#	self.combo.current(0)
	#	self.combo.bind("<<ComboboxSelected>>", self.selection_changed)
		self.caso=-1
	#	self.place(width=300, height=200)
		self.entry1=ttk.Entry(self,textvariable=dato1)
		self.entry2=ttk.Entry(self,textvariable=dato2)
		self.entry3=ttk.Entry(self,textvariable=dato3)
		
def selection_changed(self):
	global boxsel
	print("Nuevo elemento seleccionado:", boxsel.get())
	global dato1,dato2,dato3,app,numerovalor
	numerovalor=boxsel.current()
	if numerovalor==0:
		print("nada")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.caso=0
	if numerovalor==1:
		print("Fuente DC Directa")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)
		app.labelv1=ttk.Label(app,text="Voltaje DC")
		app.labelv1.place(x=80,y=30)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.caso=1

	if numerovalor==2:
		print("Puente Monofasico Completo Controlado")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)
		app.labelv1=ttk.Label(app,text="Voltaje ")
		app.labelv1.place(x=80,y=30)
		app.labelv2=ttk.Label(app,text="Angulo de disparo (grados) ")
		app.labelv2.place(x=80,y=60)
		app.labelv3=ttk.Label(app,text="Ancho de pulso (grados)")
		app.labelv3.place(x=80,y=90)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.entry2= ttk.Entry(app,width=7, textvariable=dato2)
		app.entry2.place(x=30,y=60)
		app.entry3= ttk.Entry(app,width=7, textvariable=dato3)
		app.entry3.place(x=30,y=90)
		app.caso=2

	if numerovalor==3:
		print("Puente Monofasico incompleto Controlado")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)
		app.labelv1=ttk.Label(app,text="Voltaje ")
		app.labelv1.place(x=80,y=30)
		app.labelv2=ttk.Label(app,text="Angulo de disparo (grados) ")
		app.labelv2.place(x=80,y=60)
		app.labelv3=ttk.Label(app,text="Ancho de pulso (grados)")
		app.labelv3.place(x=80,y=90)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.entry2= ttk.Entry(app,width=7, textvariable=dato2)
		app.entry2.place(x=30,y=60)
		app.entry3= ttk.Entry(app,width=7, textvariable=dato3)
		app.entry3.place(x=30,y=90)
		app.caso=3
	if numerovalor==4:
		print("Puente Trifasico Completo Controlado")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)			
		app.labelv1=ttk.Label(app,text="Voltaje ")
		app.labelv1.place(x=80,y=30)
		app.labelv2=ttk.Label(app,text="Angulo de disparo (grados) ")
		app.labelv2.place(x=80,y=60)
		app.labelv3=ttk.Label(app,text="Ancho de pulso (grados)")
		app.labelv3.place(x=80,y=90)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.entry2= ttk.Entry(app,width=7, textvariable=dato2)
		app.entry2.place(x=30,y=60)
		app.entry3= ttk.Entry(app,width=7, textvariable=dato3)
		app.entry3.place(x=30,y=90)
		app.caso=4
	if numerovalor==5:
		print("Puente Trifasico Incompleto Controlado")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)			
		app.labelv1=ttk.Label(app,text="Voltaje ")
		app.labelv1.place(x=80,y=30)
		app.labelv2=ttk.Label(app,text="Angulo de disparo (grados) ")
		app.labelv2.place(x=80,y=60)
		app.labelv3=ttk.Label(app,text="Ancho de pulso (grados)")
		app.labelv3.place(x=80,y=90)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.entry2= ttk.Entry(app,width=7, textvariable=dato2)
		app.entry2.place(x=30,y=60)
		app.entry3= ttk.Entry(app,width=7, textvariable=dato3)
		app.entry3.place(x=30,y=90)
		app.caso=5
	if numerovalor==6:
		print("Puente Trifasico Completo con Diodo de Descarga")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)			
		app.labelv1=ttk.Label(app,text="Voltaje ")
		app.labelv1.place(x=80,y=30)
		app.labelv2=ttk.Label(app,text="Angulo de disparo (grados) ")
		app.labelv2.place(x=80,y=60)
		app.labelv3=ttk.Label(app,text="Ancho de pulso (grados)")
		app.labelv3.place(x=80,y=90)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.entry2= ttk.Entry(app,width=7, textvariable=dato2)
		app.entry2.place(x=30,y=60)
		app.entry3= ttk.Entry(app,width=7, textvariable=dato3)
		app.entry3.place(x=30,y=90)
		app.caso=6
	if numerovalor==7:
		print("Chopper 4 Cuadrantes")
		if app.caso>0:	
			app.entry1.place_forget()
			app.labelv1.place_forget()
			app.botonace.place_forget()
			if app.caso>1: 
				app.labelv2.place_forget()
				app.labelv3.place_forget()
				app.entry2.place_forget()
				app.entry3.place_forget()
		app.botonace=ttk.Button(app,text="Aplicar",command=configalimentacion)
		app.botonace.place(x=30,y=120)			
		app.labelv1=ttk.Label(app,text="Voltaje")
		app.labelv1.place(x=80,y=30)
		app.labelv2=ttk.Label(app,text="Ciclo Util (0-1)")
		app.labelv2.place(x=80,y=60)
		app.labelv3=ttk.Label(app,text="Frecuencia(Hz)")
		app.labelv3.place(x=80,y=90)
		app.entry1= ttk.Entry(app,width=7, textvariable=dato1)
		app.entry1.place(x=30,y=30)
		app.entry2= ttk.Entry(app,width=7, textvariable=dato2)
		app.entry2.place(x=30,y=60)
		app.entry3= ttk.Entry(app,width=7, textvariable=dato3)
		app.entry3.place(x=30,y=90)
		app.caso=7
def selection_changed2(self):
	global boxsel2,ventconfig,labelm1,labelm2,labelm3,labelm4,labelm5,labelm6,labelm7,labelm8,labelm9,prueba
	if boxsel2.current()==0:
		prueba=1
		labelm1.place_forget()
		labelm2.place_forget()
		labelm3.place_forget()
		labelm4.place_forget()
		labelm5.place_forget()
		labelm6.place_forget()
		labelm7.place_forget()
		labelm8.place_forget()
		labelm9.place_forget()
		ventconfig.entrym4.place_forget()
		ventconfig.entrym5.place_forget()
		ventconfig.entrym6.place_forget()
		ventconfig.entrym7.place_forget()
		ventconfig.entrym8.place_forget()
		ventconfig.entrym9.place_forget()

		labelm1=ttk.Label(ventconfig,text="R(ohm)")
		labelm2=ttk.Label(ventconfig,text="L(mH)")
		labelm3=ttk.Label(ventconfig,text="E")
		labelm1.place(x=140,y=30)
		labelm2.place(x=140,y=60)
		labelm3.place(x=140,y=90)


	if boxsel2.current()>0:
		labelm1.place_forget()
		labelm2.place_forget()
		labelm3.place_forget()
		prueba=0
		labelm1=ttk.Label(ventconfig,text="Voltaje Nom")
		labelm2=ttk.Label(ventconfig,text="R.P.M.")
		labelm3=ttk.Label(ventconfig,text="HpNom(HP)")
		labelm4=ttk.Label(ventconfig,text="Potencia Nom. salida(kW)")
		labelm5=ttk.Label(ventconfig,text="IaNom(A)")
		labelm6=ttk.Label(ventconfig,text="Ra(ohm)")
		labelm7=ttk.Label(ventconfig,text="La(mH)")
		labelm8=ttk.Label(ventconfig,text="Inercia(Kg-m^2)")
		labelm9=ttk.Label(ventconfig,text="Torque de carga(N-m)")

		ventconfig.entrym4=ttk.Entry(ventconfig,textvariable=dato4m)
		ventconfig.entrym5=ttk.Entry(ventconfig,textvariable=dato5m)
		ventconfig.entrym6=ttk.Entry(ventconfig,textvariable=dato6m)
		ventconfig.entrym7=ttk.Entry(ventconfig,textvariable=dato7m)
		ventconfig.entrym8=ttk.Entry(ventconfig,textvariable=dato8m)
		ventconfig.entrym9=ttk.Entry(ventconfig,textvariable=dato9m)
		labelm1.place(x=140,y=30)
		labelm2.place(x=140,y=60)
		labelm3.place(x=140,y=90)
		labelm4.place(x=140,y=120)
		labelm5.place(x=140,y=150)
		labelm6.place(x=140,y=180)
		labelm7.place(x=140,y=210)
		labelm8.place(x=140,y=240)
		labelm9.place(x=140,y=270)
		ventconfig.entrym4.place(x=10,y=120)
		ventconfig.entrym5.place(x=10,y=150)
		ventconfig.entrym6.place(x=10,y=180)
		ventconfig.entrym7.place(x=10,y=210)
		ventconfig.entrym8.place(x=10,y=240)
		ventconfig.entrym9.place(x=10,y=270)

		mensaje=boxsel2.get()
		copia=[]
		for i in range(0,8):
			copia1=mensaje.find(":")
			copia2=mensaje.find(" ")
			copia.append(mensaje[copia1+1:copia2])
			mensaje=mensaje[copia2+1:len(mensaje)]

		ventconfig.entrym1.insert(0, copia[0])
		ventconfig.entrym2.insert(0, copia[1])
		ventconfig.entrym3.insert(0, copia[2])
		ventconfig.entrym4.insert(0, copia[3])
		ventconfig.entrym5.insert(0, copia[4])
		ventconfig.entrym6.insert(0, copia[5])
		ventconfig.entrym7.insert(0, copia[6])
		ventconfig.entrym8.insert(0, copia[7])	


root = Tk()
root.title("Simulador")
root.config(bg="#05000B")
imagen1=PhotoImage(file="p1.png")
#fondo=Label(ventana,image=imagen1)

imagen2=PhotoImage(file="p2.png")
#fondo=Label(ventana,image=imagen2)

imagen3=PhotoImage(file="p3.png")
#fondo=Label(ventana,image=imagen3)

imagen4=PhotoImage(file="p4.png")
#fondo=Label(ventana,image=imagen4)

imagen5=PhotoImage(file="p5.png")
#fondo=Label(ventana,image=imagen5)
imagen6=PhotoImage(file="p6.png")

imagen7=PhotoImage(file="p7.png")
logo=PhotoImage(file="p10.png")

RPM=1600
hp=10
Pnomsal=12000
Tm=10
V1=230*math.sqrt(2)
alpha=60
anchdisparo=50
adisparo=np.zeros(2)
cq=np.zeros(6)
pcq=np.zeros(6)
kan=np.zeros(7)
pp1=0
pp2=0
pp3=0
pp4=0
pp5=0
w=2*pi*60
lam=0
prueba=0
dato1=StringVar()
dato2=StringVar()
dato3=StringVar()
dato1m=StringVar()
dato2m=StringVar()
dato3m=StringVar()
dato4m=StringVar()
dato5m=StringVar()
dato6m=StringVar()
dato7m=StringVar()
dato8m=StringVar()
dato9m=StringVar()
datoslistos1=DoubleVar()
datoslistos2=DoubleVar()
dato1mm=DoubleVar()
datoslistos3=DoubleVar()
dato2mm=DoubleVar()
dato3mm=DoubleVar()
dato4mm=DoubleVar()
dato5mm=DoubleVar()
dato6mm=DoubleVar()
dato7mm=DoubleVar()
dato8mm=DoubleVar()
dato9mm=DoubleVar()
dato=np.zeros(9)
cc1=StringVar()
cc2=StringVar()
cc3=StringVar()
cc4=StringVar()
cc5=StringVar()
tiempoasimular=StringVar()
botonstate=np.zeros(4)       
auxili=0
repetir=0
borrarboton=0
perturbacion=0
cc11=0
cc12=0
cc13=0
cc14=0
cc15=0
paso=1
R=0
L=5
V1=0
lam=0
lam1=0
axx=0
K=0
J=1
s1 = ttk.Style()
s1.configure('new.TFrame', background='#6904A6')
mainframe = ttk.Frame(root, padding="3 3 12 12",style='new.TFrame')
mainframe.grid(column=0, row=0,sticky=(N,W, E))

s2 = ttk.Style()
s2.configure('new1.TFrame', background='#FFFFFF')
secondframe=ttk.Frame(root,style='new1.TFrame')
secondframe.grid(column=0,row=1,sticky=(N,W,E,S))

root.columnconfigure(0, weight=1)

fuenteusada=font.Font(family='@Microsoft YaHei',size=12)
font.families()


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.resizable(True,True)
root.geometry("800x600")


def ventaliment():
	global app
	global main_window
	main_window = tk.Tk()
	app = Application(main_window)
	global boxsel
	boxsel = ttk.Combobox(app,width=100,state="readonly")
	boxsel.place(x=0, y=0)
	boxsel["values"] = ["Seleccione Accionamiento","Fuente DC Directa","Puente 1F Completo Controlado", "Puente 1F Incompleto Controlado", "Puente 3F Completo Controlado", "Puente 3F Incompleto Controlado","Puente 3F Completo Controlado con Diodo Descarga","Chopper 4 Cuadrantes"]
	boxsel.current(0)
	boxsel.bind("<<ComboboxSelected>>", selection_changed)
	app.caso=0
	app.place(width=400, height=200)
	app.entry1=ttk.Entry(app,textvariable=dato1)
	app.entry2=ttk.Entry(app,textvariable=dato2)
	app.entry3=ttk.Entry(app,textvariable=dato3)

def configperturb():
	global numerovalor,cc1,cc11,cc2,cc3,cc4,cc5
	global ccperturb
	global ccperturb2
	ccperturb= tk.Tk()
	ccperturb2 =Application(ccperturb)
	ccperturb.title("Cambios")
	ccperturb.geometry("400x300")
	ccperturb.ccetq1=ttk.Label(ccperturb, text="Aplicar Cambios en")
	ccperturb.ccetq2=ttk.Label(ccperturb, text="T (segundos)")
	ccperturb.ccentry1=ttk.Entry(ccperturb, textvariable=cc1)
	ccperturb.ccentry1.place(x=10,y=40)
	ccperturb.ccetq1.place(x= 10, y=10)
	ccperturb.ccetq2.place(x= 145, y=40)

	if numerovalor==1:
		ccperturb.ccetq3=ttk.Label(ccperturb, text="Voltaje DC")
		ccperturb.ccetq3.place(x=145,y=70)
		ccperturb.ccentry2=ttk.Entry(ccperturb, textvariable=cc2)
		ccperturb.ccentry2.place(x=10,y=70)
		#ccperturb.ccetq3=ttk.Entry(ccperturb, textvariable=datpert1)
	
	if numerovalor>1:
		if numerovalor<7:
			print(numerovalor)
			ccperturb.ccetq3=ttk.Label(ccperturb, text="Voltaje")
			ccperturb.ccetq3.place(x=145,y=70)
			ccperturb.ccetq4=ttk.Label(ccperturb, text="Angulo alfa(grados)")
			ccperturb.ccetq4.place(x=145,y=100)
			ccperturb.ccetq5=ttk.Label(ccperturb, text="Ancho pulso(grados)")
			ccperturb.ccetq5.place(x=145,y=130)
			ccperturb.ccentry2=ttk.Entry(ccperturb, textvariable=cc2)
			ccperturb.ccentry2.place(x=10,y=70)
			ccperturb.ccentry3=ttk.Entry(ccperturb, textvariable=cc3)
			ccperturb.ccentry3.place(x=10,y=100)
			ccperturb.ccentry4=ttk.Entry(ccperturb, textvariable=cc4)
			ccperturb.ccentry4.place(x=10,y=130)

	if numerovalor==7:
		ccperturb.ccetq3=ttk.Label(ccperturb, text="Voltaje")
		ccperturb.ccetq3.place(x=145,y=70)
		ccperturb.ccetq4=ttk.Label(ccperturb, text="Ciclo Util (0-1)")
		ccperturb.ccetq4.place(x=145,y=100)
		ccperturb.ccetq5=ttk.Label(ccperturb, text="Frecuencia (Hz)")
		ccperturb.ccetq5.place(x=145,y=130)
		ccperturb.ccentry2=ttk.Entry(ccperturb, textvariable=cc2)
		ccperturb.ccentry2.place(x=10,y=70)
		ccperturb.ccentry3=ttk.Entry(ccperturb, textvariable=cc3)
		ccperturb.ccentry3.place(x=10,y=100)
		ccperturb.ccentry4=ttk.Entry(ccperturb, textvariable=cc4)
		ccperturb.ccentry4.place(x=10,y=130)

	ccperturb.ccentry5=ttk.Entry(ccperturb, textvariable=cc5)
	ccperturb.ccentry5.place(x=10,y=160)
	ccperturb.ccetq6=ttk.Label(ccperturb, text="Proporción del Flujo con respecto")
	ccperturb.ccetq7=ttk.Label(ccperturb, text="al valor Nominal (1 por Defecto)")
	ccperturb.ccetq6.place(x=145,y=160)
	ccperturb.ccetq7.place(x=145,y=180)

	ccperturb.ccboton=ttk.Button(ccperturb,text="Aceptar",command=cccpertb)
	ccperturb.ccboton.place(x=10,y=190)



def cccpertb():
	global ccperturb,ventconfig,app,auxili,app,fondo,pp1,pp2,pp3,pp4,pp5,perturbacion,pertetq11,pertetq12,pertetq13,pertetq14
	global pertetq15,pertetq16,pertetq1,pertetq2,pertetq3,pertetq4,pertetq5
	if auxili==1:
		pertetq11.grid_forget()
		pertetq12.grid_forget()
		pertetq13.grid_forget()
		pertetq1.grid_forget()
		pertetq2.grid_forget()
		pertetq5.grid_forget()
		pertetq16.grid_forget()
	if auxili==2:
		pertetq11.grid_forget()
		pertetq12.grid_forget()
		pertetq13.grid_forget()
		pertetq14.grid_forget()
		pertetq15.grid_forget()
		pertetq16.grid_forget()
		pertetq1.grid_forget()
		pertetq2.grid_forget()
		pertetq3.grid_forget()
		pertetq4.grid_forget()
		pertetq5.grid_forget()

	if app.caso==1:
		try:
			cc11=float(ccperturb.ccentry1.get())
			cc12=float(ccperturb.ccentry2.get())
			cc15=float(ccperturb.ccentry5.get())
			pp1=float(ccperturb.ccentry1.get())
			pp2=float(ccperturb.ccentry2.get())
			pp5=float(ccperturb.ccentry5.get())
		except:
			messagebox.showinfo(message="No se deben dejar campos vacíos y sólo se deben usar números", title="Valor Erróneo")
			return 0
		pertetq11=ttk.Label(secondframe, text="Cambios:",background="white",font=fuenteusada)
		pertetq11.grid(row=1,column=5,sticky=NSEW)
		pertetq12=ttk.Label(secondframe, text="En t=",background="white",font=fuenteusada)
		pertetq12.grid(row=2,column=5,sticky=NSEW)
		pertetq13=ttk.Label(secondframe, text="Voltaje",background="white",font=fuenteusada)
		pertetq13.grid(row=3,column=5,sticky=NSEW)
		pertetq1=ttk.Label(secondframe, text=str(cc11),background="white",font=fuenteusada)
		pertetq1.grid(row=2,column=6,sticky=NSEW)
		pertetq2=ttk.Label(secondframe, text=str(cc12),background="white",font=fuenteusada)
		pertetq2.grid(row=3,column=6,sticky=NSEW)
		pertetq16=ttk.Label(secondframe, text="Flujo de Campo:",background="white",font=fuenteusada)
		pertetq16.grid(row=6,column=5,sticky=NSEW)
		pertetq5=ttk.Label(secondframe, text=str(cc15),background="white",font=fuenteusada)
		pertetq5.grid(row=6,column=6,sticky=NSEW)
	
		auxili=1
	if app.caso>1:
		if app.caso<7:
			try:
				cc11=float(ccperturb.ccentry1.get())
				cc12=float(ccperturb.ccentry2.get())
				cc13=float(ccperturb.ccentry3.get())
				cc14=float(ccperturb.ccentry4.get())
				cc15=float(ccperturb.ccentry5.get())
				pp1=float(ccperturb.ccentry1.get())
				pp2=float(ccperturb.ccentry2.get())
				pp3=float(ccperturb.ccentry3.get())
				pp4=float(ccperturb.ccentry4.get())
				pp5=float(ccperturb.ccentry5.get())
			except:
				messagebox.showinfo(message="No se deben dejar campos vacíos y sólo se deben usar números", title="Valor Erróneo")
				return 0
			pertetq11=ttk.Label(secondframe, text="Cambios:",background="white",font=fuenteusada)
			pertetq11.grid(row=1,column=5,sticky=NSEW)
			pertetq12=ttk.Label(secondframe, text="En t=",background="white",font=fuenteusada)
			pertetq12.grid(row=2,column=5,sticky=NSEW)
			pertetq13=ttk.Label(secondframe, text="Voltaje",background="white",font=fuenteusada)
			pertetq13.grid(row=3,column=5,sticky=NSEW)
			pertetq1=ttk.Label(secondframe, text=str(cc11),background="white",font=fuenteusada)
			pertetq1.grid(row=2,column=6,sticky=NSEW)
			pertetq2=ttk.Label(secondframe, text=str(cc12),background="white",font=fuenteusada)
			pertetq2.grid(row=3,column=6,sticky=NSEW)
			pertetq3=ttk.Label(secondframe, text=str(cc13),background="white",font=fuenteusada)
			pertetq3.grid(row=4,column=6,sticky=NSEW)
			pertetq4=ttk.Label(secondframe, text=str(cc14),background="white",font=fuenteusada)
			pertetq4.grid(row=5,column=6,sticky=NSEW)
			
			pertetq5=ttk.Label(secondframe, text=str(cc15),background="white",font=fuenteusada)
			pertetq5.grid(row=6,column=6,sticky=NSEW)

			pertetq14=ttk.Label(secondframe, text="Angulo alfa",background="white",font=fuenteusada)
			pertetq14.grid(row=4,column=5,sticky=NSEW)
			pertetq15=ttk.Label(secondframe, text="Ancho de pulso",background="white",font=fuenteusada)
			pertetq15.grid(row=5,column=5,sticky=NSEW)
			pertetq16=ttk.Label(secondframe, text="Flujo de Campo:",background="white",font=fuenteusada)
			pertetq16.grid(row=6,column=5,sticky=NSEW)
			auxili=2
	if app.caso==7:
		try:
			cc11=float(ccperturb.ccentry1.get())
			cc12=float(ccperturb.ccentry2.get())
			cc13=float(ccperturb.ccentry3.get())
			cc14=float(ccperturb.ccentry4.get())
			cc15=float(ccperturb.ccentry5.get())
			pp1=float(ccperturb.ccentry1.get())
			pp2=float(ccperturb.ccentry2.get())
			pp3=float(ccperturb.ccentry3.get())
			pp4=float(ccperturb.ccentry4.get())
			pp5=float(ccperturb.ccentry5.get())
		except:
			messagebox.showinfo(message="No se deben dejar campos vacíos y sólo se deben usar números", title="Valor Erróneo")
			return 0
		pertetq11=ttk.Label(secondframe, text="Cambios:",background="white",font=fuenteusada)
		pertetq11.grid(row=1,column=5,sticky=NSEW)
		pertetq12=ttk.Label(secondframe, text="En t=",background="white",font=fuenteusada)
		pertetq12.grid(row=2,column=5,sticky=NSEW)
		pertetq13=ttk.Label(secondframe, text="Voltaje",background="white",font=fuenteusada)
		pertetq13.grid(row=3,column=5,sticky=NSEW)
		pertetq1=ttk.Label(secondframe, text=str(cc11),background="white",font=fuenteusada)
		pertetq1.grid(row=2,column=6,sticky=NSEW)
		pertetq2=ttk.Label(secondframe, text=str(cc12),background="white",font=fuenteusada)
		pertetq2.grid(row=3,column=6,sticky=NSEW)
		pertetq3=ttk.Label(secondframe, text=str(cc13),background="white",font=fuenteusada)
		pertetq3.grid(row=4,column=6,sticky=NSEW)
		pertetq4=ttk.Label(secondframe, text=str(cc14),background="white",font=fuenteusada)
		pertetq4.grid(row=5,column=6,sticky=NSEW)
		pertetq14=ttk.Label(secondframe, text="Ciclo Util",background="white",font=fuenteusada)
		pertetq14.grid(row=4,column=5,sticky=NSEW)
		pertetq15=ttk.Label(secondframe, text="Frecuencia",background="white",font=fuenteusada)
		pertetq15.grid(row=5,column=5,sticky=NSEW)
		pertetq5=ttk.Label(secondframe, text=str(cc15),background="white",font=fuenteusada)
		pertetq5.grid(row=6,column=6,sticky=NSEW)
		pertetq16=ttk.Label(secondframe, text="Flujo de Campo:",background="white",font=fuenteusada)
		pertetq16.grid(row=6,column=5,sticky=NSEW)
		auxili=2
	perturbacion=1


def configalimentacion():
	global datoslistos1,datoslistos2,datoslistos3,app,axx,resultado1,resultado2,resultado3,etq1,etq2,etq3,etqfuente,fondo

	if axx==1:
		resultado1.grid_forget()
		etq1.grid_forget()
		etqfuente.grid_forget()
	if axx==2:
		etqfuente.grid_forget()
		etq1.grid_forget()
		etq2.grid_forget()
		etq3.grid_forget()
		resultado1.grid_forget()
		resultado2.grid_forget()
		resultado3.grid_forget()
	if app.caso==1:
		try:
			datoslistos1=float(app.entry1.get())
		except:
			messagebox.showinfo(message="No se deben dejar campos vacíos y sólo se deben usar números", title="Valor Erróneo")
			return 0
		resultado1=ttk.Label(secondframe, text=str(datoslistos1),background="white",font=fuenteusada)
		resultado1.grid(row=2,column=2,sticky=(W,N))
		etq1=ttk.Label(secondframe,text="Voltaje DC:",font=fuenteusada,background="white")
		etq1.grid(row=2,column=1,sticky=(W))
		axx=1
		fondo=Label(secondframe,image=imagen7)
		fondo.grid(row=9,column=1,sticky=NSEW,rowspan=1)
	if app.caso>1:
		if app.caso<7:
			try:
				datoslistos1=float(app.entry1.get())
				datoslistos2=float(app.entry2.get())
				datoslistos3=float(app.entry3.get())	
			except:
				messagebox.showinfo(message="No se deben dejar campos vacíos y sólo se deben usar números", title="Valor Erróneo")
				return 0
			resultado1=ttk.Label(secondframe, text=str(datoslistos1),background="white",font=fuenteusada)
			resultado1.grid(row=2,column=2,sticky=(W,N))
			resultado2=ttk.Label(secondframe, text=str(datoslistos2),background="white",font=fuenteusada)
			resultado2.grid(row=3,column=2,sticky=(W,N))
			resultado3=ttk.Label(secondframe, text=str(datoslistos3),background="white",font=fuenteusada)
			resultado3.grid(row=4,column=2,sticky=(W,N))
			etq1=ttk.Label(secondframe,text="Voltaje :",font=fuenteusada,background="white")
			etq1.grid(row=2,column=1,sticky=(W))
			etq2=ttk.Label(secondframe,text="Angulo de disparo:",font=fuenteusada,background="white")
			etq2.grid(row=3,column=1,sticky=(W))
			etq3=ttk.Label(secondframe,text="Ancho de pulso (grados):",background="white",font=fuenteusada)
			etq3.grid(row=4,column=1,sticky=(W))

			if app.caso==2:
				fondo=Label(secondframe,image=imagen1)
			if app.caso==3:
				fondo=Label(secondframe,image=imagen2)
			if app.caso==4:
				fondo=Label(secondframe,image=imagen4)
			if app.caso==5:
				fondo=Label(secondframe,image=imagen5)
			if app.caso==6:
				fondo=Label(secondframe,image=imagen3)
	if app.caso>1:
		if app.caso<7:
			if datoslistos2>180:
				messagebox.showinfo(message="El ángulo de disparo no debe ser mayor a 180", title="Valor Erróneo")

			fondo.grid(row=9,column=1,sticky=NSEW,rowspan=1)

			axx=2
	if app.caso==7:
		try:
			datoslistos1=float(app.entry1.get())
			datoslistos2=float(app.entry2.get())
			datoslistos3=float(app.entry3.get())	
		except:
			messagebox.showinfo(message="No se deben dejar campos vacíos y sólo se deben usar números", title="Valor Erróneo")
			return 0
		resultado1=ttk.Label(secondframe, text=str(datoslistos1),background="white",font=fuenteusada)
		resultado1.grid(row=2,column=2,sticky=NSEW)
		resultado2=ttk.Label(secondframe, text=str(datoslistos2),background="white",font=fuenteusada)
		resultado2.grid(row=3,column=2,sticky=NSEW)
		resultado3=ttk.Label(secondframe, text=str(datoslistos3),background="white",font=fuenteusada)
		resultado3.grid(row=4,column=2,sticky=NSEW)
		etq1=ttk.Label(secondframe,text="Voltaje: ",background="white",font=fuenteusada)
		etq1.grid(row=2,column=1,sticky=NSEW)
		etq2=ttk.Label(secondframe,text="Ciclo Util(0-1):",background="white",font=fuenteusada)
		etq2.grid(row=3,column=1,sticky=NSEW)
		etq3=ttk.Label(secondframe,text="Frecuencia(Hz):",background="white",font=fuenteusada)
		etq3.grid(row=4,column=1,sticky=NSEW)
		axx=2		
		fondo=Label(secondframe,image=imagen6)
		fondo.grid(row=9,column=1,sticky=NSEW,rowspan=1)
	if app.caso==7:
		if datoslistos2>1:
			messagebox.showinfo(message="El ciclo util debe estar comprendido entre (0-1)", title="Valor Erróneo")
	etqfuente=ttk.Label(secondframe,text='Datos Accionamiento',background="white",font=fuenteusada)
	etqfuente.grid(row=1,column=1,sticky=(W))

	pass

def configmotor():
	global ventconfig,dato1m,dato2m,dato3m,dato4m,dato5m,dato6m,dato7m,dato8m,dato9m
	global ventconfig2,labelm1,labelm2,labelm3,labelm4,labelm5,labelm6,labelm7,labelm8,labelm9
	ventconfig= tk.Tk()
	ventconfig2 =Application(ventconfig)
	ventconfig.title("Configurar Motor")
	ventconfig.geometry("430x330")
	global archivo
	global boxsel2
	boxsel2 = ttk.Combobox(ventconfig,width=120,state="readonly")
	boxsel2.place(x=0, y=0)
	valmotores=archivo.readline()
	boxsel2["values"] = valmotores2
	boxsel2.current(1)
	boxsel2.bind("<<ComboboxSelected>>", selection_changed2)
	bcm=ttk.Button(ventconfig,text="Aceptar",command=setmotor)
	labelm1=ttk.Label(ventconfig,text="Voltaje Nom")
	labelm2=ttk.Label(ventconfig,text="R.P.M.")
	labelm3=ttk.Label(ventconfig,text="HpNom(HP)")
	labelm4=ttk.Label(ventconfig,text="Potencia Nom. salida(kW)")
	labelm5=ttk.Label(ventconfig,text="IaNom(A)")
	labelm6=ttk.Label(ventconfig,text="Ra(ohm)")
	labelm7=ttk.Label(ventconfig,text="La(mH)")
	labelm8=ttk.Label(ventconfig,text="Inercia(Kg-m^2):")
	labelm9=ttk.Label(ventconfig,text="Torque de carga(N-m)")
	ventconfig.entrym1=ttk.Entry(ventconfig,textvariable=dato1m)
	ventconfig.entrym2=ttk.Entry(ventconfig,textvariable=dato2m)
	ventconfig.entrym3=ttk.Entry(ventconfig,textvariable=dato3m)
	ventconfig.entrym4=ttk.Entry(ventconfig,textvariable=dato4m)
	ventconfig.entrym5=ttk.Entry(ventconfig,textvariable=dato5m)
	ventconfig.entrym6=ttk.Entry(ventconfig,textvariable=dato6m)
	ventconfig.entrym7=ttk.Entry(ventconfig,textvariable=dato7m)
	ventconfig.entrym8=ttk.Entry(ventconfig,textvariable=dato8m)
	ventconfig.entrym9=ttk.Entry(ventconfig,textvariable=dato9m)
	labelm1.place(x=140,y=30)
	labelm2.place(x=140,y=60)
	labelm3.place(x=140,y=90)
	labelm4.place(x=140,y=120)
	labelm5.place(x=140,y=150)
	labelm6.place(x=140,y=180)
	labelm7.place(x=140,y=210)
	labelm8.place(x=140,y=240)
	labelm9.place(x=140,y=270)
	bcm.place(x=140,y=300)
	ventconfig.entrym1.place(x=10,y=30)
	ventconfig.entrym2.place(x=10,y=60)
	ventconfig.entrym3.place(x=10,y=90)
	ventconfig.entrym4.place(x=10,y=120)
	ventconfig.entrym5.place(x=10,y=150)
	ventconfig.entrym6.place(x=10,y=180)
	ventconfig.entrym7.place(x=10,y=210)
	ventconfig.entrym8.place(x=10,y=240)
	ventconfig.entrym9.place(x=10,y=270)
def setmotor():
	global dato1m,dato2m,dato3m,dato4m,dato5m,dato6m,ventconfig,dato7m,dato8m,dato9m,boxsel2,repetir
	global dato1mmm,dato2mmm,dato3mmm,dato4mmm,dato5mmm,dato6mmm,dato7mmm,dato8mmm,dato9mmm
	global etqdato1mmm,etqdato2mmm,etqdato3mmm,etqdato4mmm,etqdato5mmm,etqdato6mmm,etqdato7mmm,etqdato8mmm,etqdato9mmm
	if repetir==1:
		dato1mmm.grid_forget()
		dato2mmm.grid_forget()
		dato3mmm.grid_forget()
		etqdato1mmm.grid_forget()
		etqdato2mmm.grid_forget()
		etqdato3mmm.grid_forget()

	if repetir==2:
		dato1mmm.grid_forget()
		dato2mmm.grid_forget()
		dato3mmm.grid_forget()
		dato4mmm.grid_forget()
		dato5mmm.grid_forget()
		dato6mmm.grid_forget()
		dato7mmm.grid_forget()
		dato8mmm.grid_forget()
		dato9mmm.grid_forget()
		etqdato1mmm.grid_forget()
		etqdato2mmm.grid_forget()
		etqdato3mmm.grid_forget()
		etqdato4mmm.grid_forget()
		etqdato5mmm.grid_forget()
		etqdato6mmm.grid_forget()
		etqdato7mmm.grid_forget()
		etqdato8mmm.grid_forget()
		etqdato9mmm.grid_forget()


	if boxsel2.current()==0:
		try:
			dato1mm=float(ventconfig.entrym1.get())
			dato2mm=float(ventconfig.entrym2.get())
			dato3mm=float(ventconfig.entrym3.get())

			dato[0]=float(ventconfig.entrym1.get())
			dato[1]=float(ventconfig.entrym2.get())
			dato[2]=float(ventconfig.entrym3.get())
			repetir=1
		except:
			messagebox.showinfo(message="No se deben dejar campos vacíos y sólo se deben usar números", title="Valor Erróneo")
			return 0

	if boxsel2.current()>0:
		try:		
			dato1mm=float(ventconfig.entrym1.get())
			dato2mm=float(ventconfig.entrym2.get())
			dato3mm=float(ventconfig.entrym3.get())
			dato4mm=float(ventconfig.entrym4.get())
			dato5mm=float(ventconfig.entrym5.get())
			dato6mm=float(ventconfig.entrym6.get())
			dato7mm=float(ventconfig.entrym7.get())
			dato8mm=float(ventconfig.entrym8.get())
			dato9mm=float(ventconfig.entrym9.get())

			dato[0]=float(ventconfig.entrym1.get())
			dato[1]=float(ventconfig.entrym2.get())
			dato[2]=float(ventconfig.entrym3.get())
			dato[3]=float(ventconfig.entrym4.get())
			dato[4]=float(ventconfig.entrym5.get())
			dato[5]=float(ventconfig.entrym6.get())
			dato[6]=float(ventconfig.entrym7.get())
			dato[7]=float(ventconfig.entrym8.get())
			dato[8]=float(ventconfig.entrym9.get())
		except:
			messagebox.showinfo(message="No se deben dejar campos vacíos y sólo se deben usar números", title="Valor Erróneo")
			return 0




		repetir=2

	if boxsel2.current()==0:

		dato1mmm=ttk.Label(secondframe, text=str(dato1mm),background="#FFFFFF",font=fuenteusada)
		dato1mmm.grid(row=1,column=4,sticky=NSEW)
		dato2mmm=ttk.Label(secondframe, text=str(dato2mm),background="#FFFFFF",font=fuenteusada)
		dato2mmm.grid(row=2,column=4,sticky=NSEW)
		dato3mmm=ttk.Label(secondframe, text=str(dato3mm),background="#FFFFFF",font=fuenteusada)
		dato3mmm.grid(row=3,column=4,sticky=NSEW)
		etqdato1mmm=ttk.Label(secondframe, text="Resistencia:",background="#FFFFFF",font=fuenteusada)
		etqdato1mmm.grid(row=1,column=3,sticky=NSEW)
		etqdato2mmm=ttk.Label(secondframe, text="Inductancia(mH):",background="#FFFFFF",font=fuenteusada)
		etqdato2mmm.grid(row=2,column=3,sticky=NSEW)
		etqdato3mmm=ttk.Label(secondframe, text="E:",background="#FFFFFF",font=fuenteusada)
		etqdato3mmm.grid(row=3,column=3,sticky=NSEW)

	if boxsel2.current()>0:
		dato1mmm=ttk.Label(secondframe, text=str(dato1mm),background="#FFFFFF",font=fuenteusada)
		dato1mmm.grid(row=1,column=4,sticky=NSEW)
		dato2mmm=ttk.Label(secondframe, text=str(dato2mm),background="#FFFFFF",font=fuenteusada)
		dato2mmm.grid(row=2,column=4,sticky=NSEW)
		dato3mmm=ttk.Label(secondframe, text=str(dato3mm),background="#FFFFFF",font=fuenteusada)
		dato3mmm.grid(row=3,column=4,sticky=NSEW)
		dato4mmm=ttk.Label(secondframe, text=str(dato4mm),background="#FFFFFF",font=fuenteusada)
		dato4mmm.grid(row=4,column=4,sticky=NSEW)
		dato5mmm=ttk.Label(secondframe, text=str(dato5mm),background="#FFFFFF",font=fuenteusada)
		dato5mmm.grid(row=5,column=4,sticky=NSEW)
		dato6mmm=ttk.Label(secondframe, text=str(dato6mm),background="#FFFFFF",font=fuenteusada)
		dato6mmm.grid(row=6,column=4,sticky=NSEW)
		dato7mmm=ttk.Label(secondframe, text=str(dato7mm),background="#FFFFFF",font=fuenteusada)
		dato7mmm.grid(row=7,column=4,sticky=NSEW)
		dato8mmm=ttk.Label(secondframe, text=str(dato8mm),background="#FFFFFF",font=fuenteusada)
		dato8mmm.grid(row=8,column=4,sticky=NSEW)
		dato9mmm=ttk.Label(secondframe, text=str(dato9mm),background="#FFFFFF",font=fuenteusada)
		dato9mmm.grid(row=9,column=4,sticky=NSEW)

		etqdato1mmm=ttk.Label(secondframe, text="Voltaje Nom:",background="#FFFFFF",font=fuenteusada)
		etqdato1mmm.grid(row=1,column=3,sticky=NSEW)
		etqdato2mmm=ttk.Label(secondframe, text="R.P.M:",background="#FFFFFF",font=fuenteusada)
		etqdato2mmm.grid(row=2,column=3,sticky=NSEW)
		etqdato3mmm=ttk.Label(secondframe, text="HPNom(HP):",background="#FFFFFF",font=fuenteusada)
		etqdato3mmm.grid(row=3,column=3,sticky=NSEW)
		etqdato4mmm=ttk.Label(secondframe, text="Potencia salida(kW):",background="#FFFFFF",font=fuenteusada)
		etqdato4mmm.grid(row=4,column=3,sticky=NSEW)
		etqdato5mmm=ttk.Label(secondframe, text="IaNom(A):",background="#FFFFFF",font=fuenteusada)
		etqdato5mmm.grid(row=5,column=3,sticky=NSEW)
		etqdato6mmm=ttk.Label(secondframe, text="Ra(ohm):",background="#FFFFFF",font=fuenteusada)
		etqdato6mmm.grid(row=6,column=3,sticky=NSEW)
		etqdato7mmm=ttk.Label(secondframe, text="La(mH):",background="#FFFFFF",font=fuenteusada)
		etqdato7mmm.grid(row=7,column=3,sticky=NSEW)
		etqdato8mmm=ttk.Label(secondframe, text="Inercia(Kg-m^2):",background="#FFFFFF",font=fuenteusada)
		etqdato8mmm.grid(row=8,column=3,sticky=NSEW)
		etqdato9mmm=ttk.Label(secondframe, text="Torque de Carga(N-m)",background="#FFFFFF",font=fuenteusada)
		etqdato9mmm.grid(row=9,column=3,sticky=NSEW)

#	etqextra=ttk.Label(secondframe,text=" ",background="#CCCCCC")
#	etqextra.grid(row=9,column=3,sticky=NSEW)
#	etqextra2=ttk.Label(secondframe,text=" ",background="#CCCCCC")
#	etqextra2.grid(row=9,column=4,sticky=NSEW)



etq1=ttk.Label(secondframe,text="Voltaje DC")
etq2=ttk.Label(secondframe,text="Voltaje DC")
etq3=ttk.Label(secondframe,text="Voltaje DC")
#graficar()
#grapha()
archivo=open("valoresmotor.txt","r")
valmotores=[]
valmotores=archivo.readline()
valmotores2=[]
valmotores2.append("Carga R-L-E")
while valmotores != "":
	valmotores2.append(valmotores)
	valmotores=archivo.readline()

#def calcular():



def botonvolt():
	global boton11,botonstate,borrarboton,app,mainframe
	if botonstate[0]==0:
		if borrarboton==0:
			boton11.grid_forget()
			boton11= Button(mainframe, font='fuenteusada', text="Voltaje",command=botonvolt,fg="black",bg="#FFFFFF",relief="ridge")
			boton11.grid(column=5, row=2,sticky=NSEW,padx=3,pady=1)
			botonstate[0]=1
			borrarboton=1
	
	if botonstate[0]==1:
		if borrarboton==0:
			boton11.grid_forget()
			boton11= Button(mainframe, font='fuenteusada', text="Voltaje",command=botonvolt,fg="white",bg="#6904A6",relief="ridge")
			boton11.grid(column=5, row=2,sticky=NSEW,padx=3,pady=1)
			botonstate[0]=0
			borrarboton=1
	borrarboton=0

def botonCorr():
	global boton21,botonstate,borrarboton,app,mainframe
	if botonstate[1]==0:
		if borrarboton==0:
			boton21.grid_forget()
			boton21= Button(mainframe, font='fuenteusada', text="Corriente",command=botonCorr,fg="black",bg="#FFFFFF",relief="ridge")
			boton21.grid(column=5, row=3,sticky=NSEW,padx=3,pady=1)
			botonstate[1]=1
			borrarboton=1
	
	if botonstate[1]==1:
		if borrarboton==0:
			boton21.grid_forget()
			boton21= Button(mainframe, font='fuenteusada', text="Corriente",command=botonCorr,fg="white",bg="#6904A6",relief="ridge")
			boton21.grid(column=5, row=3,sticky=NSEW,padx=3,pady=1)
			botonstate[1]=0
			borrarboton=1
	borrarboton=0
def botonvelo():
	global boton31,botonstate,borrarboton,app,mainframe
	if botonstate[2]==0:
		if borrarboton==0:
			boton31.grid_forget()
			boton31= Button(mainframe, font='fuenteusada', text="Velocidad",command=botonvelo,fg="black",bg="#FFFFFF",relief="ridge")
			boton31.grid(column=6, row=2,sticky=NSEW,padx=3,pady=1)
			botonstate[2]=1
			borrarboton=1
	
	if botonstate[2]==1:
		if borrarboton==0:
			boton31.grid_forget()
			boton31= Button(mainframe, font='fuenteusada', text="Velocidad",command=botonvelo,fg="white",bg="#6904A6",relief="ridge")
			boton31.grid(column=6, row=2,sticky=NSEW,padx=3,pady=1)
			botonstate[2]=0
			borrarboton=1
	borrarboton=0
def botontorque():
	global boton41,botonstate,borrarboton,app,mainframe
	if botonstate[3]==0:
		if borrarboton==0:
			boton41.grid_forget()
			boton41= Button(mainframe, font='fuenteusada', text="Torque",command=botontorque,fg="black",bg="#FFFFFF",relief="ridge")
			boton41.grid(column=6, row=3,sticky=NSEW,padx=3,pady=1)
			botonstate[3]=1
			borrarboton=1
	
	if botonstate[3]==1:
		if borrarboton==0:
			boton41.grid_forget()
			boton41= Button(mainframe, font='fuenteusada', text="Torque",command=botontorque,fg="white",bg="#6904A6",relief="ridge")
			boton41.grid(column=6, row=3,sticky=NSEW,padx=3,pady=1)
			botonstate[3]=0
			borrarboton=1
	borrarboton=0

def f1(x,y):
	global boxsel2,prueba,Vmnom,RPM,hp,Pnomsal,app,Tm,V1,alpha,anchdisparo,cq,pcq,kan,pp1,pp2,pp3,pp4,pp5,w,lam,R,L,lam
	global kan,ciclo
	if app.caso==1:

		return -y*R/L-(lam/L)+V1/L	
	if app.caso==2:
		if cq[0]==0:
			if cq[1]==0:
				return 0
		if cq[0]==1:
			return -y*R/L-(lam/L)+V1/L*math.sin((x*w))
		if cq[1]==1:
			return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-pi)
	if app.caso==3:
		if cq[0]==0:
			if cq[1]==0:
				return 0
		if cq[0]==1:
			if math.sin(x*w)<=0:
				if x>adisparo[1]+(kan[1])/60:
					return -y*R/L-(lam/L)
		if cq[0]==1:
			return -y*R/L-(lam/L)+V1/L*math.sin((x*w))
	
		if cq[1]==1:
			if math.sin((x*w)+pi)<=0:
				if x>adisparo[0]+(kan[0])/60:
					return -y*R/L-(lam/L)
		if cq[1]==1:
			return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-pi)
	if app.caso>3:
		if app.caso<7:
			if cq[0]==0:
				if cq[1]==0:
					if cq[2]==0:
						if cq[3]==0:
							if cq[4]==0:
								if cq[5]==0:
									return 0
			if app.caso==4:
				if cq[0]==1:
					return -y*R/L-(lam/L)+V1/L*math.sin((x*w))
				if cq[1]==1:
					return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-pi/3)
				if cq[2]==1:
					return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-2*pi/3)
				if cq[3]==1:
					return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-3*pi/3)
				if cq[4]==1:
					return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-4*pi/3)
				if cq[5]==1:
					return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-5*pi/3)

			if app.caso==5:
			
				if cq[0]==1:						
					if math.sin((x*w))>=math.sin((x*w)-pi/3):
						return -y*R/L-(lam/L)+V1/L*math.sin((x*w))

					if math.sin((x*w))<math.sin((x*w)-pi/3):
						if math.sin((x*w)-pi/3)<0:
							return -y*R/L-(lam/L)
						return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-pi/3)

				if cq[2]==1:
					if math.sin((x*w)-2*pi/3)>=math.sin((x*w)-3*pi/3):
						return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-2*pi/3)
					if math.sin((x*w)-2*pi/3)<math.sin((x*w)-3*pi/3):
						if math.sin((x*w)-3*pi/3)<0:
							return -y*R/L-(lam/L)
						return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-3*pi/3)
				
				if cq[4]==1:
					if math.sin((x*w)-4*pi/3)>=math.sin((x*w)-5*pi/3):
							return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-4*pi/3)
					if math.sin((x*w)-4*pi/3)<math.sin((x*w)-5*pi/3):
						if math.sin((x*w)-5*pi/3)<0:		
							return -y*R/L-(lam/L)
						return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-5*pi/3)
			if app.caso==6:
				
				if cq[0]==1:
					if math.sin((x*w))<0:		
						return -y*R/L-(lam/L)
					return -y*R/L-(lam/L)+V1/L*math.sin((x*w))
				

				if cq[1]==1:
					if math.sin((x*w)-1*pi/3)<0:		
						return -y*R/L-(lam/L)
					return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-pi/3)
				
				if cq[2]==1:
					if math.sin((x*w)-2*pi/3)<0:		
						return -y*R/L-(lam/L)
					return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-2*pi/3)
				

				if cq[3]==1:
					if math.sin((x*w)-3*pi/3)<0:		
						return -y*R/L-(lam/L)
					return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-3*pi/3)
				

				if cq[4]==1:

					if math.sin((x*w)-4*pi/3)<0:		
						return -y*R/L-(lam/L)
					return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-4*pi/3)
				
				if cq[5]==1:
					
					if math.sin((x*w)-5*pi/3)<0:		
						return -y*R/L-(lam/L)
					return -y*R/L-(lam/L)+V1/L*math.sin((x*w)-5*pi/3)

	if app.caso==7:
	
		if cq[0]==1:
			return -y*R/L-(lam/L)+V1/math.sqrt(2)/L
		if cq[0]==0:
			return -y*R/L-(lam/L)
def f2(x,y):
	return ((x)-Tm)/J


def f3(x):
	global kan,pcq,cq,lam,app,y,adisparo,K,ciclo,anchdisparo,V1,K,perturbacion,paso
	global boxsel2,prueba,Vmnom,RPM,hp,Pnomsal,app,Tm,alpha,anchdisparo,cq,pcq,kan,pp1,pp2,pp3,pp4,pp5,w,lam
	if perturbacion==1:
		if x>=pp1:
		
			perturbacion=0
			V1=pp2
			K=pp5*K
			alpha=pp3
			anchdisparo=pp4
			if app.caso==7:
				kan[0]=math.trunc(pp1*pp4)
			if app.caso>1:
				if app.caso<4:
					paso=1/60/100
					anchdisparo=anchdisparo/360/60
					adisparo=np.arange(alpha/360/60,alpha/360/60+2/120,1/120)	

			if app.caso>3:	
				if app.caso<7:
					paso=1/60/100
					anchdisparo=anchdisparo/360/60
					adisparo=np.arange(alpha/360/60,alpha/360/60+2/120,1/360)
			if app.caso==7:
				paso=1/anchdisparo/100
				adisparo=np.arange(alpha/anchdisparo,alpha/anchdisparo+1/anchdisparo)




	if app.caso==1:
		return V1
	if app.caso==2:
		volt1=V1*math.sin(w*x)
		volt2=V1*math.sin(w*x+pi)	

		if x>adisparo[0]+(kan[0]/60):	
			pcq[0]=1
		if x>anchdisparo+adisparo[0]+(kan[0]/60):
			pcq[0]=0
			kan[0]=kan[0]+1	

		if x>adisparo[1]+(kan[1]/60):
			pcq[1]=1
		if x>anchdisparo+adisparo[1]+(kan[1]/60):
			pcq[1]=0
			kan[1]=kan[1]+1

		if pcq[0]==1:
			if volt1>lam:
				if volt1>volt2:
					cq[0]=1
					cq[1]=0
		if pcq[1]==1:
			if volt2>lam:
				if volt2>volt1:
					cq[1]=1
					cq[0]=0
		if cq[0]==1:
			return volt1
		if cq[1]==1:
			return volt2
		if cq[0]==0:
			if cq[1]==0:
				return lam
	if app.caso==3:
		volt1=V1*math.sin(w*x)
		volt2=V1*math.sin(w*x+pi)

		if x>adisparo[0]+(kan[0]/60):
			pcq[0]=1
		if x>anchdisparo+adisparo[0]+(kan[0]/60):
			pcq[0]=0
			kan[0]=kan[0]+1

		if x>adisparo[1]+(kan[1]/60):
			pcq[1]=1
		if x>anchdisparo+adisparo[1]+(kan[1]/60):
			pcq[1]=0
			kan[1]=kan[1]+1

		if pcq[0]==1:
			if volt1>lam:
				if volt1>volt2:
					cq[0]=1
					cq[1]=0
		if pcq[1]==1:
			if volt2>lam:
				if volt2>volt1:
					cq[1]=1
					cq[0]=0
		if cq[0]==1:
			if pcq[1]==1:
				return volt2

		if cq[0]==1:
			if volt1<0:
				return 0

		if cq[0]==1:
			return volt1

		if cq[1]==1:
			if pcq[0]==1:
				return volt1

		if cq[1]==1:
			if volt2<0:
				return 0

		if cq[1]==1:
			return volt2
		if cq[0]==0:
			if cq[1]==0:
				return lam
	if app.caso>3:
		if app.caso <7:
			volt1=V1*math.sin(w*x)
			volt2=V1*math.sin((w*x)-1*pi/3)
			volt3=V1*math.sin((w*x)-2*pi/3)
			volt4=V1*math.sin((w*x)-3*pi/3)
			volt5=V1*math.sin((w*x)-4*pi/3)
			volt6=V1*math.sin((w*x)-5*pi/3)
			
			if x>adisparo[0]+(kan[0]/60):
				pcq[0]=1

			if x>anchdisparo+adisparo[0]+(kan[0]/60):
				pcq[0]=0
				kan[0]=kan[0]+1

			if x>adisparo[1]+(kan[1]/60):
				pcq[1]=1
			if x>anchdisparo+adisparo[1]+(kan[1]/60):
				pcq[1]=0
				kan[1]=kan[1]+1

			if x>adisparo[2]+((kan[2])/60):
				pcq[2]=1
			if x>anchdisparo+adisparo[2]+((kan[2])/60):
				pcq[2]=0
				kan[2]=kan[2]+1

			if x>adisparo[3]+(kan[3]/60):
				pcq[3]=1
			if x>anchdisparo+adisparo[3]+(kan[3]/60):
				pcq[3]=0
				kan[3]=kan[3]+1

			if x>adisparo[4]+(kan[4]/60):
				pcq[4]=1
			if x>anchdisparo+adisparo[4]+(kan[4]/60):
				pcq[4]=0
				kan[4]=kan[4]+1

			if x>adisparo[5]+(kan[5]/60):
				pcq[5]=1
			if x>anchdisparo+adisparo[5]+(kan[5]/60):
				pcq[5]=0
				kan[5]=kan[5]+1

			if app.caso==4:
				if pcq[0]==1:
					if volt1>lam:
						cq=np.zeros(6)
						cq[0]=1

				if pcq[1]==1:

					if volt2>lam:
		
						cq=np.zeros(6)
						cq[1]=1

				if pcq[2]==1:
					if volt3>lam:
						cq=np.zeros(6)
						cq[2]=1

				if pcq[3]==1:			
					if volt4>lam:
						cq=np.zeros(6)
						cq[3]=1

				if pcq[4]==1:
					if volt5>lam:
						cq=np.zeros(6)
						cq[4]=1
				if pcq[5]==1:			
					if volt6>lam:
						cq=np.zeros(6)
						cq[5]=1

				if cq[0]==1:
					return volt1
				if cq[1]==1:
					return volt2
				if cq[2]==1:
					return volt3
				if cq[3]==1:
					return volt4
				if cq[4]==1:
					return volt5
				if cq[5]==1:
					return volt6
				if cq[0]==0:
					if cq[1]==0:
						if cq[2]==0:
							if cq[3]==0:
								if cq[4]==0:
									if cq[5]==0:
										return lam
			if app.caso==5:
				if pcq[0]==1:
					if volt1>lam:
						cq=np.zeros(6)
						cq[0]=1
					if volt2>lam:
						cq=np.zeros(6)
						cq[0]=1
					
				if pcq[2]==1:
					if volt3>lam:
						cq=np.zeros(6)
						cq[2]=1
					if volt4>lam:
						cq=np.zeros(6)
						cq[2]=1
					
				if pcq[4]==1:
					if volt5>lam:
						cq=np.zeros(6)
						cq[4]=1
					if volt6>lam:
						cq=np.zeros(6)
						cq[4]=1
					

				if cq[0]==1:						
					if math.sin((x*w))>=math.sin((x*w)-pi/3):
						return volt1

					if math.sin((x*w))<math.sin((x*w)-pi/3):
						if math.sin((x*w)-pi/3)<0:
							return 0
						return volt2
				if cq[2]==1:
					if math.sin((x*w)-2*pi/3)>=math.sin((x*w)-3*pi/3):
						return volt3
					if math.sin((x*w)-2*pi/3)<math.sin((x*w)-3*pi/3):
						if math.sin((x*w)-3*pi/3)<0:
							return 0
						return volt4
				
				if cq[4]==1:
					if math.sin((x*w)-4*pi/3)>=math.sin((x*w)-5*pi/3):
							return volt5
					if math.sin((x*w)-4*pi/3)<math.sin((x*w)-5*pi/3):
						if math.sin((x*w)-5*pi/3)<0:		
							return 0
						return volt6

				if cq[0]==0:
					if cq[1]==0:
						if cq[2]==0:
							if cq[3]==0:
								if cq[4]==0:
									if cq[5]==0:
										return lam	
			if app.caso==6:
				if pcq[0]==1:
					if volt1>lam:
						cq=np.zeros(6)
						cq[0]=1
				if pcq[1]==1:
					if volt2>lam:
						cq=np.zeros(6)
						cq[1]=1
				if pcq[2]==1:
					if volt3>lam:
						cq=np.zeros(6)
						cq[2]=1
				if pcq[3]==1:
					if volt4>lam:
						cq=np.zeros(6)
						cq[3]=1
				if pcq[4]==1:
					if volt5>lam:
						cq=np.zeros(6)
						cq[4]=1
				if pcq[5]==1:
					if volt6>lam:
						cq=np.zeros(6)
						cq[5]=1

				if cq[0]==1:
					if math.sin(w*x)<0:
						return 0
					return volt1

				if cq[1]==1:
					if math.sin((w*x)-pi/3)<0:
						return 0
					return volt2
				if cq[2]==1:
					if math.sin((w*x)-2*pi/3)<0:
						return 0
					return volt3
				if cq[3]==1:
					if math.sin((w*x)-3*pi/3)<0:
						return 0
					return volt4
				if cq[4]==1:
					if math.sin((w*x)-4*pi/3)<0:
						return 0
					return volt5
				if cq[5]==1:
					if math.sin((w*x)-5*pi/3)<0:
						return 0
					return volt6
				if cq[0]==0:
					if cq[1]==0:
						if cq[2]==0:
							if cq[3]==0:
								if cq[4]==0:
									if cq[5]==0:
										return lam
	if app.caso==7:
	
		if x>=kan[0]/anchdisparo:
			
			cq[0]=1
			
		if x>=kan[0]/anchdisparo+adisparo[0]:
			kan[0]=kan[0]+1
			cq[0]=0

		if cq[0]==1:
			
			return V1
		if cq[0]==0:
			return 0
def f5(y):
	global app,cq,lam,R
	if app.caso==1:
		return (y-lam)/R
	if app.caso>1:
		if app.caso<4:
			if cq[0]==1:
				return (y-lam)/R
			if cq[1]==1:
				return (y-lam)/R
			if cq[0]==0:
				if cq[1]==0:
					return 0
	if app.caso>3:
		if app.caso<7:
			if cq[0]==1:
				return (y-lam)/R
			if cq[1]==1:
				return (y-lam)/R
			if cq[2]==1:
				return (y-lam)/R
			if cq[3]==1:
				return (y-lam)/R
			if cq[4]==1:
				return (y-lam)/R
			if cq[5]==1:
				return (y-lam)/R
			if cq[0]==0:
				if cq[1]==0:
					if cq[2]==0:
						if cq[3]==0:
							if cq[4]==0:
								if cq[5]==0:
									return 0
	if app.caso==7:
		if cq[0]==0:
			return 0
		if cq[0]==1:
			return (y-lam)/R

def rk4(f1,f2,f3,a,b,y0,h):
	global cq,lam,prueba
	global boxsel2,prueba,Vmnom,RPM,hp,Pnomsal,app,Tm,V1,alpha,anchdisparo,cq,pcq,kan,pp1,pp2,pp3,pp4,pp5,w,paso,K,L,R
	x=np.arange(a,b+h,h)
	n=len(x)
	y=np.zeros(n)
	v=np.zeros(n)
	v1=np.zeros(n)
	volts=np.zeros(n)
	torque=np.zeros(n)
	y[0]=y0
	v[0]=0
	v1[0]=0
	for i in range(0,n-1):
	
		volts[i+1]=f3(x[i+1])
		if L>0:
			if R>0:
				k11=f1(x[i],y[i])
				k12=f1(x[i]+h/2,y[i]+k11*h/2)
				k13=f1(x[i]+h/2,y[i]+k12*h/2)
				k14=f1(x[i]+h,y[i]+k13*h)
				y[i+1]=y[i]+(h/6)*(k11+2*k12+2*k13+k14)
		if L==0:
			if R>0:
				y[i+1]=f5(volts[i+1])

		if L<0:
			messagebox.showinfo(message="No se admite valores negativos de inductancia", title="Valor Erróneo")
			return 0
		if R<0:
			messagebox.showinfo(message="No se admite valores negativos de resistencia",title="Valor Erróneo")
			return 0
		if R==0:
			messagebox.showinfo(message="Hay un cortocircuito",title="Valor Erróneo")
			return 0

		torque=y*K
		v1[i+1]=f2(torque[i],v[i])*paso
		v1[i+1]=v1[i]+v1[i+1]*60/(2*pi)
		
		if prueba==0:

			lam=v1[i+1]*(2*pi/60)*K
		if prueba==1:

			lam=lam1
		
		if cq[0]==1:
			
			if y[i+1]<0:	
				y[i+1]=0
				torque=y*K
				if app.caso!=7:
					cq[0]=0
		if cq[1]==1:
			if y[i+1]<0:	
				y[i+1]=0
				torque=y*K
				cq[1]=0
		if cq[2]==1:
			if y[i+1]<0:
				y[i+1]=0
				torque=y*K
				cq[2]=0
		if cq[3]==1:
			if y[i+1]<0:
				y[i+1]=0
				torque=y*K
				cq[3]=0
		if cq[4]==1:
			if y[i+1]<0:
				y[i+1]=0
				torque=y*K
				cq[4]=0
		if cq[5]==1:
			if y[i+1]<0:
				y[i+1]=0
				torque=y*K
				cq[5]=0
		if app.caso==7:
			if 	y[i+1]<0:
				y[i+1]=0
	if prueba==0:
		if botonstate[3]==1:
			plt.plot(x,torque, label='Torque(N-m)')
		if botonstate[1]==1:
			plt.plot(x,y, label= 'Corriente(A)')
		if botonstate[2]==1:
			plt.plot(x,v1, label='Velocidad(R.P.M)')
		if botonstate[0]==1:
			plt.plot(x,volts, label= 'Voltaje(V)')
		
		plt.title("Simulación")

		plt.legend()
		plt.show()
	if prueba==1:
		plt.plot(x,y, label= 'Corriente(A)')
		plt.plot(x,volts, label= 'Voltaje(V)')
		plt.title("Simulación")

		plt.legend()
		plt.show()
def simular():
	global boxsel2,prueba,Vmnom,RPM,hp,Pnomsal,app,Tm,V1,R,L,alpha,anchdisparo,cq,pcq,kan,pp1,pp2,pp3,pp4,pp5,w,lam,perturbacion,cc11,cc12,cc13,cc14,cc15,paso
	global app,dato1mm,dato2mm,dato3mm,dato4mm,dato5mm,dato6mm,dato7mm,dato8mm,dato9mm,dato,lam1,adisparo,K
	if prueba==0:
	
		Vmnom=dato[0]
		RPM=dato[1]
		hp=dato[2]
		Pnomsal=dato[3]*1000
		Pnomsal=Pnomsal
		Ian=dato[4]
		R=dato[5]
		L=dato[6]/1000
		J=dato[7]
		Tm=dato[8]
		Egnom=Vmnom-Ian*R
		Wmnom=RPM*2*pi/60
		K=Egnom/Wmnom
		Pnoment=Vmnom*Ian
		Pcobre=Ian*Ian*R
		Prot=Pnoment-Pnomsal-Pcobre
		Tmnom=(Pnomsal+Prot)/Wmnom
		TmPerd=Prot/Wmnom
		Tm=TmPerd+Tm

	if prueba==1:
		R=dato[0]
		L=dato[1]/1000
		lam1=dato[2]
		
	try:
		longitud=float(tiempoentry.get())
	except:
		messagebox.showinfo(message="Se debe especificar el tiempo a simular usando sólo dígitos", title="Valor Erróneo")
		return 0

	V1=datoslistos1
	alpha=datoslistos2
	anchdisparo=datoslistos3
	
	
	w=2*pi*60
	cq=np.zeros(6)
	pcq=np.zeros(6)
	kan=np.zeros(7)

	if app.caso==1:
		paso=1/60/100
	if app.caso>1:
		if app.caso<4:
			paso=1/60/100
			anchdisparo=anchdisparo/360/60
			adisparo=np.arange(alpha/360/60,alpha/360/60+2/120,1/120)

	if app.caso>3:	
		if app.caso<7:
			paso=1/60/100
			anchdisparo=anchdisparo/360/60
			adisparo=np.arange(alpha/360/60,alpha/360/60+2/120,1/360)
	if app.caso==7:
		paso=1/anchdisparo/100
		adisparo=np.arange(alpha/anchdisparo,alpha/anchdisparo+1/anchdisparo)

	rk4(f1,f2,f3,0,longitud,0,paso)

etqfuente  =ttk.Label(secondframe,text="Voltaje DC")
resultado1=ttk.Label(secondframe, text=str(datoslistos1),background="white",font=fuenteusada)
resultado2=ttk.Label(secondframe, text=str(datoslistos2),background="white",font=fuenteusada)
resultado3=ttk.Label(secondframe, text=str(datoslistos3),background="white",font=fuenteusada)
label1= ttk.Label(mainframe,font="fuenteusada", text=" " ,background="#6904A6").grid(column=1, row=1, sticky=N)
boton1= Button(mainframe, font='fuenteusada', text="Simular",command=simular,fg="#6904A6",bg="#FFFFFF",relief="ridge")
boton1.grid(column=3, row=1,rowspan=3,sticky=NSEW,padx=3,pady=1)
boton2= Button(mainframe, font='fuenteusada', text="Accionamiento",command=ventaliment,fg="white",bg="#6904A6",relief="ridge")
boton2.grid(column=1, row=1,sticky=NSEW,padx=3,pady=1)
Logo1=Label(mainframe,image=logo)

Logo1.place(x=630,y=0)
boton3= Button(mainframe, font='fuenteusada', text="Motor",command=configmotor,fg="white",bg="#6904A6", relief="ridge")
boton3.grid(column=1, row=2,sticky=NSEW,padx=3,pady=1,)
boton4= Button(mainframe, font='fuenteusada', text="Cambios",command=configperturb,fg="white",bg="#6904A6",relief="ridge")
boton4.grid(column=1, row=3,sticky=NSEW,padx=3,pady=1)
#boton112= Button(mainframe, font='fuenteusada', text="Graficar",fg="white",bg="#6904A6",relief="ridge")
#boton112.grid(column=5, row=1,sticky=NSEW,padx=3,pady=1)
#boton111= Button(mainframe, font='fuenteusada', text="Transitorio",fg="white",bg="#6904A6",relief="ridge").grid(column=6, row=1,sticky=NSEW,padx=3,pady=1)
boton11= Button(mainframe, font='fuenteusada', text="Voltaje",command=botonvolt,fg="white",bg="#6904A6",relief="ridge")
boton11.grid(column=5, row=2,sticky=NSEW,padx=3,pady=1)
boton21= Button(mainframe, font='fuenteusada', text="Corriente",command=botonCorr,fg="white",bg="#6904A6",relief="ridge")
boton21.grid(column=5, row=3,sticky=NSEW,padx=3,pady=1)
boton31= Button(mainframe, font='fuenteusada', text="Velocidad",command=botonvelo,fg="white",bg="#6904A6", relief="ridge")
boton31.grid(column=6, row=2,sticky=NSEW,padx=3,pady=1)
boton41= Button(mainframe, font='fuenteusada', text="Torque",command=botontorque,fg="white",bg="#6904A6",relief="ridge")
boton41.grid(column=6, row=3,sticky=NSEW,padx=3,pady=1)
tiempoentry=ttk.Entry(mainframe,textvariable=tiempoasimular)
tiempoentry.grid(column=8,row=3,sticky=E)
labeltiempo=ttk.Label(mainframe, text="Tiempo a simular (segundos)",background="#6904A6",font=fuenteusada,foreground="white")
labeltiempo.grid(column=8,row=2,sticky=E)
def main():
	root.mainloop()	

if __name__ == "__main__":

	main()

