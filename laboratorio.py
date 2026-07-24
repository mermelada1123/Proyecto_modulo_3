"""herramientas = {'mazo': [{'lote': 1, 'cantidad': 2, 'costo': 140}, {'lote': 2, 'cantidad': 4, 'costo': 234}], 'taladro': [{'lote': 1, 'cantidad': 4, 'costo': 345}]}
print(herramientas)
print(herramientas["mazo"])
print(herramientas["mazo"][0]["lote"])
#for herramienta in herramientas:
#   print(herramienta["lote"])
lotes = herramientas['mazo']
print(lotes)"""

"""def buscar_lote(herramienta,):
    
    if herramienta in herramientas:
        
        #funcion verificar lote mas antiguo
        lote_mas_antiguo = None
        for lote in herramientas[herramienta]:
            if lote_mas_antiguo is None:
                lote_mas_antiguo = lote
            elif lote < lote_mas_antiguo:
                lote_mas_antiguo = lote               
                
        print(lote_mas_antiguo)
        
    else:
        print(f" No tenemos {herramienta} en stock, por favor contacte al departamento de compras, o contacte al vendedor para que anulen la venta")
"""

"""venta = 6

herramienta = [{"lote":1,"cantidad":5},{"lote":2,"cantidad":3}]
c_p = venta
for i in herramienta:
    print(i["cantidad"])
    print(f"c_p {c_p} ")
    if i["cantidad"] >= c_p:
        saldo = i["cantidad"]-c_p
        print(f"saldo{saldo}")
        i["cantidad"]=saldo
        print(f" if {herramienta}") 
        break
    else:
        c_p -= i["cantidad"]
        i["cantidad"] = 0
        
        print(f" else {herramienta}")   """ 
            
            
#prueba de mostrar inventario           
martillos = [{"lote":1,"cantidad":5,"costo":300},{"lote":2,"cantidad":3,"costo":360},{"lote":3,"cantidad":6,"costo":200}]
cantidad_acumulada = 0
costo_acumulado = 0
print(f"Kardex de martillo")

print("-------------------------------------------------------------------------------------------------------------------------")
print(f" {'lote':^20}{'cantidad':^20}{'total':^20} {'costo un.':^20} {'costo/lote':^20}{'costo total':^20}") #:>20, formato de alineación, el numero indica la cantidad de estación que se va a reservar para el elemento, >izquierda, <derecha, ^centrado.
print("-------------------------------------------------------------------------------------------------------------------------")#va entre (')si es un texto, seguido del formato y entre llaves, su es una variable, usa las llaves que ya usa la variable, junto con el formato 
for i in martillos:
    costo_lote = i["cantidad"]*i["costo"]
    cantidad_acumulada += i["cantidad"]
    costo_acumulado += costo_lote
    #print(f" martillos {i["cantidad"]} ||{i["costo"]} || {costo_lote}")
    #print(cantidad_acumulada)
    #print(costo_acumulado)
    
    print(f"{i['lote']:^20} {i['cantidad']:^20}{cantidad_acumulada:^20}{i['costo']:^20}{costo_lote:^20}{costo_acumulado:^20}")
print("-------------------------------------------------------------------------------------------------------------------------")    
    #la funcion llevara un input para herramietas, y sera el parametro
print(f"Total de unidades {cantidad_acumulada}")    
print(f"Costo total del inventario $ {costo_acumulado}")    
print("--------------------------------------------------")  