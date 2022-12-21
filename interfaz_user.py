from conector import Conexion_BD
from controlador_base_usuario import Conexion_BD
import os
lp = lambda: os.system("cls")

class menu():
      def __init__(self,main_menu):
            conexion=Conexion_BD("base_datos0.db")
            
            self.main_menu=main_menu
            main_menu= print("------------------SuperMark_v0.1---------------------\n"
                        "-----------------------------------------------------\n"
                        "-------------------/Bienvenido!/---------------------\n"
                        "-----------------------------------------------------\n"
                        "       por favor, ingrese su datos para acceder      \n"
                        "-----------------------------------------------------\n"
                        "            que  tipo de usuario es usted?           \n"
                        " administrador=0      usuario=1      uusario_venta=2 \n")
class Tipo_Usuario(menu):
 def __init__(self,tipo_user,id_usuario=1):
  self.id_usuario=id_usuario
  self.tipo_user=tipo_user  

  tipo_user=int(input("tipo de usuario:"))
  
  if tipo_user==0:
            print("--------bienvenido administrador-----------\n"
                  "------ingrese su usario y contraseña:------\n")
            usuario=input("usuario: ")
            contraseña=input("contraseña: ")
            if usuario == "hernan fresco" and contraseña=="fresco123":
                  print("-------Inicio de sesion correcto!----------\n")
            else:
                  print("-------Usuario o contraseña incorrectos------")

  elif tipo_user==1:
            print("-------------bienvenido Usuario------------\n"
                  "------ingrese su usario y contraseña:------\n")
            usuario=input("usuario: ")
            contraseña=input("contraseña: ")
            if usuario == "lucas cordoba" and contraseña=="lucas123":
                  print("-------Inicio de sesion correcto!----------\n")
            else:
                  print("-------Usuario o contraseña incorrectos------")
            print("-------Inicio de sesion correcto!----------\n")
            
            
  elif tipo_user==2:
            print("--------bienvenido Usuario_venta-----------\n"
                  "------ingrese su usario y contraseña:------\n")
            usuario=input("usuario: ")
            contraseña=input("contraseña: ")
            if usuario == "cordoba" and contraseña=="alt123":
                  print("-------Inicio de sesion correcto!----------\n")
            else:
                  print("-------Usuario o contraseña incorrectos------")
  else:
        print("'UserError', este tipo de usuario no existe")
        

menu(main_menu=True)
tipo_Usuario=Tipo_Usuario(2)





      
