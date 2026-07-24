from datos import *

def login(usuario,password):
    for i in range(3):
        ingresa_usuario = input("Ingrese su usuario: ")
        ingresa_password = input("Ingrese clave: ")

        if usuario==ingresa_usuario and password==ingresa_password:
            print("acceso correcto")
            return True
            break#(este break romple el ciclo for que pide la contraseña, se ubica en la respuesta verdadera de ese if)
            
        else: 
            print(f" ⚠️  Usuario y/o ontraseña incorrecta, le quedan {2-i} intentos")
    else:
        print(" ❌ Ha excedido el limite de intentos permitidos")

def menu():
    print(f"""
    ===========================================================
    😊 Bienvenido al sistema de gestión de inventario (FIFO)😊
            Inventarios Plus, su solución tecnológica.
    🔨🪚🪛        Ferrtería Maestro Chasquilla        🔨🪚🪛
    ===========================================================
    

    1.- Registrar compra al proveedor.
    2.- Registrar venta de mercaderia.
    3.- Registrar devolución al proveedor.
    4.- Registrar devolución de cliente.
    5.- Mostrar Stock de inventario.
    6.- Ajuste de inventario por mermas.
    7.- Salir del sistema.
    """)
    
def entrada_compras(herramienta,lote,cantidad,costo):
    if herramienta not in herramientas:    
        herramientas[herramienta]=[]  #agrego la herramienta al directorio principal(diccionario externo)   
        # Agregar elementos a la lista metodo append, variable.append(nuevo elemento)
        herramientas[herramienta].append({"lote":lote,"cantidad":cantidad,"costo":costo})
    else:
        herramientas[herramienta].append({"lote":lote,"cantidad":cantidad,"costo":costo})    
    
    print(herramientas)
    print(f"El costo de las mercaderías ascienden a $ {cantidad*costo}")
    print(f"Se ha registrado la entrada de {herramienta} al inventario")
    return

def existencia(herramienta):
    if herramienta not in herramientas:
        print(f"no tenemos {herramienta} en el inventario, contacte al vendedor")    
        return False
    
    return True


def validar_venta(herramienta,cantidad_vendida):
    
    cantidad_total = 0
    for lote in herramientas[herramienta]:
        cantidad_total += lote["cantidad"]
    if cantidad_total >= cantidad_vendida:
            return True
    
    print(f"No tenemos suficientes unidades de {herramienta}, para completar el pedido, contacte al vendedor")    
    return False    
            
def descontar_fifo_venta(herramienta,cantidad_vendida):
    cantidad_pendiente = cantidad_vendida
    for lote in herramientas[herramienta]:
        
        if lote["cantidad"] >= cantidad_pendiente:
            saldo = lote["cantidad"] - cantidad_pendiente
            lote["cantidad"] =saldo
            break
        else:
            cantidad_pendiente -= lote["cantidad"]
            lote["cantidad"] = 0
            
def mostrar_listado_herrramientas():
    print("herramientas en stock")
    for herramienta in herramientas:
        print(herramienta)
            
            

def mostrar_inventario(herramienta):

    cantidad_acumulada = 0
    costo_acumulado = 0
    print(f"Kardex de {herramienta}")

    print("-------------------------------------------------------------------------------------------------------------------------")
    print(f" {'lote':^20}{'cantidad':^20}{'total':^20} {'costo un.':^20} {'costo/lote':^20}{'costo total':^20}") #:>20, formato de alineación, el numero indica la cantidad de estación que se va a reservar para el elemento, >izquierda, <derecha, ^centrado.
    print("-------------------------------------------------------------------------------------------------------------------------")#va entre (')si es un texto, seguido del formato y entre llaves, su es una variable, usa las llaves que ya usa la variable, junto con el formato 
    for lote in herramientas[herramienta]:
        costo_lote = lote["cantidad"]*lote["costo"]
        cantidad_acumulada += lote["cantidad"]
        costo_acumulado += costo_lote
        
        
        print(f"{lote['lote']:^20} {lote['cantidad']:^20}{cantidad_acumulada:^20}{lote['costo']:^20}{costo_lote:^20}{costo_acumulado:^20}")
    print("-------------------------------------------------------------------------------------------------------------------------")    
        #la funcion llevara un input para herramietas, y sera el parametro
    print(f"Total de unidades {cantidad_acumulada}")    
    print(f"Costo total del inventario $ {costo_acumulado}")    
    print("--------------------------------------------------")  
    
