from .No import No

class LinkedList:
    def __init__ (self):
        self.ponteiroInicial = None

def getInicio(lista):
    return lista.ponteiroInicial

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

def removerElemento(lista, elemento):
    if lista.ponteiroInicial is None:
        print("Lista vazia. Nada para remover.\n")
        return False

    atual = lista.ponteiroInicial
    anterior = None
    while atual is not None:
        if atual.dado == elemento:
            if anterior is None:
                lista.ponteiroInicial = atual.proximo
            else:
                anterior.proximo = atual.proximo
            return
        anterior = atual
        atual = atual.proximo
    print(f"Elemento {elemento} não encontrado.")
    return False

def geraLoop(lista, altura):
    atual = lista.ponteiroInicial
    loop_no = None

    while atual is not None:
        altura -= 1
        if altura == 0:
            loop_no = atual
        if atual.proximo is None:
            break
        atual = atual.proximo

    atual.proximo = loop_no

def detectaLoop(lista):
    tartaruga = lista.ponteiroInicial
    lebre = lista.ponteiroInicial

    # Detecta loop
    while lebre is not None and lebre.proximo is not None:
        tartaruga = tartaruga.proximo
        lebre = lebre.proximo.proximo

        if tartaruga == lebre:
            break
    else:
        return 0  # Sem loop

    # Descobre início do loop
    tartaruga = lista.ponteiroInicial
    pos = 1

    while tartaruga != lebre:
        tartaruga = tartaruga.proximo
        lebre = lebre.proximo
        pos += 1

    print(f"\nO Loop se ínicia na {pos}ª posição")
    return pos
