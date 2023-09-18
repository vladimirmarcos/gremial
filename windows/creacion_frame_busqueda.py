import tkinter as tk
from tkinter import ttk,END
import re 
from Procesamiento import procesar_dato_int,procesar_dato_str,procesar_dato_float
from models.afiliados_dao import buscar_nombre
from tkinter import messagebox
import sqlite3

class FrameBusqueda(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.campos_busquedas()
        self.habilitar_opciones()
        self.desahabilitar_busqueda_nombre()
        
        

    def campos_busquedas(self):
       #busqueda nombre 
        self.label_opciones=tk.Label(self,text='Opciones')
        self.label_opciones.config(font=('Arial',12,'bold'))
        self.label_opciones.grid(row=0,column=1,padx=10,pady=10)

        self.label_busqueda_nombre=tk.Label(self,text='Busqueda por nombre')
        self.label_busqueda_nombre.config(font=('Arial',12,'bold'))
        self.label_busqueda_nombre.grid(row=10,column=2,padx=10,pady=10)

        self.mi_opciones=tk.StringVar()
        self.entry_opciones=tk.Entry(self,textvariable=self.mi_opciones)
        self.entry_opciones.config(width=50,font=('Arial',12))
        self.entry_opciones.grid(row=0,column=2,padx=10,pady=10,columnspan=2)
        self.entry_opciones.bind ("<Key>",self.verifica_tecla)

        self.mi_busqueda_nombre=tk.StringVar()
        self.entry_busqueda_nombre=tk.Entry(self,textvariable=self.mi_busqueda_nombre)
        self.entry_busqueda_nombre.config(width=50,font=('Arial',12))
        self.entry_busqueda_nombre.grid(row=10,column=3,padx=10,pady=10,columnspan=2)
        self.entry_busqueda_nombre.bind ("<Return>",self.busqueda_nombre)
        
        self._frame = None


        
    
    
            
    def desahabilitar_busqueda_nombre(self):
            self.mi_busqueda_nombre.set('')
            self.entry_busqueda_nombre.config(state='disabled')
            self.habilitar_opciones()

    def verifica_tecla(self,event):
         self.variable=event.char
         if self.variable=='b' or self.variable=='B':
              self.habilitar_busqueda_nombre()


    def habilitar_busqueda_nombre(self):
          self.entry_busqueda_nombre.config(state='normal')
          self.entry_busqueda_nombre.focus()       


    def habilitar_opciones(self):
         self.mi_opciones.set('')
         self.entry_opciones.config(state='disabled')
         self.entry_opciones.config(state='normal')
         self.entry_opciones.focus()

    def busqueda_nombre(self,event):
         self.nombre=self.mi_busqueda_nombre.get()
         if self.nombre !="":
                        try:
                            usuarios_encontrados=buscar_nombre (self.nombre,self.organizacion)
                            
                            if usuarios_encontrados:
                                
                                
                                titulo=f" Usuarios con nombre {self.nombre}"
                                mensaje= "\n "
                                for i in usuarios_encontrados:
                                         mensaje=mensaje+"Nombre "+ str(i[0])+ " dni "+ str(i[1])+" su número de cuenta "+str(i[2])+"\n"
                                messagebox.showinfo(titulo,mensaje)
                                self.desahabilitar_busqueda_nombre()
                                
                            else: 
                                titulo="No se encontro nombre"
                                mensaje= f"el nombre {self.nombre} no tiene asociada ninguna cuenta" 
                                messagebox.showerror(titulo,mensaje)
                                self.desahabilitar_busqueda_nombre()

                        except sqlite3.OperationalError:
                            titulo="No se ingresar a la base de datos"
                            mensaje= "La base de datos esta siendo ocupada o esta dañada, intente más   tarde" 
                            messagebox.showerror(titulo,mensaje)
                            self.desahabilitar_busqueda_nombre()
                                
                        
                       
                       
         else:
                            titulo="No ingreso nombre"
                            mensaje= "Se envio el campo vacío" 
                            messagebox.showerror(titulo,mensaje)
         
              
    def borrar(self):
        self.pack_forget()
        self.destroy()