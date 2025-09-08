class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_final(self, nome, idade):
        nova_pessoa = Pessoa(nome, idade)
        if not self.inicio:
            self.inicio = nova_pessoa
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nova_pessoa

    def exibir(self):
        atual = self.inicio
        while atual:
            print(f"{atual.nome} ({atual.idade})", end=" -> ")
            atual = atual.proximo
        print("None")

def mesclar_listas(lista1, lista2):
    nova_lista = ListaEncadeada()
    p1 = lista1.inicio
    p2 = lista2.inicio

    while p1 and p2:
        if p1.idade <= p2.idade:
            nova_lista.inserir_final(p1.nome, p1.idade)
            p1 = p1.proximo
        else:
            nova_lista.inserir_final(p2.nome, p2.idade)
            p2 = p2.proximo

    while p1:
        nova_lista.inserir_final(p1.nome, p1.idade)
        p1 = p1.proximo

    while p2:
        nova_lista.inserir_final(p2.nome, p2.idade)
        p2 = p2.proximo

    return nova_lista

if __name__ == "__main__":
    lista1 = ListaEncadeada()
    lista1.inserir_final("Ana", 22)
    lista1.inserir_final("Carlos", 30)
    lista1.inserir_final("Fernanda", 40)

    lista2 = ListaEncadeada()
    lista2.inserir_final("Bruno", 25)
    lista2.inserir_final("Daniela", 35)
    lista2.inserir_final("Eduardo", 45)

    print("Lista 1:")
    lista1.exibir()

    print("Lista 2:")
    lista2.exibir()

    lista_mesclada = mesclar_listas(lista1, lista2)

    print("Lista Mesclada:")
    lista_mesclada.exibir()