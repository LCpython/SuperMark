from conector import Conexion_BD

class control_BP():
    def __init__(self):
        self.__bd="C:\\Users\\LUCAS\\Desktop\\Proyecto de programacion\\base_datos(LC)\\base_datos0.db"
        self.conexion=Conexion_BD(self.__bd)


    def select(self):
        conexion=Conexion_BD(self.__bd)
        
        consulta = conexion.consulta("SELECT * FROM producto")
        data = consulta.fetchall()
        conexion.cerrar()
        return data

    def select(self,id):
        conexion=Conexion_BD(self.__bd)
        consulta = conexion.consulta(f"SELECT * FROM producto WHERE id_producto= {id}")
        if consulta != None:
            data = consulta.fetchone()
        else:
         data= None
        print(data)
        conexion.cerrar()
        return data

    def insert(self,precio):
        conexion=Conexion_BD(self.__bd)
        conexion.consulta(f"INSERT INTO producto( producto_precio) VALUES {precio};")
        conexion.cerrar()
        
    
        
    def update_precio(self,id,precio):
        conexion=Conexion_BD(self.__bd)
        conexion.consulta(f"UPDATE producto SET producto_precio= {precio} WHERE id_producto= {id}")
        conexion.cerrar()
    
    def eliminar(self,id):
        conexion=Conexion_BD(self.__bd)
        conexion.consulta(f"DELETE FROM producto WHERE id_producto= {id}")
        conexion.cerrar()

    def mostrar(self):  
        sql="SELECT * FROM producto"
        self.cursor.execute(sql)
        items =self.cursor.fetchall()
        for i in items:
            print('base_producto', i[2])

b_p=control_BP()
b_p.mostrar