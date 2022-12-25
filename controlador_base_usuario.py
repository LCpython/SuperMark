from conector import Conexion_BD

class Con_Cliente():
  def __init__(self):
    self.db="C:\\Users\\LUCAS\\Desktop\\Proyecto de programacion\\base_datos(LC)\\base_datos0.db"

  def alta_cliente(name_usuario,apellido_usuario,contraseña_usuario,DNI):
    conexion= Conexion_BD()
    conexion.consulta(f"INSERT INTO datos_usuario(name_usuario,apellido_usuario,contraseña_usuario,DNI) VALUES {name_usuario,apellido_usuario,contraseña_usuario,DNI};")
    conexion.commit()
    conexion.cerrar()

  def buscar_usuario(self,name_usuario):
    conexion= Conexion_BD()
    conexion.consulta(f"Select * from datos_usuario where usuario={name_usuario} ")
    conexion.commit()
    datos=conexion.cursor.fetchone()
    if datos != None:
      data = datos
    else:
      data= None
    #print(data)
    conexion.cerrar()
    return data

  def buscar_id(id_usuario):
    conexion= Conexion_BD()
    conexion.consulta(f"Select * from datos_usuario where id_cliente={id_usuario} ")
    conexion.commit()
    datos=conexion.cursor.fetchone()
    if datos != None:
      data = datos
    else:
      data= None
    #print(data)
    conexion.cerrar()
    return data

  def mostrar_datos():
    conexion= Conexion_BD()
    conexion.consulta(f"Select * from datos_usuario ")
    conexion.commit()
    datos=conexion.cursor.fetchall()
    if datos != None:
      data = datos
    else:
      data= None
    #print(data)
    conexion.cerrar()
    return data    

CC=Con_Cliente()
CC.mostrar_datos
