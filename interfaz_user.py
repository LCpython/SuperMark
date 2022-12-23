from conector import Conexion_BD 
from controlador_base_usuario import Con_Cliente    
import os

db = "C:\\Users\\LUCAS\\Desktop\\Proyecto de programacion\\base_datos(LC)\\base_datos0.db"
lp = lambda: os.system("cls")

class Menu(Con_Cliente):
    def __init__(self, main_menu):
        conexion = Conexion_BD("base_datos0.db")
        self.main_menu = main_menu
        main_menu = print("------------------SuperMark_v0.1---------------------\n"
                         "-----------------------------------------------------\n"
                         "-------------------/Bienvenido!/---------------------\n"
                         "-----------------------------------------------------\n"
                         "       por favor, ingrese su datos para acceder      \n"
                         "-----------------------------------------------------\n"
                         "            que  tipo de usuario es usted?           \n"
                         " administrador=0      usuario=1      uusario_venta=2 \n")
menu = Menu(main_menu=True)

class Tipo_Usuario(Menu):
    def __init__(self, tipo_user, id_usuario=4):
        self.id_usuario = id_usuario
        self.tipo_user = tipo_user

        tipo_user = int(input("tipo de usuario:"))
        conexion = Conexion_BD(db)
        if tipo_user == 0:
            tipo_Usuario="admin"
        elif tipo_user == 1:
            tipo_Usuario="usuario"
        elif tipo_user == 2:
            tipo_Usuario="venta"
        else:
            print("'UserError', este tipo de usuario no existe")

tipo_Usuario = Tipo_Usuario(2)

class Login(Menu):
    def __init__(self, inicio, name_usuario,apellido_usuario,contraseña_usuario):
        conexion = Conexion_BD(db)
        self.inicio = inicio
        self.name_usuario = name_usuario
        self.apellido_usuario=apellido_usuario
        self.contraseña_usuario=contraseña_usuario
        inicio=print("------------------SuperMark_v0.1---------------------\n"
                    "-----------------------------------------------------\n"
                    "-------------------/Bienvenido!/---------------------\n"
                    "-----------------------------------------------------\n"
                    "       por favor, ingrese su datos para acceder      \n")
        name_usuario=input("usuario:")
        apellido_usuario=input("apellido:")
        contraseña_usuario=input("contraseña:")
        conexion.commit()
        conexion.cerrar()
        
    def connected(self, Con_Cliente):
         self.Con_Cliente=Con_Cliente
         Login.connected(Con_Cliente)
         
         
            
Login(name_usuario="",contraseña_usuario="",apellido_usuario="",inicio=True)




