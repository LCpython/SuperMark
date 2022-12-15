from conector import Conexion_BD

print("------------------SuperMark_v0.1---------------------\n"
      "-----------------------------------------------------\n"
      "-------------------/Bienvenido!/---------------------\n"
      "-----------------------------------------------------\n"
      "       por favor, ingrese su datos para acceder      \n"
      "-----------------------------------------------------\n"
      "            que  tipo de usuario es usted?           \n"
      " administrador=0      usuario=1      uusario_venta=2 \n"
      )

user=int(input("tipo de usuario:"))
if user==0:
    print("--------bienvenido administrador-----------\n"
          "------ingrese su usario y contraseña:------\n")
    usuario=input("usuario: ")
    contraseña=input("contraseña: ")
    print("-------Inicio de sesion correcto!----------\n")
elif user==1:
    print("-------------bienvenido Usuario------------\n"
          "------ingrese su usario y contraseña:------\n")
    usuario=input("usuario: ")
    contraseña=input("contraseña: ")
    print("-------Inicio de sesion correcto!----------\n")
elif user==2:
    print("--------bienvenido Usuario_venta-----------\n"
          "------ingrese su usario y contraseña:------\n")
    usuario=input("usuario: ")
    contraseña=input("contraseña: ")  
    print("-------Inicio de sesion correcto!----------\n")

if usuario and contraseña ==True:
    pass
else:
    pass