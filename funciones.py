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