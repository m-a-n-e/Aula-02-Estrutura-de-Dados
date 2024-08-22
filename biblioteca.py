class Livro():
    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def exibirDetalhes(self):
        if self.disponivel:
            situacao = "Disponível"
        else:
            situacao = "Indisponível"
        print(f"    Título: {self.titulo} | Autor: {self.autor} | Situação: {situacao}")


class Usuario():
    def __init__(self, nome):
        self.nome = nome
        self.livrosEmprestados = []

    def emprestarLivro(self, livro):
        if livro.disponivel:
            self.livrosEmprestados.append(livro)
            livro.disponivel = False
            print(f"O livro {livro.titulo} foi emprestado para {self.nome}.")
        else:
            print(f"O livro {livro.titulo} está Indisponível no momento.")

    def devolverLivro(self, livro):
        if livro in self.livrosEmprestados:
            self.livrosEmprestados.remove(livro)
            livro.disponivel = True
            print(f"O livro {livro.titulo} foi devolvido por {self.nome}.")
        else: 
            print(f"O livro {livro.titulo} não está com {self.nome}.")


class Biblioteca():
    def __init__(self, nome):
        self.nome = nome
        self.estoqueLivros = []

    def adicionarLivro(self, livro):
        self.estoqueLivros.append(livro)
        print(f"O livro {livro.titulo} foi adicionado.")

    def exibirLivros(self):
        print("Livros disponíveis: ")
        for livro in self.estoqueLivros:
            if livro.disponivel:
                livro.exibirDetalhes()


biblioteca = Biblioteca("Biblioteca SATC")
usuario1 = Usuario("Emanuel")
usuario2 = Usuario("Letícia")
usuario3 = Usuario("Pedro")
usuario4 = Usuario("João")
livro1 = Livro("Ready Player One", "Ernest Cline")
livro2 = Livro("Eine Reise durch die Zeit", "H. G. Tannhaus")
livro3 = Livro("O Alquimista", "Paulo Coelho")
livro4 = Livro("The Creative ACT", "Rick Rubin")

biblioteca.adicionarLivro(livro1)
biblioteca.adicionarLivro(livro2)
biblioteca.adicionarLivro(livro3)
biblioteca.adicionarLivro(livro4)
biblioteca.exibirLivros()

usuario1.emprestarLivro(livro4)

biblioteca.exibirLivros()

usuario2.emprestarLivro(livro3)
usuario1.devolverLivro(livro4)

biblioteca.exibirLivros()