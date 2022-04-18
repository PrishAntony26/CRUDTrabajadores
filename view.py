import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from datetime import time,date, datetime
from controller import *
from entity import *

class Application:
    #constructor
    def __init__(self):
        #crear objeto ventana de la clase Tk
        self.ventana=tk.Tk() 
        #crear objeto de la clase TrabajadorController
        self.obj=TrabajadorController()
        #Variables
        self.vCodigo = tk.StringVar()
        self.vNombre = tk.StringVar()
        self.vfecha = tk.StringVar()
        self.vCargo = tk.StringVar()
        self.vArea = tk.StringVar()
        self.vSueldo = tk.StringVar()
        
       
        self.vfecha.set(date.today().strftime("%d/%m/%Y"))
        #VENTANA
        self.ventana.title(":: SISTEMA DE TRABAJADORES ::")
        self.ventana.geometry("550x550")
        self.ventana.configure(background="#DE9523")#Cyan
        #TITULO
        self.Label1 = tk.Label(text="CRUD DE TRABAJADORES",bg="#C7D750",fg="black",font=("Calibri",16)).place(x=180, y=10)
        
        #ETIQUETA Y TEXBOX
        self.label2 = tk.Label(text="Codigo",bg="#C7D750",fg="black").place(x=50,y=50)
        self.txtbox1 = tk.Entry(self.ventana,textvariable=self.vCodigo,width=20).place(x=175,y=50)
       
        self.label3 = tk.Label(text="Nombre",bg="#C7D750",fg="black").place(x=50,y=80)
        self.txtbox2 = tk.Entry(textvariable=self.vNombre,width=30).place(x=175,y=80)
        
        self.label9 = tk.Label(text="Fecha",bg="#C7D750",fg="black").place(x=50,y=110)
        self.txtbox8 = tk.Entry(textvariable=self.vfecha,width=10).place(x=175,y=110)
        
        self.label20 = tk.Label(text="Cargo",bg="#C7D750",fg="black").place(x=50,y=140)
        self.txtbox9 = tk.Entry(textvariable=self.vCargo,width=20).place(x=175,y=140)
        
        self.label21 = tk.Label(text="Area",bg="#C7D750",fg="black").place(x=50,y=170)
        self.txtbox10 = tk.Entry(textvariable=self.vArea,width=20).place(x=175,y=170)
        
        self.label22 = tk.Label(text="Sueldo",bg="#C7D750",fg="black").place(x=50,y=200)
        self.txtbox11 = tk.Entry(textvariable=self.vSueldo,width=20).place(x=175,y=200)
       
        #BOTONES
        self.btn1 = tk.Button(text="Grabar",command=self.insertardatos,bg="#C7D750",fg="black",width=8).place(x=40,y=250) #boton guardar
        
        self.btn2 = tk.Button(text="Modificar", command=self.actualizardatos,bg="#C7D750",fg="black",width=8).place(x=130,y=250) #boton modificar
      
        self.btn3 = tk.Button(text="Eliminar", command=self.eliminar,bg="#C7D750",fg="black",width=8).place(x=230,y=250) #boton eliminarS
       
        self.btn4 = tk.Button(text="Listar", command=self.listardatos,bg="#C7D750",fg="black",width=8).place(x=330,y=250) #boton listar
      
        self.btn5 = tk.Button(text="Limpiar", command=self.nuevo,bg="#C7D750",fg="black",width=8).place(x=430,y=250) #boton nuevo
       
        self.btn6 = tk.Button(text="Buscar",command=self.buscar,bg="#C7D750",fg="black",width=8).place(x=350,y=50) #boton buscar
        #frame
        self.tree_frame = tk.Frame(self.ventana)
        self.tree_frame.config(height=5)
        self.tree_frame.pack(side=BOTTOM)
        
         #TABLA
        self.tv = ttk.Treeview(self.tree_frame,selectmode='browse')
        self.tv['columns']=('Codigo', 'Nombre', 'Fecha','Cargo','Area','Sueldo')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('Codigo', anchor=CENTER, width=60,minwidth=60)
        self.tv.column('Nombre', anchor=tk.W, width=100,minwidth=100)
        self.tv.column('Fecha', anchor=CENTER, width=80,minwidth=80)
        self.tv.column('Cargo', anchor=tk.W, width=100,minwidth=100)
        self.tv.column('Area', anchor=tk.W, width=100,minwidth=100)
        self.tv.column('Sueldo', anchor=tk.W, width=60,minwidth=60)
        vsb = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tv.yview)
        vsb.pack(side='right',fill='y')
        self.tv.configure(yscrollcommand=vsb.set)

       
        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('Codigo', text='Id', anchor=CENTER)
        self.tv.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tv.heading('Fecha', text='Fecha', anchor=CENTER)
        self.tv.heading('Cargo', text='Cargo', anchor=tk.W)
        self.tv.heading('Area', text='Area', anchor=tk.W)
        self.tv.heading('Sueldo', text='Sueldo', anchor=tk.W)
        self.tv.pack(side=BOTTOM)
        
        self.listardatos()
        self.ventana.mainloop()
