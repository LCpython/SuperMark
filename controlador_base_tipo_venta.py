from conector import Conexion_BD

class control_BTV():
    def __init__(self):
        self.__bd="C:\\Users\\LUCAS\\Desktop\\Proyecto de programacion\\base_datos(LC)\\base_datos0.db"
    
    
    def productos(self,id_producto,producto,precio_producto):
     conexion= Conexion_BD()
     conexion.consulta(f"INSERT INTO Tabla_Prod() VALUES {producto,precio_producto,id_producto};")
     conexion.commit()
     conexion.cerrar()


    def select(self):
        conexion=Conexion_BD(self.__bd)
        
        consulta = conexion.consulta("SELECT * FROM name_usuario")
        data = consulta.fetchall()
        conexion.cerrar()
        return data

    def select2(self,id):
        conexion=Conexion_BD(self.__bd)
        consulta = conexion.consulta(f"SELECT * FROM name_usuario WHERE id_usuario= {id}")
        if consulta != None:
            data = consulta.fetchone()
        else:
         data= None
        print(data)
        conexion.cerrar()
        return data
    
    def eliminar(self,id):
        conexion=Conexion_BD(self.__bd)
        conexion.consulta(f"DELETE FROM name usuario WHERE id_usuario= {id}")
        conexion.cerrar()
        
TV=control_BTV
TV.select2 