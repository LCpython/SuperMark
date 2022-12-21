import sqlite3 as sql

class Conexion_BD():
    def __init__(self,bd):#bd es el nombre de la base de datos
        self.conexion = sql.connect(bd)
        self.cursor = self.conexion.cursor()


    def consulta(self, consulta):
        data=None
        if consulta.upper().startswith("SELECT"):
            data= self.cursor.execute(f"SELECT nombre,")
        else:
            self.cursor.execute(consulta)
            self.commit()
        return data
    
    def commit(self):
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()   
        