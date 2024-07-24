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

def recomendar():
    if categoria == 1:
        recomendar_filmes = input(f"Você escolheu a categoria {filmes} {nome_Usuario}? S/N")
        
        if recomendar_filmes.lower() == "s":
            recomendacao = random.choice(filmes)
            print(recomendacao)
        else:
            print(f"Alguma coisa deu errado {nome_usuario}, vamos tentar novamente?")

    elif categoria == 3:
        recomendar_games = input(f"Você escolheu a categoria {games}? S/N")

        if recomendar_games.lower() == "s":
            recomendacao = random.choice(games)
            print(recomendacao)

        else:
            print(f"Alguma coisa deu errado {nome_usuario}, vamos tentar novamente?")

    elif categoria == 2:
        recomendar_livros = input(f"Você escolheu a categoria {livros}? S/N")
        
        if recomendar_livros.lower() == "s":
            recomendacao = random.choice(livros)
            print(recomendacao)

        else:
            print(f"Alguma coisa deu errado {nome_usuario}, vamos tentar novamente?")



    

filmes = {}
games = {}
livros = {}

while True:
    
    nome_usuario = input("Olá, Qual seu nome?")
    categoria = input(f"""{nome_usuario} gostaria de recomendações de que tipo?
                  1 - Filmes
                  2 - Livros
                  3 - Games""")
    
    recomendar()


