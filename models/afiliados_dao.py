from .conexion_db import ConexionDB
from tkinter import messagebox

def buscar_dni(organizacion,dni):
    conexion=ConexionDB()   
    
    sql=f""" SELECT afiliado_id from '{organizacion}' WHERE dni='{dni}'
    """
    conexion.cursor.execute(sql)
    dni_encontrado=conexion.cursor.fetchone()
   
    conexion.cerrar()
    return dni_encontrado

def cargar_afiliado(organizacion,Afiliado):
    conexion=ConexionDB()
    sql=f"""INSERT INTO '{organizacion}' (nombre,dni,domicilio,mail,telefono,condicion) values ('{Afiliado.nombre}','{Afiliado.dni}','{Afiliado.domicilio}','{Afiliado.mail}','{Afiliado.telefono}','{Afiliado.condicion}')"""

    conexion.cursor.execute(sql)
    conexion.cerrar()