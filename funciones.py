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
        herramientas[herramienta]=[]  #agrego la herramienta al directorio principal   (diccionario externo)   
        # Agregar elementos a la lista metodo append, variable.append(nuevo elemento)
        herramientas[herramienta].append({"lote":lote,"cantidad":cantidad,"costo":costo})
    else:
        herramientas[herramienta].append({"lote":lote,"cantidad":cantidad,"costo":costo})    
    
    print(herramientas)
    print(f"El costo de las mercaderías ascienden a $ {cantidad*costo}")
    print("Se ha registrado la entrada de mercaderías")
    return

#def salida_venta():
    