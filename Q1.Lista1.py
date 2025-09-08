class Livro:
    def __init__(self, rotulo, autor, ano, codigo):
        self.rotulo = rotulo
        self.autor = autor
        self.ano = ano
        self.codigo = codigo

    def __str__(self):
        return f"{self.rotulo} ({self.ano}) - {self.autor} [Código: {self.codigo}]"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.rotulo}' adicionado com sucesso.")

    def buscar_por_rotulo(self, rotulo):
        encontrados = [livro for livro in self.livros if livro.rotulo.lower() == rotulo.lower()]
        return encontrados

    def remover_por_codigo(self, codigo):
        for livro in self.livros:
            if livro.codigo == codigo:
                self.livros.remove(livro)
                print(f"Livro com código {codigo} removido com sucesso.")
                return
        print(f"Nenhum livro encontrado com o código {codigo}.")


if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.adicionar_livro(Livro("Python para Iniciantes", "João Silva", 2020, "001"))
    biblioteca.adicionar_livro(Livro("Algoritmos em Python", "Maria Souza", 2021, "002"))
    biblioteca.adicionar_livro(Livro("Estruturas de Dados", "Carlos Lima", 2019, "003"))

    print("\nBusca por rótulo 'Python para Iniciantes':")
    resultado = biblioteca.buscar_por_rotulo("Python para Iniciantes")
    for livro in resultado:
        print(livro)

    print("\nRemovendo livro com código '002':")
    biblioteca.remover_por_codigo("002")

    print("\nLivros restantes na biblioteca:")
    for livro in biblioteca.livros:
        print(livro)
