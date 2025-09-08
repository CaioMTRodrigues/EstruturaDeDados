class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir(self, valor):
        novo_no = No(valor)
        if not self.inicio:
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")

    def remover_duplicatas(self):
        valores_vistos = set()
        atual = self.inicio
        anterior = None
        while atual:
            if atual.valor in valores_vistos:
                anterior.proximo = atual.proximo
            else:
                valores_vistos.add(atual.valor)
                anterior = atual
            atual = atual.proximo