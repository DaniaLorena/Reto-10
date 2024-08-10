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