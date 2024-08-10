# Reto 10

Aprendiendo sobre Listas :)

> #### Ejercicio 1
>Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

```
#Se crea un lista vacia y se declaran e incializan varibales
lista : float = []
suma : float = 0
#Se pide que cantidad de elementos va a tener el arreglo
cantidad : int = int (input("Ingrese la cantidad de componente que va a tener el arreglo: "))
#Se crea un ciclo for que va a realizar las iteraciones 
for i in range (cantidad):
    #Se pide a ususario que ingrese los numeros que va a conformar el arreglo
    num: float = float(input("Ingrese el nuevo numero a la lista: "))
    #Se va agregando el elemento a la lista
    lista.append (num)
    #Se va sumando cada elemento
    suma += lista [i]   

print (f"El arreglo es {lista}")
print (f"El promedio del arreglo es: {suma/len(lista)}")
```

> #### Ejercicio 2
> Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

```
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
```
> #### Ejercicio 3
> Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```
lista : int = []
lista_1: int =[]
#Se pide que cantidad de elementos va a tener el arreglo
cantidad : int = int (input("Ingrese la cantidad de componente que va a tener el arreglo: "))
#Se crea un ciclo for que va a realizar las iteraciones para llenar el vector
for i in range (cantidad):
    #Se pide a ususario que ingrese los numeros que va a conformar el arreglo
    num: int = int(input(f"Ingrese el {i+1} elemento a la lista: "))
    #Se va agregando el elemento a la lista
    lista.append (num)

print (f"El arreglo es {lista}")
#Por medio del método *Count* Se conoce cuantas veces se tiene que implementar los demás métodos
cantidad : int = lista.count(0)
print (f"La cantidad de ceros que tiene la lista es: {cantidad}")
#Se crea un ciclo for para que quite la los ceros de la lista, esto va a iterar la cantidad de ceros que tenga la lista
for i in range (cantidad):
    lista.remove(0)
#Se agrega al final de la lista la cantidad de ceros que tenia la lista
for i in range (cantidad):
    lista.append(0)

print (f"La nueva lista es: {lista}")
```
