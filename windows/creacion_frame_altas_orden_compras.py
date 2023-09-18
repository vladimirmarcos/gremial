import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar,DateEntry
from windows.creacion_frame_busqueda import FrameBusqueda
from Procesamiento import procesar_dato_str,procesar_dato_int
from models.afiliados_dao import buscar_dni,informacion_editar,informacion_editada,buscar_id
from models.orden_credito_dao import buscar_ordenes_creditos_bajas,buscar_orden_compras,buscar_informacion_orden,guardar_datos_fechas, actualizar_estado_orden
import sqlite3
from datetime import datetime

import calendar

class FrameFecha(FrameBusqueda):
    def __init__(self, parent):
        super().__init__(parent)
        
        
        
    def campos_datos_usuario(self):
        #label de campos

        self.label_numero_orden=tk.Label(self,text='Número de orden a dar')
        self.label_numero_orden.config(font=('Arial',12,'bold'))
        self.label_numero_orden.grid(row=1,column=0,padx=10,pady=10)

        self.label_fecha_alta=tk.Label(self,text='Fecha de Alta')
        self.label_fecha_alta.config(font=('Arial',12,'bold'))
        self.label_fecha_alta.grid(row=2,column=0,padx=10,pady=10)

        self.label_busqueda_ordenes=tk.Label(self,text='Busqueda N Cuenta')
        self.label_busqueda_ordenes.config(font=('Arial',12,'bold'))
        self.label_busqueda_ordenes.grid(row=9,column=2,padx=10,pady=10)


        #Entrys de cada Campo
        self.mi_numero_orden=tk.StringVar()
        self.entry_numero_orden=tk.Entry(self,textvariable=self.mi_numero_orden)
        self.entry_numero_orden.config(width=50,font=('Arial',12))
        self.entry_numero_orden.grid(row=1,column=1,padx=10,pady=10,columnspan=2)


        self.cal=DateEntry(self,
                           width=70,
                           mindate=datetime(2023,1,1),
                           maxdate=datetime(2100,12,31))
        self.cal.grid(row=2,column=1,padx=10,pady=10,columnspan=2) 

        self.mi_numero_cuenta=tk.StringVar()
        self.entry_numero_cuenta=tk.Entry(self,textvariable=self.mi_numero_cuenta)
        self.entry_numero_cuenta.config(width=50,font=('Arial',12))
        self.entry_numero_cuenta.grid(row=9,column=3,padx=10,pady=10,columnspan=2)  
        self._frame = None

    def desahabilitar_campos(self):
        self.mi_numero_orden.set('')
        self.mi_opciones.set('')
        self.entry_numero_orden.config(state='disabled')
        self.cal.config(state='disabled')
        self.entry_opciones.focus()
    def desahabilitar_campos_busqueda_n_cuenta(self):
        self.mi_numero_cuenta.set('')
        self.mi_opciones.set('')
        self.entry_numero_cuenta.config(state='disabled')
        self.entry_opciones.focus()

    def habilitar_campos(self):
        self.entry_numero_orden.config(state='normal')
        self.cal.config(state='normal')
        
        
        self.entry_numero_orden.bind ("<Return>",self.generar_alta_orden)
        self.cal.bind ("<Return>",self.generar_alta_orden)
        self.entry_numero_orden.focus()

    def generar_alta_orden(self,event):
         numero_orden=procesar_dato_int(self.entry_numero_orden.get())
         if numero_orden:
            id_orden=buscar_orden_compras(self.orden_compra_organizacion,numero_orden)
            if id_orden:
                informacion_orden=buscar_informacion_orden(self.orden_compra_organizacion,id_orden)
                if informacion_orden:
                    id_usuario=informacion_orden[0]
                    informacion_afiliado=buscar_id(self.organizacion,id_usuario)
                    if informacion_afiliado:
                         nombre=informacion_afiliado[0]
                         dni=informacion_afiliado[1]
                         monto=informacion_orden[1]
                         descuento=informacion_orden[2]
                         mes=informacion_orden[3]
                         cuotas=int(informacion_orden[4])
                         fecha=self.cal.get()
                         titulo="Cambio de condicion"
                         mensaje=f"¿Esta seguro de generar orden de compra del afiliado {nombre} con dni {dni} perteneciente a {self.titulo_organizacion}, con monto de {monto}, descuento de {descuento} %, en cuotas de {cuotas} válida desde el mes de {mes} con fecha de alta {fecha} ?"
                         respuesta = messagebox.askyesno(titulo, mensaje)
                         if respuesta:
                              monto_cuota=(monto-monto*(descuento/100))/cuotas
                              fechas_vencimiento=guardar_datos_fechas(self.fecha_vencimiento_organizacion,fecha,cuotas,"sin pagar",id_usuario,id_orden,monto_cuota)
                              actualizar_estado_orden(id_orden,self.orden_compra_organizacion,"alta")
                              titulo="Fechas de pagos y montos"
                              mensaje=""
                              for i in range (len(fechas_vencimiento)):
                                   mensaje=mensaje+f"El paga número {i+1} vence la fecha {fechas_vencimiento[i]} con un monto de {monto_cuota}"+"\n"
                              self.desahabilitar_campos()
                              messagebox.showinfo(titulo,mensaje)
                    else: 
                     titulo="Error base de datos"
                     mensaje="No se pudo ingresar a la base de datos intente más tarde"
                     messagebox.showerror(titulo,mensaje)
                         
                else: 
                     titulo="Error base de datos"
                     mensaje="No se pudo ingresar a la base de datos intente más tarde"
                     messagebox.showerror(titulo,mensaje)
                
                
            else: 
                 titulo="Error con el dato ingresado"
                 mensaje=f"La orden con número {numero_orden} ya fue dada de alta o no existe"
                 messagebox.showerror(titulo,mensaje) 
                 
         else: 
             titulo="Dato no valido como número de Orden"
             mensaje="El dato ingresado como número de orden no es un dato válido"
             messagebox.showerror(titulo,mensaje) 
        

    def verifica_tecla(self,event):
         super().verifica_tecla(event)
         if self.variable=='h' or self.variable=='H':
              self.habilitar_campos()
         if self.variable=='n' or self.variable=='N':
              self.habilitar_campos_busqueda_n_cuenta()

    def habilitar_campos_busqueda_n_cuenta(self):
        self.entry_numero_cuenta.config(state='normal')
        self.entry_numero_cuenta.focus()
        self.entry_numero_cuenta.bind ("<Return>",self.busqueda_numero_cuenta)

    def busqueda_numero_cuenta(self,event):
        self.numero_cuenta=procesar_dato_int(self.entry_numero_cuenta.get())
        if self.numero_cuenta:
            creditos=buscar_ordenes_creditos_bajas(self.orden_compra_organizacion,self.numero_cuenta)
            if creditos:
                titulo="Lista de ordenes de compras"  
                mensaje= f"El afiliado número {self.numero_cuenta} posee la siguiente lista de ordenes de compra por activarse: "+"\n"
                j=0
                for i in creditos:          
                                         auxiliar=creditos[j]
                                         auxiliar=int(auxiliar[0])
                                         mensaje=mensaje+ "La orden con número " + str(auxiliar)+"\n"
                                         j=j+1
                messagebox.showinfo(titulo,mensaje)
                self.desahabilitar_campos_busqueda_n_cuenta()
            else: 
             titulo="El afiliado no tiene ordenes de cuentas por activar "
             mensaje=f"El afiliado con número de cuenta igual a {self.numero_cuenta} no posee ordenes de compras por activarse"
             messagebox.showerror(titulo,mensaje)
        else: 
             titulo="Dato no valido como número de cuenta"
             mensaje="El dato ingresado como número de cuenta no es un dato válido"
             messagebox.showerror(titulo,mensaje) 


