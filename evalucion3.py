import os

menu = """
1. Registrar vehiculo
2. Listar vehiculo
3. imprimir vehiculo
4. salir
"""
reporte = []
marcas = ["toyota","ford","chevrolet"]

planilla =["""                                 LISTA VEHICULOS
----------------------------------------------------------------------------------------------------------
  MARCA               AÑO    KILOMETRAJE           COST_REP          IMP_SERV          COSTO TOTAL                                                                  
----------------------------------------------------------------------------------------------------------          
"""]



def registrar():
    while True:
        try:

            marca = input(f"ingrese marca de vehiculo{marcas}: ").strip().lower()
            año = int(input("ingrese año de vehiculo: "))
            kil = int(input("ingrese kilometrajer de auto: "))
            presu = int(input("ingrese costo de reparacion estimada: "))
            imp_serv = round(presu * 0.08)
            costo_total = round(presu + imp_serv)
            if marca and marcas and año and kil and presu >0:
                reporte.append([marca,año,kil,presu,imp_serv,costo_total])
                input("Registrado con exito")
                break
            else:
                input("error")
        except Exception as e:
                input(f"error de excepcion {str(e)}")


def listar():
    salida = planilla
    for t in reporte:
        salida += f"{t[0]:20s}"
        salida += f"{t[1]:5d}"
        salida += f"{t[2]:5d}"
        salida += f"{t[3]:5d}"
        salida += f"{t[4]:5d}"
        salida += f"{t[5]:5d}"
        salida += f"{t[6]:5d}"
        salida += "\n"
    return salida

def listartodos(marcas):
    salida = planilla
    if marcas == t[0]:
      for t in reporte:
        salida += f"{t[0]:20s}"
        salida += f"{t[1]:5d}"
        salida += f"{t[2]:5d}"
        salida += f"{t[3]:5d}"
        salida += f"{t[4]:5d}"
        salida += f"{t[5]:5d}"
        salida += f"{t[6]:5d}"
        salida += "\n"
    return salida

def imprimir():
    x = input(f"cargo a imprimir [todos/{marcas}]: ").strip().lower()
    if x == "todos":
        with open("listadoautos.txt","w") as archivo:
            archivo.write(listar())
    elif x in marcas:
        with open("listadoautos.txt","w") as archivo:
            archivo.write(listartodos(x))
    else:
        input("archivo no encontrad")
    

while True:
    try:
        opc = input(menu)
        if opc == "4":
            break
        elif opc == "1":
            registrar()
        elif opc == "2":
           listar()
        elif opc == "3":
            imprimir()
        else:
            input("error de opcion")
    except Exception as e:
        input(f"excepcion al menu {str(e)}")