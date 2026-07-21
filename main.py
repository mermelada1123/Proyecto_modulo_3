from datos import*
from funciones import*

def main():
    if not login(usuario,password):
        return
    
    while True:
        menu()

        opcion =input("Ingrese la opción que desea realizar: ")
                    
        if opcion =="1":
            print(" 📥 Entrada de mercadería por compras")
            lote = input("Ingrese lote: ")
            cantidad = int(input("Ingrese cantidad: "))   
            costo = int(input("Ingrese precio unitario: "))    
            
            # lista.append(nuevo_elemento)   , como mi nuevo elemento es un diccionario, ademas uso llaves para su contentido         
            Herramientas.append({"lote":lote,"cantidad":cantidad,"costo":costo}) 
            print(Herramientas)
            print(f"El costo de las mercaderías ascienden a $ {cantidad*costo}")
            print("Se ha registrado la entrada de mercaderías")
            
            
            
                    
        elif opcion =="2":
            print(" 📤 Salida de mercadería por ventas")
            
        elif opcion =="3":
            print(" 🤦‍♀️ Salida de mercadería por nota de crédito")
            
        elif opcion =="4":
            print(" 🪃 Entrada de mercadería por nota de crédito")
            
        elif opcion =="5":
            print(" 📲 Inventario y costo actual")
            
        elif opcion =="6":
            print(" 🔧 Ajustes de Inventario")
            
        elif opcion =="7":
            print(" 😊 Gracias por operar con Inventarios Plus.")
            break
if __name__=="__main__":
            
    main()