class FrameFechaAmep(FrameFecha):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_datos_usuario()
        self.desahabilitar_campos()
        self.desahabilitar_campos_busqueda_n_cuenta()

    def generar_alta_orden(self,event):
         self.orden_compra_organizacion="orden_compra_amep"
         self.organizacion="afiliado_amep"
         self.fecha_vencimiento_organizacion="fechas_vencimiento_amep"
         self.titulo_organizacion="A.M.E.P."
         super().generar_alta_orden(event)
    def  busqueda_nombre(self, event):
                   self.organizacion='afiliado_amep'
                   super().busqueda_nombre(event)
    def busqueda_numero_cuenta(self,event):
         self.orden_compra_organizacion="orden_compra_amep"
         super().busqueda_numero_cuenta(event)

class FrameFechaAdep(FrameFecha):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.campos_datos_usuario()
        self.desahabilitar_campos()
        self.desahabilitar_campos_busqueda_n_cuenta()

    def generar_alta_orden(self,event):
         self.orden_compra_organizacion="orden_compra_adep"
         self.organizacion="afiliado_adep"
         self.fecha_vencimiento_organizacion="fechas_vencimiento_adep"
         self.titulo_organizacion="A.D.E.P."
         super().generar_alta_orden(event)

    def  busqueda_nombre(self, event):
                   self.organizacion='afiliado_adep'
                   super().busqueda_nombre(event)

    def busqueda_numero_cuenta(self,event):
         self.orden_compra_organizacion="orden_compra_adep"
         super().busqueda_numero_cuenta(event)
