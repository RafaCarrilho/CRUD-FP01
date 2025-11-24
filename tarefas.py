from validacoes import validar_orcamento
from eventos import listar_eventos


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
                    try:
                        valor_tarefa = float(dados[2])
                    except ValueError:
                        continue

                    if nome_evento in repositorio:
                        if len(repositorio[nome_evento]) > 5:
                            repositorio[nome_evento][5].append({"nome": nome_tarefa, "valor": valor_tarefa})
    except Exception as e:
        print(f"Erro ao carregar tarefas: {e}")


def menu_tarefas(repositorio):
    print("\nPara qual evento deseja gerenciar tarefas?")
    listar_eventos(repositorio)
    nome = input("Nome do evento: ").lower()

    if nome not in repositorio:
        print("Evento não encontrado.")
        return

    while True:
        tarefas = repositorio[nome][5]

        total_gasto = sum(t["valor"] for t in tarefas)
        orcamento = repositorio[nome][3]
        saldo = orcamento - total_gasto

        print(f"\n--- Gerenciador: {nome.upper()} ---")
        print(f"Orçamento: R$ {orcamento:.2f}")
        print(f"Gasto Atual: R$ {total_gasto:.2f}")
        print(f"Saldo: R$ {saldo:.2f}")
        print("-" * 30)

        if not tarefas:
            print("  (Nenhuma despesa cadastrada)")
        else:
            for i, t in enumerate(tarefas):
                print(f"  {i + 1}. {t['nome']} -> R$ {t['valor']:.2f}")
        print("-" * 30)

        print("1. Adicionar Tarefa/Despesa")
        print("2. Remover Tarefa")
        print("0. Voltar")
        opcao = input("> ")

        if opcao == "1":
            nome_tarefa = input("Nome da despesa: ")
            nome_tarefa = nome_tarefa.replace(";", ",")
            valor_tarefa = validar_orcamento("Valor: R$ ")

            repositorio[nome][5].append({"nome": nome_tarefa, "valor": valor_tarefa})
            print("Tarefa adicionada!")

        elif opcao == "2":
            if not tarefas:
                print("Não há tarefas para remover.")
                continue
            try:
                numero = int(input("Número da tarefa para remover: "))
                index = numero - 1
                if 0 <= index < len(tarefas):
                    removido = tarefas.pop(index)
                    print(f"'{removido['nome']}' removida!")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Digite um número válido.")

        elif opcao == "0":
            break
