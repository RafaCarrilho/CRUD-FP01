import os
from eventos import (
    create,
    display,
    display_arquivo,
    listar_eventos,
    alterador,
    deletador,
)
from tarefas import menu_tarefas, carregar_tarefas
from arquivos import arquivoTarefas


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def carregar_dados():
    repositorio_temp = {}

    if os.path.exists("eventos.csv"):
        try:
            with open("eventos.csv", "r", encoding="utf8") as file:
                linhas = [linha.strip() for linha in file.readlines() if linha.strip()]

                step = 6

                for i in range(0, len(linhas), step):
                    try:
                        if i + 5 < len(linhas):
                            nome = linhas[i].split(":")[1].strip().lower()
                            tipo = linhas[i + 1].split(":")[1].strip()
                            data = linhas[i + 2].split(":")[1].strip()
                            local = linhas[i + 3].split(":")[1].strip()
                            orca = float(linhas[i + 4].split(":")[1].strip())
                            convid = int(linhas[i + 5].split(":")[1].strip())

                            repositorio_temp[nome] = [tipo, data, local, orca, convid, []]

                    except (IndexError, ValueError) as e:
                        print(f"Erro ao ler registro na linha {i}: {e}")
                        continue
        except Exception as e:
            print(f"Erro crítico ao abrir arquivo: {e}")

    carregar_tarefas(repositorio_temp)

    return repositorio_temp


def salvar_tudo(repositorio):
    try:
        with open("eventos.csv", "w", encoding="utf8") as file:
            pass

        print("Salvando eventos...")
        for nome in repositorio:
            display_arquivo(nome, repositorio)

        arquivoTarefas(repositorio)

    except Exception as e:
        print(f"Erro ao salvar dados: {e}")


# --- Início do Programa ---
limpar_tela()
print("Bem-vindo ao Organiza Festa!")
repositorio = carregar_dados()

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Criar Evento")
    print("2. Listar Eventos (Visualizar)")
    print("3. Alterar Dados do Evento")
    print("4. Deletar Evento")
    print("5. Gerenciar Tarefas e Gastos")
    print("6. Salvar Tudo")
    print("0. Sair")

    options = input("> ")

    if options == "1":
        lista = create()

        repositorio[lista[0]] = lista[1:]
        print("Evento criado com sucesso!")

    elif options == "2":
        limpar_tela()
        listar_eventos(repositorio)
        if repositorio:
            detalhar = input("Digite o nome para ver detalhes (ou Enter para voltar): ").lower()
            if detalhar in repositorio:
                display(detalhar, repositorio)

    elif options == "3":
        alterador(repositorio)

    elif options == "4":
        deletador(repositorio)

    elif options == "5":
        menu_tarefas(repositorio)

    elif options == "6":
        salvar_tudo(repositorio)

    elif options == "0":
        print("Salvando dados antes de sair...")
        salvar_tudo(repositorio)
        break

    else:
        print("Opção inválida.")
