#1. Definição e Planejamento
#Objetivo: Criar um programa que sugere categorias e recomendações baseadas no interesse do usuário em conteúdo geek.

#Etapas do Planejamento:

#2. Estrutura do Projeto
#Componentes do Sistema:

#Interface de Usuário (UI):

#Terminal ou interface gráfica simples para interação.
#Receber entradas do usuário e exibir sugestões.
#Banco de Dados ou Estrutura de Dados:

#Armazenar listas de séries, filmes, animes e livros.
#Pode ser um simples arquivo JSON ou um banco de dados leve como SQLite.
#Lógica de Recomendação:

#Algoritmo para sugerir categorias baseadas na entrada do usuário.
#Algoritmo para fornecer recomendações dentro de uma categoria específica.
#3. Tecnologias e Ferramentas
#Linguagem de Programação:

#Python: Por sua simplicidade e vasto ecossistema de bibliotecas, como pandas para manipulação de dados e Tkinter para interfaces gráficas.
#Bibliotecas e Frameworks:

#Input/Output: Utilizar input() para receber entradas e print() para exibir resultados no terminal.
#JSON ou SQLite: Para armazenar e recuperar dados de recomendações.
#Tkinter: Para criar uma interface gráfica simples (opcional).
#Numpy/Pandas: Para manipulação de dados se necessário.
#IDE e Ferramentas de Desenvolvimento:

#VS Code ou PyCharm: IDEs populares para desenvolver em Python.
#Git: Controle de versão para gerenciar o código.
#4. Desenvolvimento do Projeto
#Etapas de Implementação:

#Configuração do Ambiente: Configure seu ambiente de desenvolvimento com as bibliotecas necessárias.
#Desenvolvimento da UI:
#Crie um menu inicial que solicita ao usuário para inserir suas preferências.
##Exiba as categorias sugeridas com base nas entradas do usuário.
#Implementação da Lógica de Recomendação:
#Desenvolva funções para analisar a entrada do usuário e sugerir categorias.
#Implemente a lógica para fornecer recomendações dentro de uma categoria específica.
#Banco de Dados:
#Estruture e preencha o arquivo JSON ou banco de dados com as listas de recomendações.
#Crie funções para buscar dados do banco de dados.
#5. Testes e Validação
#Etapas de Teste:

#Testes Unitários: Teste cada função individualmente para garantir que elas funcionem como esperado.
#Testes de Integração: Teste o sistema como um todo para garantir que os componentes funcionem bem juntos.
#Feedback de Usuário: Se possível, peça a amigos ou colegas para testarem o programa e fornecerem feedback.
#6. Documentação e Publicação
#Etapas de Documentação:

#Documentação do Código: Comente o código e escreva documentação para explicar a funcionalidade de cada parte do programa.
#Postagem no Blog: Crie uma postagem detalhada no blog explicando o projeto, como ele funciona, e forneça exemplos de uso.
#7. Manutenção e Atualização
#Etapas de Manutenção:

#Correção de Bugs: Resolva quaisquer problemas que surgirem após a implementação inicial.
#Atualizações: Adicione novas funcionalidades ou categorias de recomendações conforme necessário.

import random


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
                notas()
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
            notas()
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
            notas()
        else:
            print(f"Agradecemos sua utilização {nome_usuario}")

    else:
        print(f"Alguma coisa deu errado {nome_usuario}, vamos tentar novamente?")

def notas():
    pass

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
    "O Guai do Mochieliro Das Galáxias": ["1979", "Douglas Adams"],
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

while True:

    categoria = int(input(f"""{nome_usuario} gostaria de recomendações de que tipo?"
                  1 - Filmes
                  2 - Livros
                  3 - Games"""))

    if categoria == 1:
        recomendar_filmes()


    elif categoria == 2:
        recomendar_livros()

    elif categoria == 3:
        recomendar_games()
