import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from windows.creacion_frame_busqueda import FrameBusqueda
from Procesamiento import procesar_dato_str,procesar_dato_int
from models.afiliados_dao import buscar_dni,informacion_editar,informacion_editada
import sqlite3
  


class FrameEditUser(FrameBusqueda):
    def __init__(self, parent):
        super().__init__(parent)
        
    def campos_datos_usuario(self):
        #label de campos

        self.label_dni_cuenta=tk.Label(self,text='DNI de cuenta a editar')
        self.label_dni_cuenta.config(font=('Arial',12,'bold'))
        self.label_dni_cuenta.grid(row=1,column=1,padx=10,pady=10)


        self.label_nombre=tk.Label(self,text='Nombre')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=2,column=0,padx=10,pady=10)
        
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

        self.label_dni=tk.Label(self,text='DNI')
        self.label_dni.config(font=('Arial',12,'bold'))
        self.label_dni.grid(row=7,column=0,padx=10,pady=10)


        #Entrys de cada Campo

        self.mi_dni_cuenta=tk.StringVar()
        self.entry_dni_cuenta=tk.Entry(self,textvariable=self.mi_dni_cuenta)
        self.entry_dni_cuenta.config(width=50,font=('Arial',12))
        self.entry_dni_cuenta.grid(row=1,column=2,padx=10,pady=10,columnspan=2)

        self.mi_nombre=tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial',12))
        self.entry_nombre.grid(row=2,column=1,padx=10,pady=10,columnspan=2)

        

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

        self.mi_dni=tk.StringVar()
        self.entry_dni=tk.Entry(self,textvariable=self.mi_dni)
        self.entry_dni.config(width=50,font=('Arial',12))
        self.entry_dni.grid(row=7,column=1,padx=10,pady=10,columnspan=2)        
        self._frame = None

    def desahabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_dni.set('')
        self.mi_domicilio.set('')
        self.mi_telefono.set('')
        self.mi_mail.set('')
        self.mi_opciones.set('')
        self.mi_dni_cuenta.set('')
        
       
        self.entry_nombre.config(state='disabled')
        self.entry_dni.config(state='disabled')
        self.entry_domicilio.config(state='disabled')
        self.entry_telefono.config(state='disabled')
        self.entry_mail.config(state='disabled')
        self.mi_condicion.config(state='disabled')
        self.entry_dni_cuenta.config(state='disabled')
        self.entry_opciones.focus()

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_dni.config(state='normal')
        self.entry_domicilio.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.entry_mail.config(state='normal')
        self.mi_condicion.config(state='normal')
        self.entry_dni_cuenta.config(state='normal')
        
        self.entry_dni_cuenta.bind ("<Return>",self.editar_dato)
        self.entry_nombre.bind ("<Return>",self.editar_dato)
        self.entry_dni.bind ("<Return>",self.editar_dato)
        self.entry_domicilio.bind ("<Return>",self.editar_dato)
        self.entry_telefono.bind ("<Return>",self.editar_dato)
        self.entry_mail.bind ("<Return>",self.editar_dato)
        self.entry_dni_cuenta.focus()
    def editar_dato(self,event):
        dni_cuenta=procesar_dato_int(self.mi_dni_cuenta.get())
        if dni_cuenta:
            verificar_cuenta=buscar_dni(self.organizacion,dni_cuenta)
            if verificar_cuenta:
                datos=informacion_editar(self.organizacion,dni_cuenta)
                nombre_actual=datos[0]
                dni_actual=datos[1]
                direccion_actual=datos[2]
                mail_actual=datos[3]
                telefono_actual=datos[4]
                condicion_actual=datos[5]

                nombre=self.mi_nombre.get()
                dni=self.mi_dni.get()
                direccion=self.mi_domicilio.get()
                mail=self.mi_mail.get()
                telefono=self.mi_telefono.get()
                condicion=self.mi_condicion.get()
                if((nombre=="")and(dni=="")and(direccion=="")and(mail=="")and (telefono=="")and condicion==""):
                    titulo="No se ingreso dato"
                    mensaje="No se detectaron campos a modificar"
                    messagebox.showerror(titulo,mensaje)

                else:
                    if (nombre!=""):
                        titulo="Cambio de Nombre"
                        mensaje=f"¿Esta seguro de cambiar {nombre_actual} con dni {dni_actual} por {nombre} ?"
                        respuesta = messagebox.askyesno(titulo, mensaje)
                        if respuesta:
                                informacion_editada(self.organizacion,'nombre',nombre,dni_cuenta)
                                titulo="Se cambio nombre del afiliado exitosamente"
                                mensaje=f"El nombre del afiliado es {nombre}"
                                messagebox.showinfo(titulo,mensaje) 
                    if (mail!=""):
                        titulo="Cambio de mail"
                        mensaje=f"¿Esta seguro de cambiar el mail {mail_actual} del afiliado con nombre {nombre_actual} con dni {dni_actual} por {mail} ?"
                        respuesta = messagebox.askyesno(titulo, mensaje)
                        if respuesta:
                            informacion_editada(self.organizacion,'mail',mail,dni_cuenta)
                            titulo="Se cambio mail del afiliado exitosamente"
                            mensaje=f"El mail del afiliado es {mail}"
                            messagebox.showinfo(titulo,mensaje) 
                    if (telefono!=""):
                        titulo="Cambio de telefono"
                        mensaje=f"¿Esta seguro de cambiar el telefono {telefono_actual} del afiliado con nombre {nombre_actual} con dni {dni_actual} por {telefono} ?"
                        respuesta = messagebox.askyesno(titulo, mensaje)
                        if respuesta:
                            informacion_editada(self.organizacion,'telefono',telefono,dni_cuenta)
                            titulo="Se cambio telefono del afiliado exitosamente"
                            mensaje=f"El teléfono del afiliado es {telefono}"
                            messagebox.showinfo(titulo,mensaje) 

                    if (direccion!=""):
                        titulo="Cambio de direccion"
                        mensaje=f"¿Esta seguro de cambiar la direccion{direccion_actual} del afiliado con nombre {nombre_actual} con dni {dni_actual} por {direccion} ?"
                        respuesta = messagebox.askyesno(titulo, mensaje)
                        if respuesta:
                            informacion_editada(self.organizacion,'domicilio',direccion,dni_cuenta)
                            titulo="Se cambio direccion del afiliado exitosamente"
                            mensaje=f"La direccion del afiliado es {direccion}"
                            messagebox.showinfo(titulo,mensaje) 

                    if (condicion!=""):
                        titulo="Cambio de condicion"
                        mensaje=f"¿Esta seguro de cambiar la condicion {condicion_actual} del afiliado con nombre {nombre_actual} con dni {dni_actual} por {condicion} ?"
                        respuesta = messagebox.askyesno(titulo, mensaje)
                        if respuesta:
                            informacion_editada(self.organizacion,'condicion',condicion,dni_cuenta)
                            titulo="Se cambio condicion del afiliado exitosamente"
                            mensaje=f"La condicion del afiliado es {condicion}"
                            messagebox.showinfo(titulo,mensaje) 
                    if (dni!=""):
                        dni=procesar_dato_int(dni)
                        if dni:
                            titulo="Cambio de condicion"
                            mensaje=f"¿Esta seguro de cambiar el dni {dni_actual} del afiliado con nombre {nombre_actual} por {dni} ?"
                            respuesta = messagebox.askyesno(titulo, mensaje)
                            if respuesta:
                                informacion_editada(self.organizacion,'dni',dni,dni_cuenta)
                                titulo="Se cambio el dni exitosamente"
                                mensaje=f"El nuevo dni del afiliado {nombre_actual} es {dni}"
                                messagebox.showinfo(titulo,mensaje)  

                        else:
                            titulo="Dato no valido como DNI"
                            mensaje="El dato ingresado como DNI a modificar no es un dato válido"
                            messagebox.showerror(titulo,mensaje)      
                        

            else:
                titulo="DNI no valido"
                mensaje=f"El dni {dni_cuenta} no esta asociado a ningun afiliado de {self.organizacion_titulo}"
                messagebox.showerror(titulo,mensaje)
        else:
            titulo="Dato no valido como DNI"
            mensaje="El dato ingresado como DNI a buscar no es un dato válido"
            messagebox.showerror(titulo,mensaje)

    def verifica_tecla(self,event):
         super().verifica_tecla(event)
         if self.variable=='h' or self.variable=='H':
              self.habilitar_campos()

class FrameEditarAmeppUser(FrameEditUser):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_datos_usuario()
        self.desahabilitar_busqueda_nombre()
        self.desahabilitar_campos()
        self.habilitar_opciones()
    
    def editar_dato(self,event):
        self.organizacion='afiliado_amep'
        self.organizacion_titulo='A.M.E.P.'
        super().editar_dato(event)


class FrameEditarAdeppUser(FrameEditUser):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_datos_usuario()
        self.desahabilitar_busqueda_nombre()
        self.desahabilitar_campos()
        self.habilitar_opciones()
    
    def editar_dato(self,event):
        self.organizacion='afiliado_adep'
        self.organizacion_titulo='A.D.E.P.'
        super().editar_dato(event)