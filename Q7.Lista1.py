class Requisicao:
    def __init__(self, numero, tamanho_arquivo):
        self.numero = numero
        self.tamanho_arquivo = tamanho_arquivo

    def __str__(self):
        return f"Requisição {self.numero} - {self.tamanho_arquivo}KB"

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0

    def esta_cheia(self):
        return self.tamanho == self.capacidade

    def esta_vazia(self):
        return self.tamanho == 0

    def enfileirar(self, requisicao):
        if self.esta_cheia():
            print("Fila cheia. Não é possível adicionar nova requisição.")
            return
        self.fila[self.fim] = requisicao
        self.fim = (self.fim + 1) % self.capacidade
        self.tamanho += 1
        print(f"Requisição {requisicao.numero} adicionada à fila.")

    def atender_requisicao(self):
        if self.esta_vazia():
            print("Fila vazia. Nenhuma requisição para atender.")
            return
        requisicao = self.fila[self.inicio]
        self.fila[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        print(f"Atendendo {requisicao}")

    def exibir_fila(self):
        print("Fila de Impressão:")
        i = self.inicio
        count = 0
        while count < self.tamanho:
            print(self.fila[i])
            i = (i + 1) % self.capacidade
            count += 1
        print("Fim da fila.\n")

if __name__ == "__main__":
    fila = FilaCircular(5)

    fila.enfileirar(Requisicao(1, 120))
    fila.enfileirar(Requisicao(2, 300))
    fila.enfileirar(Requisicao(3, 150))

    fila.exibir_fila()

    fila.atender_requisicao()
    fila.atender_requisicao()

    fila.exibir_fila()

    fila.enfileirar(Requisicao(4, 200))
    fila.enfileirar(Requisicao(5, 100))
    fila.enfileirar(Requisicao(6, 250)) 

    fila.exibir_fila()