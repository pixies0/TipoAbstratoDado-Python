from .No import No

class LinkedList:
    def __init__ (self):
        self.ponteiroInicial = None

def inserirNoFinal(lista, novoElemento):
    novoNo = No(novoElemento)
    if lista.ponteiroInicial is None:
        lista.ponteiroInicial = novoNo
    else:
        atual = lista.ponteiroInicial
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = novoNo

def inserirNoMeio(lista, novoElemento, posicao):
    novoNo = No(novoElemento)
    if posicao == 0:
        novoNo.proximo = lista.ponteiroInicial
        lista.ponteiroInicial = novoNo
    else:
        atual = lista.ponteiroInicial
        contador = 0
        while atual is not None and contador < posicao - 1:
            atual = atual.proximo
            contador += 1
        if atual is None:
            raise IndexError("Posição fora dos limites da lista")
        novoNo.proximo = atual.proximo
        atual.proximo = novoNo

def inserirNoInicio(lista, novoElemento):
    novoNo = No(novoElemento)
    novoNo.proximo = lista.ponteiroInicial
    lista.ponteiroInicial = novoNo

def imprimirLista(lista):
    atual = lista.ponteiroInicial
    while atual is not None:
        print(f"[{atual.dado}]", end=" -> ")
        atual = atual.proximo
    print("[ ]")
