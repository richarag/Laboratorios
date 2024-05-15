print("semana 12: Ejercicio ")
print("a, sumatoria")
print("b, factorial")
print("c, tablas de multiplicar")
print("d, numero perfecto")
opcion=input("elija una opcion a calcular")

match(opcion):
    case "a":
        N=0
        while N<=0:
            N=int(input("ingrese un numero entero positivo:"))
            if N<=0:
                print("el numero ingresado debe ser entero:")
        sumatoria=0
        for cont in range(1, N+1):
            sumatoria+=cont #sumatoria=sumatoria+cont
        print("la sumatoria es:", sumatoria)
    case "b": 
       N=0   
       while N<=0:
            N=int(input("ingrese un numero entero positivo:"))
            if N<=0:
                print("el numero ingresado debe ser entero")  
            factorial=1
            for cont in range (1, N+1):
                factorial*=cont # factorial=factorial*cont
            print("la factorial es:", factorial)
    case "c":
        for i in range (1,11):
            for j in range(1,11):
                print(i*j, "\t", end= '')
            print()
    case "d":
       N=0   
       while N<=0:
            N=int(input("ingrese un numero entero positivo:"))
            if N<=0:
                print("el numero ingresado debe ser entero")
            acumulador=0 
            for factor in range(1, N):
                if N%factor==0:
                    acumulador+=factor
            if N==acumulador:
                print("es perfecto")
            else:
                print("No es perfecto")   
    case _:
        print("elija una opcion valida")