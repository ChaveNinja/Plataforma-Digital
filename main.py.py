import json
import os

def carregar_usuarios():
    if not os.path.exists("usuarios.json"):
        return {}
    with open("usuarios.json", "r") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f, indent=4)

def cadastrar_usuario():
    usuarios = carregar_usuarios()
    email = input("Digite seu e-mail: ")
    if email in usuarios:
        print("Usuário já cadastrado.")
        return
    senha = input("Digite sua senha: ")
    usuarios[email] = {"senha": senha}
    salvar_usuarios(usuarios)
    print("Cadastro realizado com sucesso!")

def login():
    usuarios = carregar_usuarios()
    email = input("E-mail: ")
    senha = input("Senha: ")
    if email in usuarios and usuarios[email]["senha"] == senha:
        print(f"Bem-vindo, {email}!")
        return True
    else:
        print("Usuário ou senha inválidos.")
        return False
def mostrar_cursos():
    cursos = {
        1: "Introdução à Lógica",
        2: "Variáveis e Tipos em Python",
        3: "Estruturas de Decisão (if/else)",
        4: "Laços de Repetição (for e while)",
        5: "Segurança Digital Básica"
    }
    print("\n--- Cursos Disponíveis ---")
    for k, v in cursos.items():
        print(f"{k}. {v}")
    escolha = int(input("Digite o número do curso que deseja ver: "))
    if escolha in cursos:
        print(f"\nAula: {cursos[escolha]}")
    if escolha in cursos:
            print(f"Aula: {cursos[escolha]}")
            if escolha == 1:
                print("""Introdução à Lógica:
A lógica é a base do pensamento computacional. Ela envolve a construção de argumentos válidos, utilizando proposições, conectivos lógicos (como E, OU, NÃO) e regras para inferência. Em programação, a lógica nos permite criar condições e tomar decisões de forma estruturada e previsível.""")
            elif escolha == 2:
                print("""Variáveis e Tipos em Python:
Variáveis são nomes que armazenam valores. Em Python, você pode criar variáveis sem declarar o tipo:
ex: nome = "João", idade = 25.
Os tipos mais comuns são: int (números inteiros), float (números decimais), str (texto), bool (verdadeiro ou falso). Python é uma linguagem de tipagem dinâmica.""")
            elif escolha == 3:
                print("""Estruturas de Decisão (if/else):
Com if e else, seu programa pode tomar decisões com base em condições.
Exemplo:
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
Essas estruturas permitem que seu programa reaja de forma diferente de acordo com a entrada do usuário.""")
            elif escolha == 4:
                print("""Laços de Repetição (for e while):
Loops permitem repetir ações automaticamente. O 'for' percorre sequências:
for i in range(5):
    print(i)
O 'while' repete enquanto uma condição for verdadeira:
while condicao:
    faça_algo()
Eles são úteis para percorrer listas, realizar cálculos repetitivos e muito mais.""")
            elif escolha == 5:
                print("""Segurança Digital Básica:
A segurança digital protege seus dados contra acessos indevidos. Conceitos importantes incluem:
- Senhas fortes e únicas
- Autenticação em duas etapas
- Evitar clicar em links suspeitos
- Atualizar softwares regularmente
A segurança começa com hábitos conscientes ao usar a internet.""")

    else:
        print("Curso inválido.")
def aplicar_quiz():
    perguntas = [
        {
            "pergunta": "Qual estrutura é usada para repetir blocos de código em Lógica de Programação?",
            "opcoes": ["A) if", "B) while", "C) break", "D) def"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual componente é essencial para conectar um computador à rede?",
            "opcoes": ["A) Placa de vídeo", "B) SSD", "C) Placa de rede", "D) Fonte de alimentação"],
            "resposta": "C"
        },
        {
            "pergunta": "O que é uma chave primária em Banco de Dados?",
            "opcoes": ["A) Um campo que aceita valores nulos", 
                       "B) Um campo que armazena imagens", 
                       "C) Um campo que identifica unicamente cada registro", 
                       "D) Um campo que pode se repetir"],
            "resposta": "C"
        },
        {
            "pergunta": "Qual protocolo é usado para envio de pacotes na internet?",
            "opcoes": ["A) HTML", "B) TCP/IP", "C) SQL", "D) HTTP"],
            "resposta": "B"
        },
        {
            "pergunta": "Na Engenharia de Software, qual fase define os requisitos do sistema?",
            "opcoes": ["A) Codificação", "B) Testes", "C) Levantamento de requisitos", "D) Deploy"],
            "resposta": "C"
        }
    ]

    print("=== Quiz de Conhecimentos Técnicos ===")
    acertos = 0

    for i, p in enumerate(perguntas, 1):
        print(f"\n{i}) {p['pergunta']}")
        for opcao in p["opcoes"]:
            print(opcao)
        resposta = input("Sua resposta: ").strip().upper()
        if resposta == p["resposta"]:
            print("✅ Correto!")
            acertos += 1
        else:
            print(f"❌ Errado! A resposta correta é {p['resposta']}.")

    total = len(perguntas)
    media = (acertos / total) * 10
    print(f"\nVocê acertou {acertos} de {total} perguntas.")
    print(f"Sua média final é: {media:.2f}")

def menu():
    while True:
        print("\n=== Plataforma de Educação Digital ===")
        print("1. Cadastrar")
        print("2. Login")
        print("3 Realizar Quiz")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "3":
            aplicar_quiz()
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            if login():
                mostrar_cursos()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
