import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,Menu
from windows.creacion_frame_usuarios import FrameUserAmepp,FrameUserAdepp
from windows.creacion_frame_ordenes_compras import FrameOrdenAmepp,FrameOrdenAdepp
from windows.creacion_frame_editar_afiliados import FrameEditarAmeppUser,FrameEditarAdeppUser
from windows.creacion_frame_altas_orden_compras import FrameFechaAmep,FrameFechaAdep
class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.menu = tk.Menu(parent)
        
        
        self.menu_afiliados= tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Afiliados", menu=self.menu_afiliados)
        self.menu_afiliados.add_command(label="Agregar afiliados Amepp",command=self.Crear_Afiliado_Amepp)
        self.menu_afiliados.add_command(label="Agregar afiliados Adepp",command=self.Crear_Afiliado_Adepp)
        self.menu_afiliados.add_command(label="Editar Afiliado AMEP",command=self.editar_afiliado_amep)
        self.menu_afiliados.add_command(label="Editar Afiliado ADEP",command=self.editar_afiliado_adep)
        parent.config(menu=self.menu)

        self.menu_ordenes_compra = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Ordenes de compra",menu=self.menu_ordenes_compra)
        self.menu_ordenes_compra.add_command(label="Crear orden de compra ADEPP",command=self.crear_orden_compra_adepp)
        self.menu_ordenes_compra.add_command(label="Crear orden de compra AMEPP",command=self.crear_orden_compra_amepp)
        self.menu_ordenes_compra.add_command(label="Alta orden A.M.E.P",command=self.alta_orden_compra_amepp)
        self.menu_ordenes_compra.add_command(label="Alta orden A.D.E.P",command=self.alta_orden_compra_adepp)
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
           
    def editar_afiliado_adep(self):      
         if self._frame is not None:
            self._frame.borrar()
            self._frame = None
         if self._frame is None:
            self._frame = FrameEditarAdeppUser(self)

    def editar_afiliado_amep(self):      
         if self._frame is not None:
            self._frame.borrar()
            self._frame = None
         if self._frame is None:
            self._frame = FrameEditarAmeppUser(self)

    def crear_orden_compra_amepp(self):      
         if self._frame is not None:
            self._frame.borrar()
            self._frame = None
         if self._frame is None:
            self._frame = FrameOrdenAmepp(self)
    
    def crear_orden_compra_adepp(self):      
         if self._frame is not None:
            self._frame.borrar()
            self._frame = None
         if self._frame is None:
            self._frame = FrameOrdenAdepp(self)

    def alta_orden_compra_amepp(self):      
         if self._frame is not None:
            self._frame.borrar()
            self._frame = None
         if self._frame is None:
            self._frame = FrameFechaAmep(self)

    def alta_orden_compra_adepp(self):      
         if self._frame is not None:
            self._frame.borrar()
            self._frame = None
         if self._frame is None:
            self._frame = FrameFechaAdep(self)


    