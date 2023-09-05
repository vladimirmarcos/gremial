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