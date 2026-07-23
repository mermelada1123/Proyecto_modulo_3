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

venta = 6

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
        
        print(f" else {herramienta}")    
            