#end class
    
# lista de metodos

    def insertardatos(self):
        #crear objeto alu de la clase Trabajador
        #Validar que se ingresen todos los datos 
        if(self.vCodigo.get()!=""and self.vNombre.get()!=""and self.vfecha.get()!=""and self.vCargo.get()!=""and self.vArea.get()!=""and self.vSueldo.get()!=""):
            #Validacion formato codigo y que el sueldo sea un numero 
            if(self.formatoCodigo(self.vCodigo.get())and self.validarSueldo(self.vSueldo.get())):
                tr=Trabajador(self.vCodigo.get(),self.vNombre.get(),self.vfecha.get(),self.vCargo.get(),self.vArea.get(),float(self.vSueldo.get()))
                    #METODO DE CONTROLLER 
                msg= self.obj.procesarTrabajador(tr,1)
                tkinter.messagebox.showinfo("Informacion", msg)
                self.nuevo()
                self.listardatos()
            else:
                tkinter.messagebox.showinfo("Error","Formato de codigo incorrecto, intentelo nuevamente")   
                self.nuevo()
        else:
             tkinter.messagebox.showinfo("Error","Debe ingresar todos los datos solicitados")   
    
    def formatoCodigo(self,cad):
        return cad.startswith("E")
        
    def validarSueldo(self,num):
        try:
            num = int(num)
            return True
        except ValueError:
            tkinter.messagebox.showinfo("Error","Debe ingresar un numero en el sueldo")
            return False
      
            
    def listardatos(self):
        #limpiar tabla
        for i in self.tv.get_children():
            self.tv.delete(i) 
        #METODO CONTROLLER            
        trabajadores = self.obj.listaTrabajador()
        for t in trabajadores:
            self.tv.insert('', 'end', values=(t['codigo'],t['nombre'],t['fecha'],t['cargo'],t['area'],t['sueldo']))
        
    #end def
    
    def actualizardatos(self):
        #crear objeto alu de la clase Alumno
        tr=Trabajador(self.vCodigo.get(),self.vNombre.get(),self.vfecha.get(),self.vCargo.get(),self.vArea.get(),float(self.vSueldo.get()))
        msg=self.obj.procesarTrabajador(tr,2)  
        tkinter.messagebox.showinfo("Informacion", msg)
        self.nuevo()
        self.listardatos()
    
    def nuevo(self):
        self.vCodigo.set("")
        self.vNombre.set("")
        self.vCargo.set("")
        self.vArea.set("")
        self.vSueldo.set("")
        for i in self.tv.get_children():
            self.tv.delete(i)
        
       
    def eliminar(self):
         #variable
        #codigo=self.vCodigo.get()
        # Validamos que ha
        tr=Trabajador(self.vCodigo.get(),self.vNombre.get(),self.vfecha.get(),self.vCargo.get(),self.vArea.get(),float(self.vSueldo.get()))
        msg=self.obj.procesarTrabajador(tr,3)
        tkinter.messagebox.showinfo("Informacion", msg)
        self.nuevo()
        self.listardatos()
    
    def buscar(self):
         #variable
        
        codigo=self.vCodigo.get()
        if(codigo!=""):
            trabajador=self.obj.buscarTrabajador(codigo)
            if trabajador!=None:
                self.vCodigo.set(trabajador[0])
                self.vNombre.set(trabajador[1])
                self.vfecha.set(trabajador[2])
                self.vCargo.set(trabajador[3])
                self.vArea.set(trabajador[4])
                self.vSueldo.set(trabajador[5])
            else:
                tkinter.messagebox.showwarning("Aviso", "Trabajador no existe")
                self.nuevo()
        else:
             tkinter.messagebox.showwarning("Aviso", "Debe ingresar el codigo de trabajador para realizar busqueda")  
    
#end class


#prueba de ventana

Aplicacion = Application()
