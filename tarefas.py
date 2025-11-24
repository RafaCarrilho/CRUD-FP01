from validacoes import validar_orcamento

from eventos import display, listar_eventos


def carregar_tarefas(repositorio):
    try:
        with open("tarefas.csv", "r", encoding="utf8") as file:
            linhas = file.readlines()
            for linha in linhas:
                linha = linha.strip()
                if not linha:
                    continue

                dados = linha.split(";")
                if len(dados) == 3:
                    nome_evento = dados[0].lower()
                    nome_tarefa = dados[1]
                    valor_tarefa = float(dados[2])

                    if nome_evento in repositorio:
                        repositorio[nome_evento][4].append({"nome": nome_tarefa, "valor": valor_tarefa})
    except Exception as e:
        print(f"Erro ao carregar tarefas: {e}")


def salvar_tarefas(repositorio):
    try:
        with open("tarefas.csv", "w", encoding="utf8") as file:
            for nome_evento, dados in repositorio.items():
                tarefas = dados[4]
                for t in tarefas:
                    linha = f"{nome_evento};{t['nome']};{t['valor']}\n"
                    file.write(linha)
        print("Tarefas salvas em 'tarefas.csv'!")
    except Exception as e:
        print(f"Erro ao salvar tarefas: {e}")


def menu_tarefas(repositorio):
    print("Para qual evento deseja gerenciar tarefas?")
    listar_eventos(repositorio)
    nome = input("Nome do evento: ").lower()

    if nome not in repositorio:
        print("Evento não encontrado.")
        return

    while True:
        display(nome, repositorio)
        print("--- Gerenciador de Tarefas ---")
        print("1. Adicionar Tarefa/Despesa")
        print("2. Remover Tarefa")
        print("0. Voltar")
        opcao = input("> ")

        if opcao == "1":
            nome_tarefa = input("Nome da despesa: ")
            nome_tarefa = nome_tarefa.replace(";", ",")  # Isso aqui é importante pq eu estou usando o ; no .split()
            valor_tarefa = validar_orcamento("Valor: R$ ")

            repositorio[nome][4].append({"nome": nome_tarefa, "valor": valor_tarefa})
            print("Tarefa adicionada!")

        elif opcao == "2":
            tarefas = repositorio[nome][4]
            if not tarefas:
                print("Não há tarefas para remover.")
                continue
            try:
                index = int(input("Número da tarefa para remover: ")) - 1
                if 0 <= index < len(tarefas):
                    removido = tarefas.pop(index)
                    print(f"{removido['nome']} removida!")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Digite um número válido.")

        elif opcao == "0":
            break
