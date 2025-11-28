from LinkedList import *

lista = LinkedList()
print("Lista Vazia:")
imprimirLista(lista)

print("Inserindo no final:")
inserirNoFinal(lista, 10)
imprimirLista(lista)

inserirNoFinal(lista, 20)
imprimirLista(lista)

print("Inserindo no meio:")
inserirNoMeio(lista, 5, 2)
imprimirLista(lista)

inserirNoMeio(lista, 15, 3)
imprimirLista(lista)

print("Inserindo no início:")
inserirNoInicio(lista, 1)
imprimirLista(lista)

inserirNoInicio(lista, 99)
imprimirLista(lista)
