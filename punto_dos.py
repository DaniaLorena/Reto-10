#Se crean y declaran dos listas vacias
lista_1 : float =[]
lista_2 : float = []

cantidad : int = int (input("Ingrese la cantidad de componente que van a tener los arreglos: "))
#Se crea un ciclo for que va a realizar las iteraciones para llenar los vectores
for i in range (cantidad):
    #Se pide a ususario que ingrese los numeros que va a conformar el arreglo
    num: float = float(input(f"Ingrese {i+1}  elemento al arreglo _1 : "))
    #Se va agregando el elemento a la lista
    lista_1.append (num)

for i in range (cantidad):
    num: float = float(input(f"Ingrese {i+1} elemento al arreglo _2 : "))
    lista_2.append (num)
  
print (f"El arreglo 1 es {lista_1}")
print (f"El arreglo 2 es {lista_2}")

#Se realiza el producto punto entre los vectores formados anteriormente
producto_punto: float = 0
for i in range (len(lista_1)):
    producto_punto += lista_1[i]*lista_2[i]

print (f"El producto punto de los vectores es: {producto_punto}")