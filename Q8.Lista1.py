class Pagina:
    def __init__(self, url):
        self.url = url
        self.anterior = None
        self.proximo = None

class Deque:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir_inicio(self, url):
        nova_pagina = Pagina(url)
        if not self.inicio:
            self.inicio = self.fim = nova_pagina
        else:
            nova_pagina.proximo = self.inicio
            self.inicio.anterior = nova_pagina
            self.inicio = nova_pagina

    def inserir_fim(self, url):
        nova_pagina = Pagina(url)
        if not self.fim:
            self.inicio = self.fim = nova_pagina
        else:
            nova_pagina.anterior = self.fim
            self.fim.proximo = nova_pagina
            self.fim = nova_pagina

    def remover_inicio(self):
        if not self.inicio:
            return None
        pagina = self.inicio
        self.inicio = self.inicio.proximo
        if self.inicio:
            self.inicio.anterior = None
        else:
            self.fim = None
        return pagina

    def remover_fim(self):
        if not self.fim:
            return None
        pagina = self.fim
        self.fim = self.fim.anterior
        if self.fim:
            self.fim.proximo = None
        else:
            self.inicio = None
        return pagina

    def exibir(self):
        atual = self.inicio
        print("Histórico de Navegação:")
        while atual:
            print(f"- {atual.url}")
            atual = atual.proximo
        print("Fim do histórico.\n")

class Navegador:
    def __init__(self):
        self.historico = Deque()
        self.pilha_avancar = []

    def acessar_pagina(self, url):
        self.historico.inserir_fim(url)
        self.pilha_avancar.clear()
        print(f"Acessando: {url}")

    def voltar(self):
        pagina = self.historico.remover_fim()
        if pagina:
            self.pilha_avancar.append(pagina.url)
            print(f"Voltando da página: {pagina.url}")
        else:
            print("Não há páginas para voltar.")

    def avancar(self):
        if self.pilha_avancar:
            url = self.pilha_avancar.pop()
            self.historico.inserir_fim(url)
            print(f"Avançando para: {url}")
        else:
            print("Não há páginas para avançar.")

    def mostrar_historico(self):
        self.historico.exibir()

if __name__ == "__main__":
    navegador = Navegador()

    navegador.acessar_pagina("google.com")
    navegador.acessar_pagina("github.com")
    navegador.acessar_pagina("stackoverflow.com")

    navegador.mostrar_historico()

    navegador.voltar()
    navegador.voltar()

    navegador.mostrar_historico()

    navegador.avancar()
    navegador.mostrar_historico()