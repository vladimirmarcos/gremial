class Afiliados:
     def __init__(self,nombre,dni,domicilio,mail,telefono,condicion):
        self.afiliado_id=None
        self.nombre=nombre
        self.dni=dni
        self.domicilio=domicilio
        self.mail=mail
        self.telefono=telefono
        self.condicion=condicion   
     def __str__(self):
        return f'Creditos[{self.nombre},{self.dni},{self.domicilio},{self.mail},{self.telefono},{self.condicion}]'
     

class OrdenCompra:
     def __init__(self,id_usuario,importe,dinero,porcentaje,cuota,mes,dias,comercio,orden_compra,pagare,estado):
        self.id_orden_compra=None
        self.id_usuario=id_usuario
        self.importe=importe
        self.dinero=dinero
        self.porcentaje=porcentaje
        self.cuota=cuota
        self.mes=mes
        self.dias=dias
        self.comercio=comercio
        self.orden_compra=orden_compra
        self.pagare=pagare
        self.estado=estado    
     def __str__(self):
        return f'Creditos[{self.id_usuario},{self.importe},{self.dinero},{self.porcentaje},{self.cuota},{self.mes},{self.dias},{self.comercio},{self.orden_compra},{self.pagare},{self.estado}]'
     
class Fechas_Vencimiento:
    def __init__(self,fecha,total,estado,cuenta,orden_compra):
        self.id_fecha=None
        self.fecha=fecha
        self.total=total
        self.estado=estado
        self.cuenta=cuenta
        self.orden_compra=orden_compra
    def __str__(self):
        return f'Creditos[{self.fecha},{self.total},{self.estado},{self.cuenta},{self.orden_compra}]'