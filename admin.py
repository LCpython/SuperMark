<<<<<<< HEAD
from interfaz_user import Con_Cliente
from controlador_base_productos import control_BP


bd = "C:\\Users\\LUCAS\\Desktop\\Proyecto de programacion\\base_datos(LC)\\base_datos0.db"

import sqlite3
conn = sqlite3.connect("base_datos0.db")
cursor = conn.cursor()
class admin(Con_Cliente):
    conexion=(bd)
    def __init__(self,admin_user,admin_passw,):
        self.admin_user=admin_user
        self.admin_passw=admin_passw
class Producto():
    def __init__(self,menu_producto):
        self.menu_producto = menu_producto
    conexion=(bd)
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
class editar(Producto):
    def __init__(self,editar_producto,borrar_producto,agregar_producto):
        self.editar_producto=editar_producto
        self.borrar_producto=borrar_producto
        self.agregar_producto=agregar_producto
        

#Producto(menu_producto=True)
producto = Producto(menu_producto=True)

Inventario=(control_BP)
#if inventario==1:
#    conexion=db
#    consulta = conexion.consulta("SELECT * FROM base_producto")
#else:
#    conexion=db
#    consulta = conexion.consulta("SELECT * FROM base_producto")
     
class inventarios():
    conexion=bd
    conexion_consulta=(control_BP)
    
    def vender_Producto():
        global Inventario
        cantidad=int(input("Cantidad de venta : "))
        if cantidad > Inventario :
            print("No tienes productos suficientes")
        else:
            Inventario -= cantidad
    
    def Reabastecer():
        global Inventario
        cantidad=int(input("Cantidad: "))
        Inventario +=cantidad
    
    def ver_Inventario(self):
        cursor.execute
        conexion=bd
        consulta = conexion.consulta(f"SELECT * FROM producto")
        data = consulta.fetchall()
        conexion.cerrar()
        cursor.close()                 
         
        return data
    
    
    while True:
        try:
            print("""
            Menú
            [1] Vender producto
            [2] Reabastecer
            [3] Ver el inventario
            [4] Salir
            """)
            opcion = int(input("¿Qué deseas hacer?: "))
        except ValueError:
            print("Favor de ingresar una opción válida")
        else:
            if opcion < 1 or opcion > 4:
                print("{} no es una opción válida".format(opcion) )
                continue
            if opcion == 1:
                cursor.execute
                vender_Producto(+"SELECT * FROM 'producto'\n"
                                +"SELECT * FROM 'precio_producto'\n")
                cursor.close()  
            elif opcion == 2:
                    Reabastecer()
            elif opcion == 3:
                    cursor.execute
                    ver_Inventario(f"SELECT * FROM 'producto'")
                    cursor.close()  
            else:
                break
    print("Gracias por su compra")

def vender_Producto():
        global inventario
        print("ingrese la cantidad que desea vender")
        cantidad=int(input("Ingrese la cantida: "))
        if cantidad<=inventario:
                inventario=inventario-cantidad
                print ("Cantidad existente en el inventario: ",inventario)
        elif inventario==0 and cantidad>inventario:
            print ("Debe reabastecer el inventario")
            print()
        elif cantidad> inventario:
            print ("No tiene disponibilidad suficiente del producto")
            print()
 
def reabastecer():
    global inventario
    cantidad=int(input("Ingrese la cantidad que desea ingresar: "))
    inventario=inventario+cantidad
    print("La cantidad se ha ingresado con exito")
 
 
 
 

        
    

from interfaz_user import Con_Cliente
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



        
        
    

        