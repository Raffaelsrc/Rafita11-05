precio_menor = 4000
precio_adulto = 7000
precio_tercera_edad = 3000
precio_entrada = 0
entrada_adulto= 0
entrada_menor = 0
entrada_tercera_edad = 0
sw = 1
while sw == 1:
    print("--SISTEMA COMPRA ENTRADAS--")
    print("1. Comprar Entradas")
    print("2. Salir")
    op = int(input("SELECCIONE OPCION"))
    try: 
            if (op > 0 and op < 3):
                print("ha seleccionado la opcion de comprar entradas")
                cantidad = int(input("Cuantas entradas desea?"))
                for n in range(cantidad):
                    tipo = int(input("Entradas disponibles: \n1. Entrada infantil $4.000\t2. Entrada Adulto $7.000\t3. Entrada Tercera Edad $3.000"))
                    if tipo == 1:
                        entrada_menor = entrada_menor + 1
                        precio_entrada = precio_entrada + 4000
                    elif tipo == 2:
                        entrada_adulto = entrada_adulto + 1
                        precio_entrada = precio_entrada + 7000
                    elif tipo == 3:
                        entrada_tercera_edad = entrada_tercera_edad + 1
                        precio_entrada = precio_entrada + 3000
                    else:
                        print("OPCION INCORRECTA")
                continuar = int(input("desea seguir comprando? 1= no\t2 = si"))
                if continuar == 1:
                    print("---Resumen de compra---")
                    print(f"1. ENTRADA MENOR\tcantidad {entrada_menor}")
                    print(f"2. ENTRADA ADULTO\tcantidad {entrada_adulto}")
                    print(f"3. ENTRADA TERCER EDAD\tcantidad {entrada_tercera_edad}")
                    print(f"TOTAL A PAGAR ES ${precio_entrada}")
                    sw = 0
                if op == 2:
                    print("Cerrando sesion...")
                    sw = 0
    except:
            print("Ingreso de opcion erronea")