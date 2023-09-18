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

def buscar_nombre (nombre,organizacion):
    conexion=ConexionDB()   
    if nombre !="0":
        sql=f""" SELECT nombre,dni,afiliado_id from {organizacion} WHERE nombre like '%{nombre}%'
    """
        conexion.cursor.execute(sql)
        auxiliar=conexion.cursor.fetchall()
        usuarios_encontrados=[]
        conexion.cerrar()
        if auxiliar:
            usuarios_encontrados=[list(x) for x in auxiliar]   
            return usuarios_encontrados
        else:
            return None
    else:
          sql=f""" SELECT nombre,dni from '{organizacion}'
    """
          conexion.cursor.execute(sql)
          auxiliar=conexion.cursor.fetchall()
          usuarios_encontrados=[]
          conexion.cerrar()
          if auxiliar:
            usuarios_encontrados=[list(x) for x in auxiliar]   
            return usuarios_encontrados
          else:
            return None
          
def informacion_editar(organizacion,dni):
    conexion=ConexionDB()   
    
    sql=f""" SELECT nombre,dni,domicilio,mail,telefono,condicion from '{organizacion}' WHERE dni='{dni}'
    """
    conexion.cursor.execute(sql)
    informacion_encontrada=conexion.cursor.fetchone()
   
    conexion.cerrar()
    informacion_encontrada=list(informacion_encontrada)
    return informacion_encontrada

def informacion_editada(organizacion,campo,valor,dni):
    conexion=ConexionDB()   
    
    sql=f""" update '{organizacion}' set '{campo}'='{valor}' WHERE dni='{dni}'
    """
    conexion.cursor.execute(sql)
    conexion.cerrar()
    
def buscar_id(organizacion,id_afiliado):
     conexion=ConexionDB()
     sql=f""" SELECT nombre,dni from '{organizacion}' where afiliado_id={id_afiliado}
    """
     conexion.cursor.execute(sql)
     auxiliar=conexion.cursor.fetchone()
     conexion.cerrar()
     if auxiliar:
            auxiliar=list (auxiliar)
            
            return auxiliar
     else:
        
            return None