print("Ricardo Aragón 1155324") 
d=0 
while d<=0: 
    d=int(input("Ingrese un número mayor 0: ")) 
    if d<=0: 
        print("El número mayor ingresado debe ser mayor a 0") 
        print() 
ProceA=sum(1/m for m in range(1,d+1))  
print("Calculo a:", ProceA) 
print()
ProceB=sum(1/(2**C) for C in range(1,d+1)) 
print("Calculo B", ProceB)   
print() 
k=int(input("Ingrese un número entero para la variable k: ")) 
g=int(input("Ingrese un número entero para la variable g: "))  
f=int(input("Ingrese un número entero para la variable m: ")) 
ProceC=sum((k**p)*(g**(f-p))for p in range(f+1)) 
print("Calculo C", ProceC) 


