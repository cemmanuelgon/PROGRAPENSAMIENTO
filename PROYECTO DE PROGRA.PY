#Creaciòn del proyecto
inicio= print("Bienvenidos, esta es LicuadosBetter, los mejores licuados de fresa de todo el paìs")
nombre = input("Ingresa tu nombre:")
print("Buenos dìas", nombre,)
preciolicuado=20
opciones=0
respuesta=input("¿Quieres ingresar tu número de NIT? (SI/NO): ")
if respuesta.lower() == "si":
    NIT= input("Ingrese el nùmero de NIT, por favor")
    print("Tù nùmero de NIT es", NIT)
else:
    vermenu=0
    print("Ok,no hay problema tù NIT es C/F")
    NIT=("C/F")
vermenu=input("¿Deseas ver el menú? SI/NO: ")
if vermenu.lower() == "si":
    print("El menù es un licuado de el licuado de fresa con leche deslactosada sin azúcar de tamaño normal Q20.00")
    preciolicuado=20
else:
    print("Entendido")
iniciodelcambio= input("¿Deseas hacer un cambio a tu pedido? SI/NO: ")   
if iniciodelcambio.lower ()== "si":
    print("Escoge alguna opción del menú de cambios")
    resultado = 0
    menu= 0
    while True:
            menu = int(input("""
                Menú de cambios
                (1) Azúcar
                (2) Tipo de leche (obligatorio)
                (3) Agrandado
                (4) confirmar pedido
                (5) Salir
                """))
            if menu == 1:
                cambiosazucar=0
                cantazucar=0
                totalazucar=0
                calculoazucar=0
                if cantazucar <= 2:
                    print("Por cada cucharadita cuesta Q0.50, Solo se pueden agregar 2") 
                    print("Cuantos cucharaditas desea agregar?")
                    calculoazucar = int(input(cantazucar))
                    totalazucar= calculoazucar * 0.50
                    print("Total de cambio de azúcar es : Q.",totalazucar)
                else:
                    print( "ERROR INGRESE CANTIDAD VÁLIDA")

            elif menu == 2:
                tipodeleche=0
                precioporcambiodeleche=0
                cantidaddelicuados=0
                suma=0
                menu = int(input("""
            Menú de comida
            (1) agua
            (2) leche deslactosada
            (3) Leche entera
            (4) leche de soya
                        """))
                print("Que tipo de leche quiere")
                if menu == 1:
                    tipodeleche= str("Licuado de agua")
                    cantidaddelicuados= int(input("¿Cuántos licuados deseas agregar con este tipo?"))
                    precioporcambiodeleche= cantidaddelicuados * 18
                    print("Tu licuado ahora será de", tipodeleche, "y precio de ", precioporcambiodeleche)
                    suma= totalazucar + precioporcambiodeleche
                    preciodecambiodelecheyagregarazucar=suma
                    print("El precio del cambio de tipo de leche y agregado de cucharaditas de azúcar es de", suma)
                elif menu==2:
                    tipodeleche= str("licuado con leche deslactosada")
                    print("Tu licuado ahora será de", tipodeleche)
                    cantidaddelicuados= int(input("¿Cuántos licuados deseas agregar con este tipo?"))
                    precioporcambiodeleche= cantidaddelicuados * 20
                    print("Tu licuado ahora será de", tipodeleche, "y precio de ", precioporcambiodeleche)
                    suma= totalazucar + precioporcambiodeleche
                    preciodecambiodelecheyagregarazucar=suma
                    print("El precio del cambio de tipo de leche y agregado de cucharaditas de azúcar es de", suma)
                elif menu==3:
                    tipodeleche= str("Licuado con leche entera")
                    print("Tu licuado ahora será de", tipodeleche)
                    cantidaddelicuados= int(input("¿Cuántos licuados deseas agregar con este tipo?"))
                    precioporcambiodeleche= cantidaddelicuados * 20
                    print("Tu licuado ahora será de", tipodeleche, "y precio de ", precioporcambiodeleche)
                    suma= totalazucar + precioporcambiodeleche
                    preciodecambiodelecheyagregarazucar=suma
                    print("El precio del cambio de tipo de leche y agregado de cucharaditas de azúcar es de", suma)
                elif menu==4:
                    tipodeleche= str("Licuado con leche de soya")
                    print("Tu licuado ahora será de", tipodeleche)
                    cantidaddelicuados= int(input("¿Cuántos licuados deseas agregar con este tipo?"))
                    precioporcambiodeleche= cantidaddelicuados * 23
                    print("Tu licuado ahora será de", tipodeleche, "y precio de ", precioporcambiodeleche)
                    suma= totalazucar + precioporcambiodeleche
                    preciodecambiodelecheyagregarazucar=suma
                    print("El precio del cambio de tipo de leche y agregado de cucharaditas de azúcar es de", suma)
                elif menu :
                    break
            elif menu == 3:
                agrandarlicuado=0
                calculolicuado=0
                totalagrandadolicuado=0
                preciofinaldelpedido=0
                suma=0
                print("El precio por agrandado es del .5 porciento del licuado")
                cantidaddeagrandadodelicuado= int(input("Cuántos licuados desea agregar?:"))
                calculolicuado = cantidaddeagrandadodelicuado
                totalagrandadolicuado = ((calculolicuado + preciodecambiodelecheyagregarazucar) * 0.05) + (calculolicuado + preciodecambiodelecheyagregarazucar)
                print("El total del agrandado con el cambio de tipo de leche y el agregado de cucharaditas de azúcar es de", totalagrandadolicuado)
                suma= totalagrandadolicuado
                preciofinaldelpedido= suma
                print("El precio final del pedido es de", preciofinaldelpedido)
            elif menu== 4:
                pedidofinal=0
                confirmarpedido=input("¿Quieres confirmar tu pedido? (SI/NO): ")
                if confirmarpedido.lower() == "si":
                    print("Tu pedido agrego la cantidad de cucharaditas de azúcar de", calculoazucar, "Agrego la cantidad de tipo de leche de", tipodeleche, "y por último agrego la cantidad de agrandados de", cantidaddeagrandadodelicuado, "dando una cantida de precio final de", preciofinaldelpedido)
                else:
                    print("la orden a nombre de", nombre, "con NIT de", NIT, "su precio final es de", preciofinaldelpedido)
            elif menu == 5:
                break  
else:
    print("Entendido")
    print(" la orden a nombre de", nombre, "con NIT de", NIT, "su precio final es de Q20.")