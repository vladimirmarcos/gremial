import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from windows.creacion_frame_busqueda import FrameBusqueda
from Procesamiento import procesar_dato_str,procesar_dato_int
from models.afiliados_dao import buscar_dni,cargar_afiliado,buscar_nombre
from models.models import Afiliados
import sqlite3
  
class FrameUser(FrameBusqueda):
    def __init__(self, parent):
        super().__init__(parent)
                
    def campos_datos_usuario(self):
        #label de campos

        self.label_nombre=tk.Label(self,text='Nombre')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=1,column=0,padx=10,pady=10)

        self.label_dni=tk.Label(self,text='DNI')
        self.label_dni.config(font=('Arial',12,'bold'))
        self.label_dni.grid(row=2,column=0,padx=10,pady=10)

        self.label_condicion=tk.Label(self,text='Condicion')
        self.label_condicion.config(font=('Arial',12,'bold'))
        self.label_condicion.grid(row=3,column=0,padx=10,pady=10)

        self.label_domicilio=tk.Label(self,text='Domicilio')
        self.label_domicilio.config(font=('Arial',12,'bold'))
        self.label_domicilio.grid(row=4,column=0,padx=10,pady=10)

        self.label_telefono=tk.Label(self,text='Teléfono')
        self.label_telefono.config(font=('Arial',12,'bold'))
        self.label_telefono.grid(row=5,column=0,padx=10,pady=10)  

        
        self.label_mail=tk.Label(self,text='Mail')
        self.label_mail.config(font=('Arial',12,'bold'))
        self.label_mail.grid(row=6,column=0,padx=10,pady=10)


        #Entrys de cada Campo

        

        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial',12))
        self.entry_nombre.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.mi_dni=tk.StringVar()
        self.entry_dni=tk.Entry(self,textvariable=self.mi_dni)
        self.entry_dni.config(width=50,font=('Arial',12))
        self.entry_dni.grid(row=2,column=1,padx=10,pady=10,columnspan=2)

        self.mi_condicion=ttk.Combobox(self,
                                      state="readonly",
                                      values=["Directo", "Adherente"])
        self.mi_condicion.config(width=50, height=200,font=('Arial',12))
        self.mi_condicion.grid(row=3,column=1,padx=10,pady=10,columnspan=2) 

        self.mi_domicilio=tk.StringVar()
        self.entry_domicilio=tk.Entry(self,textvariable=self.mi_domicilio)
        self.entry_domicilio.config(width=50,font=('Arial',12))
        self.entry_domicilio.grid(row=4,column=1,padx=10,pady=10,columnspan=2)


        self.mi_telefono=tk.StringVar()
        self.entry_telefono=tk.Entry(self,textvariable=self.mi_telefono)
        self.entry_telefono.config(width=50,font=('Arial',12))
        self.entry_telefono.grid(row=5,column=1,padx=10,pady=10,columnspan=2)


        self.mi_mail=tk.StringVar()
        self.entry_mail=tk.Entry(self,textvariable=self.mi_mail)
        self.entry_mail.config(width=50,font=('Arial',12))
        self.entry_mail.grid(row=6,column=1,padx=10,pady=10,columnspan=2)
        self._frame = None

        
    def verificar_dato(self,event):
         
          dni=procesar_dato_int(self.mi_dni.get())
          if dni:
              verificado=buscar_dni(self.organizacion,dni)
              if verificado:
                  titulo=" error al registrar el usuario"
                  mensaje= "el dni ya esta registrado" 
                  messagebox.showerror(titulo,mensaje)
              else: 
                   nombre=procesar_dato_str(self.mi_nombre.get())
                   domicilio=procesar_dato_str(self.mi_domicilio.get())
                   condicion=procesar_dato_str(self.mi_condicion.get())
                   mail=self.mi_mail.get()
                   telefono=self.mi_telefono.get()
                   if nombre=="" or condicion=="":
                       titulo=" error al registrar el usuario"
                       mensaje= "EL nombre y la condición deben ser completados" 
                       messagebox.showerror(titulo,mensaje)
                   else: 
                         if mail=="":
                              mail="no lo tenemos"
                         if telefono=="":
                              telefono="no lo tenemos"
                         if domicilio=="":
                              domicilio="no lo tenemos"
                         afiliado=Afiliados(
                             nombre,
                             dni,
                             domicilio,
                             mail,
                             telefono,
                             condicion

                         )
                         mensaje=f" ¿Desea cargar a la persona {nombre} con dni {dni} con la condición {condicion} cuyo domicilio es {domicilio}, su número de contacto es {telefono} y su mail de contacto es {mail} en {self.organizacion_titulo}?"
                         titulo=f"Nuevo afiliado {self.organizacion_titulo}"
                         respuesta = messagebox.askyesno(titulo, mensaje)
                         if respuesta:
                              cargar_afiliado(self.organizacion,afiliado)
                              titulo="Se cargo exitosamente "
                              mensaje= "el Afiliado en Amep se cargo exitosamente" 
                              messagebox.showinfo(titulo,mensaje)
                              self.desahabilitar_campos()

                       
          else:
              titulo=" error al registrar el usuario"
              mensaje= "El dato ingresado como dni no es válido" 
              messagebox.showerror(titulo,mensaje)
          
    def desahabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_dni.set('')
        self.mi_domicilio.set('')
        self.mi_telefono.set('')
        self.mi_mail.set('')
        self.mi_opciones.set('')
        
       
        self.entry_nombre.config(state='disabled')
        self.entry_dni.config(state='disabled')
        self.entry_domicilio.config(state='disabled')
        self.entry_telefono.config(state='disabled')
        self.entry_mail.config(state='disabled')
        self.mi_condicion.config(state='disabled')
        self.entry_opciones.focus()

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_dni.config(state='normal')
        self.entry_domicilio.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.entry_mail.config(state='normal')
        self.mi_condicion.config(state='normal')
        self.entry_nombre.focus()

        self.entry_nombre.bind ("<Return>",self.verificar_dato)
        self.entry_dni.bind ("<Return>",self.verificar_dato)
        self.entry_domicilio.bind ("<Return>",self.verificar_dato)
        self.entry_telefono.bind ("<Return>",self.verificar_dato)
        self.entry_nombre.bind ("<Return>",self.verificar_dato)
        self.entry_mail.bind ("<Return>",self.verificar_dato)

    def borrar(self):
        self.pack_forget()
        self.destroy()

