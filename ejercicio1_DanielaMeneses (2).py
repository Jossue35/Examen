print("-----Menú de opciones-----","\n","1.Suma","\n","2.Resta","\n","3.Multiplicación","\n","4.División","\n", "5.Potencia","\n","6.Raíz","\n","7.Salir")



try:
    opcion = float(input("Elija la operación que desea realizar: "))
except ValueError:
    print("Error: Ingrese un valor numérico válido.")
else:

    match opcion:
        case 1:
            print("Usted ha seleccionado suma")
            try:
                a = float(input("Ingrese el primer número que desea sumar: "))
                b = float(input("Ingrese el segundo número que desea sumar: "))
                print("La suma de los números es: ", a + b)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
        case 2:
            print("Usted ha seleccionado resta")
            try:
                c = float(input("ingrese el minuendo: "))
                d = float(input("ingrese el sustraendo: "))
                print("La resta de los números es: ", c - d)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")

        case 3:
            print("Usted ha seleccionado multiplicación")
            try:
                e = float(input("ingrese el multiplicando: "))
                f = float(input("ingrese el multiplicador: "))
                print("La multiplicación de los números es: ", e * f)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")

        case 4:
            
            print("Usted ha seleccionado división")
            try:
                g = float(input("ingrese el dividendo: "))
                h = float(input("ingrese el divisor: "))
                print("La división de los números es: ", g / h)
            except ZeroDivisionError:
                print("Error: No se puede dividir por cero.")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
        case 5:
            
            print("Usted ha seleccionado potencia")
            try:
                i = float(input("ingrese la base: "))
                j = float(input("ingrese el exponente: "))
                print("El resultado es: ", i ** j)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
            except OverflowError:
                print("Error: El resultado es demasiado grande para ser representado.")
            except ZeroDivisionError:
                print("Error: No se puede elevar 0 a un exponente negativo.")
        case 6:
            print("Usted ha seleccionado raiz")
            try:
                k = float(input("Ingrese el radicando: "))
                m = float(input("Ingrese el índice: "))
                resultado = k ** (1 / m)
                print("El resultado es: ", resultado)

                if isinstance(resultado, complex): #Esto es una función en Python que se utiliza para comprobar si una variable es de un tipo de dato específico. En este caso, estamos verificando si resultado es una instancia del tipo de dato complex, que representa números complejos en Python.
                    print("La raíz cuadrada resulta en un número complejo.") #Los números complejos resultan cuando se intenta calcular la raíz cuadrada (índice 2) de un número negativo.
                
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
            except ZeroDivisionError:
                print("Error: No se puede calcular la raíz con índice cero.")
            

        case 7:
            print("Usted esta saliendo del menú")
            
        case _:
            print("Esta opción no existe")


