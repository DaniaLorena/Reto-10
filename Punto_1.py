#Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.


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
