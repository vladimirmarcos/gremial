import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Procesamiento import procesar_dato_int,procesar_dato_str,procesar_dato_float
from models.afiliados_dao import buscar_dni,informacion_editar
from models.models import OrdenCompra
from models.orden_credito_dao import consulta_ordenes_Compra
from windows.creacion_frame_busqueda import FrameBusqueda
from models.orden_credito_dao import carga_orden_compra
from models.orden_credito_dao import actualizar_valores_ordenes,documento_orden_compra


class FrameOrdenCompra(FrameBusqueda):
    def __init__(self, parent):
        super().__init__(parent)
        self.campos_datos_ordenes()
        self.desahabilitar_campos()
        self.desahabilitar_busqueda_nombre()
        self.habilitar_opciones()
        
        
    def campos_datos_ordenes(self):
       #label de campos
        self.label_dni=tk.Label(self,text='DNI')
        self.label_dni.config(font=('Arial',12,'bold'))
        self.label_dni.grid(row=1,column=0,padx=10,pady=10)

        self.label_Importe=tk.Label(self,text='Importe en texto')
        self.label_Importe.config(font=('Arial',12,'bold'))
        self.label_Importe.grid(row=2,column=0,padx=10,pady=10)  
    
        self.label_dinero=tk.Label(self,text='Importe en número')
        self.label_dinero.config(font=('Arial',12,'bold'))
        self.label_dinero.grid(row=3,column=0,padx=10,pady=10)

        self.label_porcentaje=tk.Label(self,text=' Porcentaje de descuento\n (en caso de no tener colocar 0)')
        self.label_porcentaje.config(font=('Arial',12,'bold'))
        self.label_porcentaje.grid(row=4,column=0,padx=10,pady=10)

        

        self.label_cuota=tk.Label(self,text='cuotas')
        self.label_cuota.config(font=('Arial',12,'bold'))
        self.label_cuota.grid(row=5,column=0,padx=10,pady=10)

        self.label_mes=tk.Label(self,text='Mes')
        self.label_mes.config(font=('Arial',12,'bold'))
        self.label_mes.grid(row=6,column=0,padx=10,pady=10)

        self.label_dias=tk.Label(self,text='Días de vigencia')
        self.label_dias.config(font=('Arial',12,'bold'))
        self.label_dias.grid(row=7,column=0,padx=10,pady=10)

        self.label_comercio=tk.Label(self,text='Comercio')
        self.label_comercio.config(font=('Arial',12,'bold'))
        self.label_comercio.grid(row=8,column=0,padx=10,pady=10)

        #Entrys de cada Campo
        self.mi_dni=tk.StringVar()
        self.entry_dni=tk.Entry(self,textvariable=self.mi_dni)
        self.entry_dni.config(width=50,font=('Arial',12))
        self.entry_dni.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.mi_importe=tk.StringVar()
        self.entry_importe=tk.Entry(self,textvariable=self.mi_importe)
        self.entry_importe.config(width=50,font=('Arial',12))
        self.entry_importe.grid(row=2,column=1,padx=10,pady=10,columnspan=2)
        
        self.mi_dinero=tk.StringVar()
        self.entry_dinero=tk.Entry(self,textvariable=self.mi_dinero)
        self.entry_dinero.config(width=50,font=('Arial',12))
        self.entry_dinero.grid(row=3,column=1,padx=10,pady=10,columnspan=2)


        self.mi_porcentaje=tk.StringVar()
        self.entry_porcentaje=tk.Entry(self,textvariable=self.mi_porcentaje)
        self.entry_porcentaje.config(width=50,font=('Arial',12))
        self.entry_porcentaje.grid(row=4,column=1,padx=10,pady=10,columnspan=2) 

        self.mi_cuotas=ttk.Combobox(self,
                                      state="readonly",
                                      values=["1", "2", "3", "4", "5", "6", "7", "8", "9",
                                              "10", "11", "12"])
        self.mi_cuotas.config(width=50, height=200,font=('Arial',12))
        self.mi_cuotas.grid(row=5,column=1,padx=10,pady=10,columnspan=2) 

        self.mi_mes=ttk.Combobox(self,
                                      state="readonly",
                                      values=["Enero", "Febrero", "Marzo", "Abril",
                                              "Mayo", "Junio", "Julio", "Agosto",
                                              "Septiembre","Octubre", "Noviembre", "Diciembre"])
        self.mi_mes.config(width=50, height=200,font=('Arial',12))
        self.mi_mes.grid(row=6,column=1,padx=10,pady=10,columnspan=2) 

        self.mi_dias=tk.StringVar()
        self.entry_dias=tk.Entry(self,textvariable=self.mi_dias)
        self.entry_dias.config(width=50,font=('Arial',12))
        self.entry_dias.grid(row=7,column=1,padx=10,pady=10,columnspan=2)
        
        self.mi_comercio=tk.StringVar()
        self.entry_comercio=tk.Entry(self,textvariable=self.mi_comercio)
        self.entry_comercio.config(width=50,font=('Arial',12))
        self.entry_comercio.grid(row=8,column=1,padx=10,pady=10,columnspan=2)

   
        self._frame = None

    def habilitar_campos(self):
            
            self.entry_dni.config(state='normal')
            self.entry_importe.config(state='normal')
            self.entry_dinero.config(state='normal')
            self.entry_porcentaje.config(state='normal')
            self.mi_cuotas.config(state='normal')
            self.mi_mes.config(state='normal')
            self.entry_dias.config(state='normal')
            self.entry_comercio.config(state='normal')


            self.entry_dni.bind ("<Return>",self.verificar_dato)
            self.entry_importe.bind ("<Return>",self.verificar_dato)
            self.entry_dinero.bind ("<Return>",self.verificar_dato)
            self.entry_porcentaje.bind ("<Return>",self.verificar_dato)
            self.entry_dias.bind ("<Return>",self.verificar_dato)
            self.entry_comercio.bind ("<Return>",self.verificar_dato)
            self.entry_dni.focus()



    def desahabilitar_campos(self):
            self.mi_dni.set('')
            self.mi_importe.set('')
            self.mi_dinero.set('')
            self.mi_porcentaje.set('')
            self.mi_cuotas.set('1')
            self.mi_mes.set('Enero')
            self.mi_dias.set('')
            self.mi_comercio.set('')
            self.mi_opciones.set('')
        
            self.entry_dni.config(state='disabled')
            self.entry_importe.config(state='disabled')
            self.entry_dinero.config(state='disabled')
            self.entry_porcentaje.config(state='disabled')
            self.mi_cuotas.config(state='disabled')
            self.mi_mes.config(state='disabled')
            self.entry_dias.config(state='disabled')
            self.entry_comercio.config(state='disabled')
            self.entry_opciones.focus()
        

    def verifica_tecla(self,event):
         super().verifica_tecla(event)
         if self.variable=='h' or self.variable=='H':
              self.habilitar_campos()
    
    def borrar(self):
        self.pack_forget()
        self.destroy()
    def verificar_dato(self,event):
         
          dni=procesar_dato_int(self.mi_dni.get())
          if dni:
              id_usuario=buscar_dni(self.organizacion,dni)
              
              if id_usuario==None:
                  titulo=" error al registrar Orden de compra"
                  mensaje= "el dni no esta registrado en Amepp" 
                  messagebox.showerror(titulo,mensaje)
              else: 
                   id_usuario=list(id_usuario)
                   id_usuario=id_usuario[0]
                   importe=procesar_dato_str(self.mi_importe.get())
                   dinero=procesar_dato_int(self.mi_dinero.get())
                   porcentaje=procesar_dato_float(self.mi_porcentaje.get())
                   cuota=procesar_dato_int(self.mi_cuotas.get())
                   mes=procesar_dato_str(self.mi_mes.get())
                   dias=procesar_dato_int(self.mi_dias.get())
                   comercio=procesar_dato_str(self.mi_comercio.get())
                   if importe=="" or dinero==None or porcentaje==None or cuota==None or mes=="" or dias==None or comercio=="":
                       titulo=" Error al registrar la orden de compra"
                       mensaje= "Agunos datos ingresados son erroneos o los campos estan vacíos" 
                       messagebox.showerror(titulo,mensaje)
                   else: 
                         datos=consulta_ordenes_Compra(self.organizacion_orden)
                         if datos:
                            datos=list(datos)
                            pagare=datos[0]
                            orden_compra=datos[1]
                            Orden_Compra=OrdenCompra(
                            id_usuario,
                            importe,
                            dinero,
                            porcentaje,
                            cuota,
                            mes,
                            dias,
                            comercio,
                            orden_compra,
                            pagare,
                            estado="baja"

                         )
                            
                            informacion_restante=informacion_editar(self.organizacion,dni)
                            nombre=informacion_restante[0]
                            domicilio=informacion_restante[2]
                            titulo=f"Generación de orden  {self.organizacion_titulo}"
                            mensaje=f"¿Esta seguro de generar la orden de compra al afiliado {nombre}, por el monto {Orden_Compra.importe} por las cuotas {Orden_Compra.cuota}, con porcentaje de descuento de {Orden_Compra.porcentaje}% en el comercio {Orden_Compra.comercio} valido solo por {Orden_Compra.dias} días?"
                            respuesta = messagebox.askyesno(titulo, mensaje)
                            if respuesta:
                                carga_orden_compra(self.orden_compra_tabla,Orden_Compra)
                                self.pagare=pagare+1
                                self.nuevo_valor=orden_compra+1
                                actualizar_valores_ordenes(self.organizacion_orden,self.nuevo_valor,self.pagare)
                            
                                documento_orden_compra(Orden_Compra,nombre,domicilio,dni,self.doc,self.ruta)
                                titulo="Se cargo exitosamente "
                                mensaje= "LA orden se cargo exitosamente" 
                                messagebox.showinfo(titulo,mensaje)
                                self.desahabilitar_campos()
                         else:
                             titulo="Error al generar la orden de compra"
                             mensaje= "No se pudo acceder a la base, intente más tarde" 
                             messagebox.showerror(titulo,mensaje)

                       
          else:
              titulo=" error al registrar la orden de compra"
              mensaje= "El dato ingresado como dni no es válido" 
              messagebox.showerror(titulo,mensaje)
          
class FrameOrdenAmepp(FrameOrdenCompra):
         def __init__(self,parent):
            super().__init__(parent)
            self.pack(fill=tk.BOTH, expand=tk.YES)
            
         def verificar_dato(self,event):
            self.organizacion='afiliado_amep'
            self.organizacion_orden='orden_amep'
            self.organizacion_titulo='A.M.E.P.'
            self.orden_compra_tabla='orden_compra_amep'
            self.doc="OrdendeCompraenBlancoAMEPPMODELO.docx"
            self.ruta="orden_compra_amepp/orden-de-compra-de-"
            super().verificar_dato(event)
         

class FrameOrdenAdepp(FrameOrdenCompra):
         def __init__(self,parent):
            super().__init__(parent)
            self.pack(fill=tk.BOTH, expand=tk.YES)
            
         def verificar_dato(self,event):
            self.organizacion='afiliado_adep'
            self.organizacion_orden='orden_adep'
            self.organizacion_titulo='A.D.E.P.'
            self.orden_compra_tabla='orden_compra_adep'
            self.doc="OrdendeCompraenBlancoADEPPMODELO.docx"
            self.ruta="orden_compra_adepp/orden-de-compra-de-"
            super().verificar_dato(event)