class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.proximo = None

class ListaCircular:
    def __init__(self):
        self.inicio = None

    def inserir_ordenado(self, nome, idade):
        nova_pessoa = Pessoa(nome, idade)

        if not self.inicio:
            self.inicio = nova_pessoa
            nova_pessoa.proximo = self.inicio
            return

        atual = self.inicio
        anterior = None

        while True:
            if idade < atual.idade:
                break
            anterior = atual
            atual = atual.proximo
            if atual == self.inicio:
                break

        nova_pessoa.proximo = atual

        if anterior:
            anterior.proximo = nova_pessoa
        else:
            ultimo = self.inicio
            while ultimo.proximo != self.inicio:
                ultimo = ultimo.proximo
            ultimo.proximo = nova_pessoa
            self.inicio = nova_pessoa

    def exibir(self):
        if not self.inicio:
            print("Lista vazia.")
            return

        atual = self.inicio
        while True:
            print(f"{atual.nome} ({atual.idade})", end=" -> ")
            atual = atual.proximo
            if atual == self.inicio:
                break
        print("(volta ao início)")