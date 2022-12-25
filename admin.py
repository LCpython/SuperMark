
from interfaz_user import Con_Cliente
from interfaz_user import Tipo_Usuario
from controlador_base_productos import control_BP
from tabulate import tabulate


bd = "C:\\Users\\LUCAS\\Desktop\\Proyecto de programacion\\base_datos(LC)\\base_datos0.db"

import sqlite3
conn = sqlite3.connect("base_datos0.db")
cursor = conn.cursor()

class admin(Con_Cliente):
    conexion=(bd)
    def __init__(self,admin_user,admin_passw,):
        self.admin_user=admin_user
        self.admin_passw=admin_passw
        self.conexion = sqlite3.connect("base_datos0.db")
        self.conexion_consulta=("SELECT * name_usuario=? WHERE base_usuario=?")
        
class Producto():
    def __init__(self,menu_producto):
        self.menu_producto = menu_producto
        self.conexion = sqlite3.connect("base_datos0.db")
        self.conexion_consulta=("SELECT * producto=? WHERE base_producto=?")
        
    def mostrar(self):  
        sql="SELECT * FROM producto where base_producto=? "
        self.cursor.execute(sql)
        items =self.cursor.fetchall()
        for i in items:
            print("producto", i[2])
        
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


        





class inventarios():
    conexion=bd
    conexion_consulta=(control_BP)
    
    def vender_Producto():
        print()
        Inventario=()
        cantidad=int(input("Cantidad de venta : "))
        if cantidad > Inventario :
            print("No tienes productos suficientes")
        else:
            Inventario -= cantidad
    
    
    def ver_Inventario(self):
        sql="SELECT * FROM producto where base_producto=? "
        self.cursor.execute(sql)
        items =self.cursor.fetchall()
        for i in items:
            print("producto", i[2])
        
    
    
    while True:
        try:
            print("""
            Menú
            [1] Vender producto
            [2] Ver el inventario
            [3] Salir
            """)
            opcion = int(input("¿Qué deseas hacer?: "))
        except ValueError:
            print("Favor de ingresar una opción válida")
        else:
            if opcion < 1 or opcion > 3:
                print("{} no es una opción válida".format(opcion) )
                continue
            if opcion == 1:
                vender_Producto()
            elif opcion == None:
                pass
            elif opcion == 2:
                ver_Inventario()
            else:
                break
    print("Gracias por su compra")

def vender_Producto():
        print()
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
    inventario
    cantidad=int(input("Ingrese la cantidad que desea ingresar: "))
    inventario=inventario+cantidad
    print("La cantidad se ha ingresado con exito")
    
    
    
    
    
    
    
    
    
    
#Inventario={
#    (1,'Leche entera 1Lt',125.25),
#    (2,'yogurt 1Lt',145.75),
#    (3,'queso chaqueño 1Lt',560.15),
#    (4,'queso ricota 1kg',900.55),
#    (5,'crema chantilli 1Lt',1050.25)
#} 
#table = tabulate(Inventario, headers='keys', tablefmt='grid')    
    



