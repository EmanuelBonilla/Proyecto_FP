import tkinter
import tkinter.messagebox
from tkinter import*
from PIL import ImageTk, Image
from datos import*

#------------------------------------------------VENTANA------------------------
#aqui ponemos que una variable es tipo tkinter
ventana= tkinter.Tk()

#aqui ponemos el titulo de la ventana
ventana.title("ASISTENCIA DOCENCIA")

#tamaño de la ventana
ventana.geometry("500x500")

#aqui se puede configurar si el tamaño d ela vetana se pyede cambiar 
ventana.resizable(False,False)

#config
ventana.config(bg="#AD3333")


#-------------------------------------FUNCIONES--------------------------------
def salir():
	ventana.destroy()


def comprobar():
	flag=0
	contador=0
	for i in usuarios:
		contador=contador+1
		if i == user.get():
			flag=contador
	if flag==0:
		tkinter.messagebox.showinfo("","No se encontro el nombre:  "+user.get())

	if flag>0:
		if contrasena[flag-1]==ca.get():
			tkinter.messagebox.showinfo("","DATOS CORRECTOS")
			ventana.destroy()
			resultados=tkinter.Tk()

			#configuraciones de ventana
			resultados.title("ASISTENCIA DOCENCIA")
			resultados.geometry("500x500")
			resultados.resizable(0,0)


			#labels
			lbl_nombre=tkinter.Label(resultados,text="Nombre: "+nombre[flag-1])
			lbl_nombre.pack()
			lbl_nombre.place(x=20,y=20)

			lbl_edad=tkinter.Label(resultados,text="Edad: "+edad[flag-1])
			lbl_edad.pack()
			lbl_edad.place(x=20,y=40)

			lbl_telefono=tkinter.Label(resultados,text="Telefono: "+telefono[flag-1])
			lbl_telefono.pack()
			lbl_telefono.place(x=20,y=60)

			lbl_cedula=tkinter.Label(resultados,text="Cedula: "+cedula[flag-1])
			lbl_cedula.pack()
			lbl_cedula.place(x=20,y=80)

			lbl_materia=tkinter.Label(resultados,text="Materia: "+materia[flag-1])
			lbl_materia.pack()
			lbl_materia.place(x=20,y=100)

			c_salon=0
			if flag==1 or flag==3:
				c_salon=1
			if flag==2:
				c_salon=0

			lbl_Horario=tkinter.Label(resultados,text="Su horario de clases es en el salon "+salon[c_salon]+" de: "+hora[flag-1]+" a "+hora[flag])
			lbl_Horario.pack()
			lbl_Horario.place(x=20,y=120)

			#funciones
			def COAS():
				tkinter.messagebox.showinfo("SISTEMA","ASISTENCIA AÑADIDA")
			def salir_2():
				resultados.destroy()



			boton_as= tkinter.Button(resultados,text="Confirmar Asistencia",command=COAS)
			boton_as.pack()
			boton_as.place(x=300,y=460)

			boton_sa= Button(resultados,text="SALIR",command=salir_2)
			boton_sa.pack()
			boton_sa.place(x=100,y=460)

			resultados.mainloop()

		else:
			tkinter.messagebox.showinfo("","CONTRASEÑA INCORRECTA")



#-------------------------------------------ETIQUETA----------------------
#cabezera
cabezera= tkinter.Label(ventana, text="Bienvenido a el programa").place(x=20,y=20 ,height=20, width=180 )


#-------------------------------------------ENTRY-------------------------
lbl_USUARIO = Label(ventana,text="USUARIO: ").place(x=20,y=40,height=20,width=200)
lbl_CONTRASEÑA = Label(ventana,text="CONTRASEÑA: ").place(x=20,y=60,height=20,width=200)


user=tkinter.Entry(ventana,fg="blue")
user.pack()
user.place(x=200,y=40,height=20,width=200)

ca=tkinter.Entry(ventana,fg="blue")
ca.pack()
ca.place(x=200,y=60,height=20,width=200)

#-------------------------------------------BOTON------------------------
boton2= tkinter.Button(ventana, text="SALIR",command=salir)
boton2.pack()
boton2.place(x=20,y=80, height=20, width=150)

boton3= Button(ventana,text="ENTRAR",command=comprobar,fg="blue")
boton3.pack()
boton3.place(x=150,y=80,height=20,width=150)


#---------------------------------------IMG--------------------------
#cambiams el tamaño de la imagen
image= Image.open("edlu.png")
image= image.resize((200,200),Image.Resampling.LANCZOS)


img = ImageTk.PhotoImage(image)
lbl_img = Label(ventana, image=img)

#el uso del place inhabilita el uso del pack practicamente
lbl_img.place(x=300,y=300)


#esto funciona para que la ventana se mantenga siempre abierta
ventana.mainloop()