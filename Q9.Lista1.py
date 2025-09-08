class Requisicao:
    def __init__(self, id, prioridade):
        self.id = id
        self.prioridade = prioridade

    def __str__(self):
        return f"Requisição {self.id} - Prioridade {self.prioridade}"

class FilaPrioridade:
    def __init__(self):
        self.fila = []

    def enfileirar(self, requisicao):
        self.fila.append(requisicao)
        self.fila.sort(key=lambda r: r.prioridade)
        print(f"Requisição {requisicao.id} adicionada com prioridade {requisicao.prioridade}.")

    def desenfileirar(self):
        if not self.fila:
            print("Fila vazia.")
            return None
        requisicao = self.fila.pop(0)
        print(f"Atendendo {requisicao}")
        return requisicao

    def exibir(self):
        print("Fila com Prioridade:")
        for r in self.fila:
            print(f"- {r}")
        print("Fim da fila.\n")

if __name__ == "__main__":
    fila = FilaPrioridade()

    fila.enfileirar(Requisicao(1, 3))
    fila.enfileirar(Requisicao(2, 1))
    fila.enfileirar(Requisicao(3, 2))

    fila.exibir()

    fila.desenfileirar()
    fila.desenfileirar()

    fila.exibir()