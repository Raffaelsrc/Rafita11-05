sw = 1
while sw == 1:
    print("1. Comprar Entradas")
    print("2. Salir")
    op = int(input("SELECCIONE OPCION"))
try: 
    if (op > 0 and op < 4):
        print("ha seleccionado la opcion de comprar entradas")
        continuar = int(input("desea seguir comprando? 1= no\t2 = si"))
        if continuar == 1:
            print("muchas gracias por su compra")
            sw = 0
    if op == 2:
        print("Cerrando sesion...")
        sw = 0
except:
    print("Ingreso de opcion erronea")
    
    