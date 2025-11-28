from LinkedList import *

def carregarEntrada(arquivo):
    with open(arquivo, "r") as f:
        qtd_testes = int(f.readline().strip())

        testes = []
        for _ in range(qtd_testes):
            tam, altura_loop = map(int, f.readline().strip().split())
            valores = list(map(int, f.readline().strip().split()))
            testes.append((tam, altura_loop, valores))

    return testes


def executarInput(altura_loop, valores):
    lista = LinkedList()

    imprimirLista(lista)

    print("\nInserindo valores do arquivo:")
    for v in valores:
        inserirNoFinal(lista, v)
        imprimirLista(lista)

    print(f"\nGerando loop!!")
    geraLoop(lista, altura_loop)

    inicio = getInicio(lista)
    print(f"\nInício da lista: [{inicio.dado}]")

    if altura_loop == 0:
        print("\nNenhum loop será criado (altura = 0).")
        imprimirLista(lista)
        return  # encerra o teste

    atual = lista.ponteiroInicial
    for _ in range(20):
        print(f"[{atual.dado}]", end=" -> ")
        atual = atual.proximo
    print("... LOOP ...")

    detectaLoop(lista)

def main():
    testes = carregarEntrada("input.txt")

    for tam, altura_loop, valores in testes:
        print("\n==============================")
        executarInput(altura_loop, valores)


if __name__ == "__main__":
    main()
