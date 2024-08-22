import random
import json
import tkinter

with open('banco_de_dados.json', 'r') as f:
    dados = json.load(f)

filmes = dados["filmes"]
livros = dados["livros"]
games = dados["games"]
notas = dados["notas"]


def menu():
    while True:

        categoria = int(input(f"""{nome_usuario} gostaria de recomendações de que tipo?"
    1 - Filmes
    2 - Livros
    3 - Games
    4 - Sair
    """))

        if categoria == 1:
            recomendar_filmes()

        elif categoria == 2:
            recomendar_livros()

        elif categoria == 3:
            recomendar_games()

        elif categoria == 4:
            print(f"Obrigado por utilizar nosso recomendador {nome_usuario}.")
            break

def recomendar_filmes():
    recomendar_filmes = input(f"Você escolheu a categoria filmes {nome_usuario}? S/N").strip().lower()

    if recomendar_filmes.lower() == "s":
        recomendacao = random.choice(list(filmes.keys()))
        ano = filmes[recomendacao][0]
        diretor = filmes[recomendacao][1]
        print(f"""Recomendação de filme:{recomendacao} 
                Ano de lançamento:{ano} 
                Diretor:{diretor}
                Nota do Titulo: {media_de_nota("filmes", recomendacao)}""")



        registrar_nota = input(f"Gostou da recomendação {nome_usuario}? S/N").strip().lower()
        if registrar_nota == "s":
            registro_de_nota("filmes", recomendacao)

        else:
                print(f"Agradecemos sua utilização {nome_usuario}")

    else:
        print(f"Alguma coisa deu errado {nome_usuario}, vamos tentar novamente?")

def recomendar_livros():
    recomendar_livros = input(f"Você escolheu a categoria livros {nome_usuario}?  S/N").strip().lower()

    if recomendar_livros.lower() == "s":
        recomendacao = random.choice(list(livros.keys()))
        ano = livros[recomendacao][0]
        autor = livros[recomendacao][1]
        print(f"""Recomendação de livro:{recomendacao} 
                  Ano de lançamento:{ano} 
                  Autor:{autor}
                  Nota do Titulo: {media_de_nota("livros", recomendacao)}""")

        nota = input(f"Gostou da recomendação {nome_usuario}? S/N").strip().lower()
        if nota == "s":
            registro_de_nota("livros", recomendacao)

        else:
            print(f"Agradecemos sua utilização {nome_usuario}")


    else:
        print(f"Alguma coisa deu errado {nome_usuario}, vamos tentar novamente?")

def recomendar_games():
    recomendar_games = input(f"Você escolheu a categoria games {nome_usuario}? S/N").strip().lower()

    if recomendar_games == "s":
        recomendacao = random.choice(list(games.keys()))
        ano = games[recomendacao][0]
        diretor = games[recomendacao][1]
        print(f"""Recomendação de Game:{recomendacao} 
                Ano de lançamento:{ano} 
                Diretor:{diretor}
                Nota do titulo: {media_de_nota("games", recomendacao)} """)


        nota = input(f"Gostou da recomendação {nome_usuario}? S/N")
        if nota == "s":
            registro_de_nota("games", recomendacao)
        media_de_nota("games", recomendacao)

    else:
        print(f"Alguma coisa deu errado {nome_usuario}, vamos tentar novamente?")

def registro_de_nota(categoria, titulo):
    nota = float(input("Por favor, avalie de 1 a 5: "))
    if 1 <= nota <= 5:
        if categoria not in notas[categoria]:

            notas[categoria][titulo] = []
        notas[categoria][titulo].append(nota)
    else:
        print(f"resgistro não contabilizado, tente novamente...")

def media_de_nota(categoria, titulo):
    if categoria in notas and titulo in notas[categoria]:
        lista_notas = notas[categoria][titulo]

        if lista_notas:
            media = sum(lista_notas) / len(lista_notas)
            print(f"A média das notas para '{titulo}' na categoria '{categoria}' é {media:.1f}")
        else:
            print(f"Não há notas registradas para '{titulo}' na categoria '{categoria}'.")
    else:
        print(f"Categoria '{categoria}' ou título '{titulo}' não encontrado(s).")

filmes = {}

games = {}

livros = {}

notas = {
    "filmes": {},

    "games": {},

    "livros": {}

}

dados = {
    "filmes": filmes,
    "livros": livros,
    "games": games,
    "notas": notas
}

with open("banco_de_dados.json", "w") as f:
    json.dump(dados, f)


Tk = tkinter




nome_usuario = input("Olá, Qual seu nome? ")
menu()