class FrameUserAmepp(FrameUser):
      def __init__(self,parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_datos_usuario()
        self.habilitar_opciones()
        self.desahabilitar_busqueda_nombre()
        self.desahabilitar_campos()

      
      def verificar_dato(self,event):
         self.organizacion='afiliado_amep'
         self.organizacion_titulo='A.M.E.P.'
         super().verificar_dato(event)
         

      def verifica_tecla(self,event):
         super().verifica_tecla(event)
         if self.variable=='h' or self.variable=='H':
              self.habilitar_campos()

      def  busqueda_nombre(self, event):
                   self.organizacion='afiliado_amep'
                   super().busqueda_nombre(event)
                   
     
class FrameUserAdepp(FrameUser):
     def __init__(self,parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_datos_usuario()
        self.habilitar_opciones()
        self.desahabilitar_busqueda_nombre()
        self.desahabilitar_campos()
    

     def verificar_dato(self,event):
         self.organizacion='afiliado_adep'
         self.organizacion_titulo='A.D.E.P.'
         super().verificar_dato(event)
          
     def  busqueda_nombre(self, event):
                   self.organizacion='afiliado_adep'
                   super().busqueda_nombre(event)

     def verifica_tecla(self,event):
         super().verifica_tecla(event)
         if self.variable=='h' or self.variable=='H':
              self.habilitar_campos()