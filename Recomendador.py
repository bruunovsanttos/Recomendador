import random
from tkinter import *

Tk()

def menu():
    while True:

        categoria = int(input(f"""{nome_usuario} gostaria de recomendações de que tipo?"
    1 - Filmes
    2 - Livros
    3 - Games
    """))

        if categoria == 1:
            recomendar_filmes()

        elif categoria == 2:
            recomendar_livros()

        elif categoria == 3:
            recomendar_games()


def recomendar_filmes():
    recomendar_filmes = input(f"Você escolheu a categoria filmes {nome_usuario}? S/N")

    if recomendar_filmes.lower() == "s":
        recomendacao = random.choice(list(filmes.keys()))
        ano = filmes[recomendacao][0]
        diretor = filmes[recomendacao][1]
        print(f"""Recomendação de filme:{recomendacao} 
                Ano de lançamento:{ano} 
                Diretor:{diretor}""")

        nota = input(f"Gostou da recomendação {nome_usuario}? S/N")
        if nota == "s":
                pass
        else:
                print(f"Agradecemos sua utilização {nome_usuario}")

    else:
        print(f"Alguma coisa deu errado {nome_usuario}, vamos tentar novamente?")

def recomendar_livros():
    recomendar_livros = input(f"Você escolheu a categoria livros {nome_usuario}?  S/N")

    if recomendar_livros.lower() == "s":
        recomendacao = random.choice(list(livros.keys()))
        ano = livros[recomendacao][0]
        autor = livros[recomendacao][1]
        print(f"""Recomendação de livro:{recomendacao} 
                  Ano de lançamento:{ano} 
                  Autor:{autor}""")

        nota = input(f"Gostou da recomendação {nome_usuario}? S/N")
        if nota == "s":
            pass
        else:
            print(f"Agradecemos sua utilização {nome_usuario}")


    else:
        print(f"Alguma coisa deu errado {nome_usuario}, vamos tentar novamente?")

def recomendar_games():
    recomendar_games = input(f"Você escolheu a categoria games {nome_usuario}? S/N")

    if recomendar_games.lower() == "s":
        recomendacao = random.choice(list(games.keys()))
        ano = games[recomendacao][0]
        diretor = games[recomendacao][1]
        print(f"""Recomendação de Game:{recomendacao} 
                Ano de lançamento:{ano} 
                Diretor:{diretor}""")

        continuar = input(f"Gostou da recomendação {nome_usuario}? S/N")

        nota = input(f"Gostou da recomendação {nome_usuario}? S/N")
        if nota == "s":
            pass
        else:
            print(f"Agradecemos sua utilização {nome_usuario}")

    else:
        print(f"Alguma coisa deu errado {nome_usuario}, vamos tentar novamente?")

def registrar_nota(categoria, titulo):

    pass#nota = input(f"Deseja colocar uma nota na recomendação que foi dada? S/N")
    #if nota.lower()== "s":
     #   valor_nota = int(input(f"Qual nota você deseja dar de 1 à 5 para a {recomendacao} {nome_usuario}? ")
       # valor_nota.append(nota)


filmes = {
    "Star Wars": ["1977", "George Lucas"],
    "O Guia Do Mochileiro das Galáxias": ["2005", "Garth Jennings"],
    "De Volta Para o Futuro": ["1985", "Robert Zemeckis"],
    "Duna": ["2021", "Denis Villeneuve"],
    "Jogador Nº 1": ["2018", "Steven Spielberg"],
    "Os Caça Fantasmas": ["1984", "Ivan Reitman"],
    "Matrix": ["1999", "Lana Wachowski, Lilly Wachowski"],
    "Akira": ["1991", "Katsuhiro Otomo"],
    "Interestrelar": ["2014", "Christopher Nolan"],
    "Blade Runner": ["1982", "Ridley Scott"],
    "Senhor dos Anéis": ["2001", "Peter Jackson"]
}

games = {
    "Mario Bros.": ["1983", "Shigeru Miyamoto, Gunpei Yokoi"],
    "Sonic the Hedgehog": ["1991", "Yuji Naka"],
    "The Legend of Zelda: Ocarina of Time": ["1998", "Shigeru Miyamoto, Koji Kondo, Eiji Aonuma, Yoshiaki Koizumi, Takashi Tezuka, Yoichi Yamada"],
    "Metroid": ["1986", "Gunpei Yokoi"],
    "Metal Slug": ["1996", "Nazca Corporation, SNK, Irem"],
    "Metal Gear": ["1987", "Hideo Kojima"],
    "Grand Theft Auto (GTA)": ["1997", "Rockstar North, Rockstar Lincoln, Visual Science, DMA Design"],
    "Tetris": ["1984", "Alexey Pajitnov, Sega, Spectrum Holobyte"],
    "Pac-Man": ["1980", "Toru Iwatani"],
    "Pokemon": ["1996", "Ken Sugimori, Satoshi Tajiri"]
}

livros = {
    "O Guia do Mochieliro Das Galáxias": ["1979", "Douglas Adams"],
    "O Senhor Dos Anéis": ["1954", "J. R. R. Tolkien"],
    "Duna": ["1965", "Frank Herbert"],
    "2001 - Uma Odisseia no espaço": ["1968", "Arthur C. Clarke"],
    "Jogos Vorazes": ["2008", "Suzanne Collins"],
    "Percy Jackson": ["2005", "Rick Riordan"],
    "Harry Potter": ["1997", "J. K. Rowling"],
    "Viagem ao Centro Da Terra": ["1864", "Júlio Verne"],
    "As Crônicas de Gelo e do Fogo": ["1996", "George R.R. Martin"],
    "Neuromancer": ["1984", "William Gibson"]
}


nome_usuario = input("Olá, Qual seu nome? ")
menu()



janela = Tk()

janela.title("Recomendador Geek")

texto_inicial = Label(janela, text="Seja bem vindo ao Recomendador GEEK ")
texto_orientacao.grid(column=0, row=0)

botao = Button(janela, text="Vamos começar?", command=menu)
botao.grid(column=0, row=1)

texto_menu = Label(janela, text="")
texto_menu.grid(column=0, row=2)


janela.mainloop()


