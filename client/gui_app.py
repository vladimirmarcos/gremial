import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,Menu
from windows.creacion_frame_usuarios import FrameUserAmepp,FrameUserAdepp
from windows.creacion_frame_ordenes_compras import FrameOrdenAmepp
class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.menu = tk.Menu(parent)
        
        
        self.menu_afiliados= tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Afiliados", menu=self.menu_afiliados)
        self.menu_afiliados.add_command(label="Agregar afiliados Amepp",command=self.Crear_Afiliado_Amepp)
        self.menu_afiliados.add_command(label="Agregar afiliados Adepp",command=self.Crear_Afiliado_Adepp)
        parent.config(menu=self.menu)

        self.menu_ordenes_compra = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Ordenes de compra",menu=self.menu_ordenes_compra)
        self.menu_ordenes_compra.add_command(label="Crear orden de compra ADEPP",command="self.crear_orden_compra_amepp")
        self.menu_ordenes_compra.add_command(label="Crear orden de compra AMEPP",command=self.crear_orden_compra_amepp)
        parent.config(menu=self.menu)


        self._frame = None


    
    def Crear_Afiliado_Amepp(self):
         if self._frame is not None:
            self._frame.borrar()
            self._frame = None
         if self._frame is None:
            self._frame = FrameUserAmepp(self)

    def Crear_Afiliado_Adepp(self):
         if self._frame is not None:
            self._frame.borrar()
            self._frame = None
         if self._frame is None:
            self._frame = FrameUserAdepp(self)



    def crear_orden_compra_amepp(self):      
         if self._frame is not None:
            self._frame.borrar()
            self._frame = None
         if self._frame is None:
            self._frame = FrameOrdenAmepp(self)
           