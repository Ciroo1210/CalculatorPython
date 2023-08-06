opciones  = int(input(print("""elije la operación
                            1 suma
                            2 resta 
                            3  division
                            4 multiplicación""")))
n1 = float(input(print("elije numero")))
n2 = float(input(print("elije numero")))

if opciones == 1:
    n3 = (n1 + n2)
    print("este es el resultado =",(n3))
    
elif opciones == 2:
    n3 = (n1 - n2)
    print("este es el resultado =",(n3))
    
elif opciones == 3:
    n3 = (n1 // n2)
    print("este es el resultado =",(n3))

elif opciones == 4:
    n3 = (n1 * n2)
    print("este es el resultado =",(n3))
    
    