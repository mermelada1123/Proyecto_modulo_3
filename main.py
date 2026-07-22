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
            
            herramienta =  input("Ingrese la herramienta a registrar: ")
            lote = input("Ingrese lote: ")
            cantidad = int(input("Ingrese cantidad: "))   
            costo = int(input("Ingrese precio unitario: "))  
            entrada_compras(herramienta,lote,cantidad,costo)      
            
            
                    
        elif opcion =="2":
            print(" 📤 Salida de mercadería por ventas")
            herramienta = input("que harramienta se vendió?: ")
            #lote = input("A que lote corresponde: ") aca no debe se input, se debe descontar lote mas antiguo
            cantidad = int(input("Ingrese cantidad vendida: "))   
            #costo = int(input("Ingrese precio unitario: ")) Aca el costo debe provenir de lote mas antiguo
            
            
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
        
        else:
            print("Ingrese solo numeros del 1-7")
if __name__=="__main__":
            
    main()