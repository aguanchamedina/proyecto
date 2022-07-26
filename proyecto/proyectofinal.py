from tkinter import *

# RESPUESTA DE HOLA, NOMBRE, CEDULA, UBICACIÓN 
def consultar():  
    lblsaludar=Label(ventana,text="Hola " + entradaNombre.get()
                     + " \nIdentificado con cedula: "
                     + entradaCedula.get() + "\nUbicado en: " + entradaubicacion.get(),font=("Arial Black",10),bg="grey68").place(x=50,y=350)
def tipoVehiculo():
    s=selec.get()
    l=entradaAlquiler.get()
    horas=int(l)
    prado = horas*150000
    jeep = horas*200000
    toyota = horas*100000
    Cruiser =horas*80000
    audi =horas*400000
    lblsaludar1=Label(ventana,text=" Escogiste la opcion del vehiculo numero: "
                      + str(s),font=("Arial Black",10),bg="grey68").place(x=50,y=420)
    if s==1:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler del prado es $150000"
                          +"\nEl total a pagar por " + str(l)
                          +"horas de alquiler es:$"+str(prado),font=("Arial Black",10),bg="oliveDrab1").place(x=50,y=460)
        
    elif s==2:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler del jeep es $200000"
                          +"\nEl total a pagar por " + str(l)
                          +"horas de alquiler es:$"+str(jeep),font=("Arial Black",10),bg="oliveDrab1").place(x=50,y=520)
    elif s==3:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler toyota es $100000"
                          +"\nEl total a pagar por " + str(l)
                          +"horas de alquiler es:$"+str(toyota),font=("Arial Black",10),bg="oliveDrab1").place(x=50,y=580)
    elif s==4:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler Cruiser es $80000"
                          +"\nEl total a pagar por " + str(l)
                          +"horas de alquiler es:$"+str(Cruiser),font=("Arial Black",10),bg="oliveDrab1").place(x=50,y=640)
    else:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler audi es $400000"
                          +"\nEl total a pagar por " + str(l)
                          +"horas de alquiler es:$"+str(audi),font=("Arial Black",10),bg="oliveDrab1").place(x=50,y=700)
        
     
#DIMENSIONES DE LA VENTANA
ventana=Tk()
ventana.geometry("2000x1100+0+0")

# TITULO  
ventana.title(" MOVIL RTA CONFI")

# VARIABLES 
lblCedula=Label(text="Cedula:",font=("Arial Black",14),bg="oliveDrab1").place(x=10,y=10)
entradaCedula=StringVar()
txtCedula=Entry(ventana,textvariable=entradaCedula).place(x=115,y=15)

lblNombre=Label(text="Nombre:",font=("Arial Black",14),bg="oliveDrab1").place(x=10,y=40)
entradaNombre=StringVar()
txtNombre=Entry(ventana,textvariable=entradaNombre).place(x=115,y=50)

lblAlquiler=Label(text="¿Por cuantas horas va alquilar el vehiculo?:",font=("Arial Black",14),bg="oliveDrab1").place(x=10,y=100)
entradaAlquiler=IntVar()
txtAlquiler=Entry(ventana,textvariable=entradaAlquiler).place(x=480,y=110)

lblUbicacion=Label(text="Ubicacion:",font=("Arial Black",14),bg="oliveDrab1").place(x=10,y=70)
entradaubicacion=StringVar()
txtUbicacion=Entry(ventana,textvariable=entradaubicacion).place(x=130,y=75)

# BOTONES DE LOS CARROS 
selec=IntVar()

vehiculo1=Radiobutton(ventana,text="1. PRADO",value=1,
                       variable=selec,command=tipoVehiculo,font=("Arial Black",10)).place(x=100,y=140)
vehiculo2=Radiobutton(ventana,text="2. JEEP",value=2,
                       variable=selec,command=tipoVehiculo,font=("Arial Black",10)).place(x=100,y=160)
vehiculo3=Radiobutton(ventana,text="3. TOYOTA",value=3,
                       variable=selec,command=tipoVehiculo,font=("Arial Black",10)).place(x=100,y=180)
vehiculo4=Radiobutton(ventana,text="4. CRUISER",value=4,
                       variable=selec,command=tipoVehiculo,font=("Arial Black",10)).place(x=100,y=200)
vehiculo5=Radiobutton(ventana,text="5. AUDI",value=5,
                       variable=selec,command=tipoVehiculo,font=("Arial Black",10)).place(x=100,y=220)

# IMAGENES DE LOS CARROS 
#miImagen1 = PhotoImage(file="Prado.png")
#Label(ventana,image=miImagen1).place(x=720,y=10)
tex1=Label(text="PRADO:",font=("Arial Black",20)).place(x=580,y=100)

#miImagen2 = PhotoImage(file="jeep.png")
#Label(ventana,image=miImagen2).place(x=1400,y=10)
tex2=Label(text="JEEP:",font=("Arial Black",20)).place(x=1200,y=100)

#miImagen3 = PhotoImage(file="toyota.png")
tex3=Label(text="LAND CRUISER:",font=("Arial Black",20)).place(x=530,y=500)
#Label(ventana,image=miImagen3).place(x=720,y=320)

#miImagen4 = PhotoImage(file="Cruiser.png")
tex4=Label(text="TOYOTA CRUISER:",font=("Arial Black",20)).place(x=1150,y=500)
#Label(ventana,image=miImagen4).place(x=1400,y=400)

#miImagen5 = PhotoImage(file="audi.png")
#Label(ventana,image=miImagen5).place(x=750,y=650)
tex5=Label(text="AUDI:",font=("Arial Black",20)).place(x=650,y=900)

# BOTON CONSULTAR 
btnSaludar=Button(ventana,text="Consultar",command=consultar,font=("Arial Black",15),bg="oliveDrab1").place(x=95,y=270)

# FIN DEL PROGRAMA 
ventana.mainloop()
