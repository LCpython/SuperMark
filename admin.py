import interfaz_user
from controlador_base_usuario import Con_Cliente    
from controlador_base_productos import control_BP


db = "C:\\Users\\LUCAS\\Desktop\\Proyecto de programacion\\base_datos(LC)\\base_datos0.db"

class admin(Con_Cliente):
    conexion=(db)
    def __init__(self,admin_user,admin_passw,):
        self.admin_user=admin_user
        self.admin_passw=admin_passw

class Producto():
    def __init__(self,menu_producto):
        self.menu_producto = menu_producto
    conexion=(db)
    conexion_consulta=(control_BP)
    def select_producto(self,menu_producto,id_producto,precio_producto,producto,main_producto):
        self.id_producto=id_producto
        self.menu_producto=menu_producto
        self.precio_producto=precio_producto
        self.producto=producto
        self.main_producto=main_producto
        menu_producto=print("-------------------SuperMark_v0.1---------------------\n"
                            "------------------------------------------------------\n"
                            "-------------------/Productos_Lista/------------------\n"
                            "------------------------------------------------------\n")

#Producto(menu_producto=True)
producto = Producto(menu_producto=True)



        
        
    
        