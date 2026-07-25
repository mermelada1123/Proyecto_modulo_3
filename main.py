from datos import*
from funciones import*

def main():
    """if not login(usuario,password):
        return
    """
    while True:
        menu()

        opcion =input("Ingrese la opción que desea realizar: ")
                    
        if opcion =="1":
            print(" 📥 Entrada de mercadería por compras")
            
            herramienta =  input("Ingrese la herramienta a registrar: ").lower()
            lote = (input("Ingrese lote: "))
            if lote.isdecimal():
                lote =int(lote)
                cantidad = (input("Ingrese cantidad: "))   
                if cantidad.isdecimal():
                    cantidad = int(cantidad)
                    costo = (input("Ingrese precio unitario: "))  
                    if costo.isdecimal():
                        costo = int(costo)
                        

                        entrada_compras(herramienta,lote,cantidad,costo)
                    else:
                        print(f" ❌ Ingrese sólo numeros")
                else:
                    print(f" ❌ Ingrese sólo numeros")
            else:
                print(f" ❌ Ingrese sólo numeros")         
        
                                
        elif opcion =="2":
            print(" 📤 Salida de mercadería por ventas")
            herramienta = input("que harramienta se vendió?: ").lower()
            if existencia(herramienta):
                cantidad_vendida = (input("Ingrese cantidad vendida: "))
                if cantidad_vendida.isdecimal():
                    cantidad_vendida = int(cantidad_vendida)   
                    if validar_venta(herramienta,cantidad_vendida):
                        descontar_fifo_venta(herramienta,cantidad_vendida)
                else:
                    print(f" ❌ Ingrese solo cantidades numéricas")            
            
                        
            
        elif opcion =="3":
            print(" 📲 Inventario y costo actual")
            mostrar_listado_herrramientas()
                
            herramienta = input("a que herramienta le consultará el stock: ").lower()
                
            mostrar_inventario(herramienta)
        
        
        elif opcion =="4":
            print(" 🕠 Historial de compras")
            mostrar_historial_compras()
            
            
            
        elif opcion =="5":
            print(" 😊 Gracias por operar con Inventarios Plus.")
            break
                
        else:
            print(" ❌ Ingrese solo numeros del 1-7")
if __name__=="__main__":
            
    main()