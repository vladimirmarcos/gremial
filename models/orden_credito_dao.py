from .conexion_db import ConexionDB
import datetime
from Procesamiento import convertir_mes
from docxtpl import DocxTemplate
def consulta_ordenes_Compra(organizacion):
    conexion=ConexionDB()
    sql=f""" SELECT pagare,{organizacion} FROM orden_compra """
    conexion.cursor.execute(sql)
    datos=conexion.cursor.fetchone()
    conexion.cerrar()
    return datos

def carga_orden_compra(organizacion,orden_compra):
    conexion=ConexionDB()
    sql=f"""INSERT INTO '{organizacion}' (id_usuario,importe,dinero,porcentaje,cuota,mes,dias,comercio,orden_compra,pagare,estado) values ('{orden_compra.id_usuario}','{orden_compra.importe}','{orden_compra.dinero}','{orden_compra.porcentaje}','{orden_compra.cuota}','{orden_compra.mes}','{orden_compra.dias}','{orden_compra.comercio}','{orden_compra.orden_compra}','{orden_compra.pagare}','{orden_compra.estado}')"""
    conexion.cursor.execute(sql)
    conexion.cerrar()


def actualizar_valores_ordenes(organizacion,valor1,pagare):
     
     conexion=ConexionDB()
     sql=f"""    update orden_compra set '{organizacion}'='{valor1}', pagare='{pagare}';    
                """
     conexion.cursor.execute(sql)
     conexion.cerrar()

def documento_orden_compra(Orden_compra,nombre,domicilio,dni,doc,ruta):
            modelo_blanco = DocxTemplate(doc)
            fecha_actual=datetime.datetime.now()
            fecha_dia=datetime.datetime.strftime(fecha_actual,'%d')
            fecha_mes=convertir_mes( int(datetime.datetime.strftime(fecha_actual,'%m')))
            ano=datetime.datetime.strftime(fecha_actual,'%Y')
            context = {'orden_compra': Orden_compra.orden_compra,
            'fecha_dia': fecha_dia,
            'pagare': Orden_compra.pagare,
            'fecha_mes': fecha_mes,
            'ano' : ano,           
            'nombre' : nombre ,
           'dni': dni,
           'domicilio': domicilio,
           'importe': Orden_compra.importe,
           'dinero': Orden_compra.dinero,
           'porcentaje': Orden_compra.porcentaje,
           'cuotas': Orden_compra.cuota,
           'mes': Orden_compra.mes,
           'días':Orden_compra.dias,
           'comercio':Orden_compra.comercio}
            modelo_blanco.render(context)
            nombre_archivo=ruta+nombre+"-"+str(Orden_compra.comercio)+"-"+fecha_dia+"-"+fecha_mes+"-"+ano+".docx"
            modelo_blanco.render(context)
            modelo_blanco.save(nombre_archivo)


def buscar_ordenes_creditos_bajas (organizacion,numero_cuenta):
    conexion=ConexionDB()   
   
    sql=f""" SELECT orden_compra from {organizacion} where id_usuario={numero_cuenta} and estado='baja'
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
    
def buscar_orden_compras(organizacion,orden_compra):
      conexion=ConexionDB()   
      sql=f""" SELECT id_orden_compra from {organizacion} where orden_compra={orden_compra} and estado='baja'
    """
      conexion.cursor.execute(sql)
      auxiliar=conexion.cursor.fetchone()
      conexion.cerrar()
      if auxiliar:
            auxiliar=list(auxiliar)
            auxiliar=auxiliar[0]
            return auxiliar
      else:
            
            return None

def buscar_informacion_orden(organizacion,id_orden):
      conexion=ConexionDB()   
      
      sql=f""" SELECT id_usuario,dinero,porcentaje,mes,cuota from {organizacion} where id_orden_compra={id_orden}
    """
      conexion.cursor.execute(sql)
      auxiliar=conexion.cursor.fetchone()
      conexion.cerrar()
      if auxiliar:
            auxiliar=list(auxiliar)
            
            return auxiliar
      else:
            
            return None

def guardar_datos_fechas(fecha_vencimiento_organizacion,fecha,cuota,estado,cuenta,orden_compra,total):
   
    lista_fechas=[]
    fecha_actual=datetime.datetime.strptime(fecha, "%m/%d/%y")
    dia_delta=datetime.timedelta(days=30)
    proxima=fecha_actual+dia_delta
    proxima_str=datetime.datetime.strftime(proxima,"%Y%m%d")
    conexion=ConexionDB()
    sql=f"""INSERT INTO {fecha_vencimiento_organizacion} (fecha,total,estado,cuenta,orden_compra)
        VALUES ('{proxima_str}','{total}','{estado}','{cuenta}','{orden_compra}')
    
        """
    conexion.cursor.execute(sql)
    lista_fechas.append(proxima_str)
    for i in range (cuota-1): 
       proxima=proxima+dia_delta
       proxima_str=datetime.datetime.strftime(proxima,"%Y%m%d")
       sql=f"""INSERT INTO {fecha_vencimiento_organizacion} (fecha,total,estado,cuenta,orden_compra)
        VALUES ('{proxima_str}','{total}','{estado}','{cuenta}','{orden_compra}')
    
        """
       conexion.cursor.execute(sql)
       lista_fechas.append(proxima_str)
    conexion.cerrar()
    return lista_fechas

def  actualizar_estado_orden(orden_compra,organizacion,estado):
       conexion=ConexionDB()   
       sql=f""" update '{organizacion}' set estado='{estado}' WHERE id_orden_compra='{orden_compra}'
    """
       conexion.cursor.execute(sql)
       auxiliar=conexion.cursor.fetchone()
       conexion.cerrar()
      