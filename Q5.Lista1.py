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

    def exibir(self, limite=20):
        if not self.inicio:
            print("Lista vazia.")
            return

        atual = self.inicio
        contador = 0
        while contador < limite:
            print(f"{atual.nome} ({atual.idade})", end=" -> ")
            atual = atual.proximo
            contador += 1
            if atual == self.inicio:
                break
        print("(volta ao início)")

    def validar_circularidade(self):
        if not self.inicio:
            return False

        atual = self.inicio.proximo
        while atual and atual != self.inicio:
            atual = atual.proximo
        return atual == self.inicio

if __name__ == "__main__":
    lista = ListaCircular()
    lista.inserir_ordenado("Ana", 25)
    lista.inserir_ordenado("Carlos", 30)
    lista.inserir_ordenado("Bruno", 20)
    lista.inserir_ordenado("Fernanda", 35)

    print("Lista Circular Ordenada por Idade:")
    lista.exibir()

    print("\nA lista é circular?", "Sim" if lista.validar_circularidade() else "Não")