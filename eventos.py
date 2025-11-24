from arquivos import arquivoEventos
from datas import contagem_regressiva
from validacoes import validar_data, validar_orcamento, validar_convidados


def create():
    lista = []
    nome_evento = input("Nome do evento: ").lower()
    lista.append(nome_evento)

    tipo_de_evento = input("Tipo de evento? (ex: casamento, aniversario, corporativo): ")
    lista.append(tipo_de_evento)

    data_do_evento = validar_data("Quando é a data do evento? (formato DD/MM/AAAA): ")
    lista.append(data_do_evento)

    local_de_evento = input("Local de evento? ")
    lista.append(local_de_evento)

    orca_de_evento = validar_orcamento("Orçamento do evento: ")
    lista.append(orca_de_evento)

    convidados_de_evento = validar_convidados()
    lista.append(convidados_de_evento)

    lista.append([])

    return lista


def display(nome, repositorio):
    if nome in repositorio:
        tipo = repositorio[nome][0]
        data = repositorio[nome][1]
        contagem = contagem_regressiva(data)
        local = repositorio[nome][2]
        orca = repositorio[nome][3]
        convid = repositorio[nome][4]

        qtd_tarefas = len(repositorio[nome][5])

        print(f"Nome: {nome}")
        print(f"Tipo: {tipo}")
        print(f"Data: {data}")
        print(contagem)
        print(f"Local: {local}")
        print(f"Orçamento: R$ {orca:.2f}")
        print(f"Convidados: {convid}")
        print(f"Tarefas cadastradas: {qtd_tarefas}\n")
    else:
        print("Evento não encontrado.")


def display_arquivo(nome, repositorio):
    tipo = repositorio[nome][0]
    data = repositorio[nome][1]
    local = repositorio[nome][2]
    orca = repositorio[nome][3]
    convid = repositorio[nome][4]
    arquivoEventos(nome, tipo, local, orca, data, convid)


def listar_eventos(repositorio):
    if not repositorio:
        print("Nenhum evento cadastrado.\n")
    else:
        print("\nEventos cadastrados:")
        for nome in repositorio:
            print(f"- {nome}")
        print()


def alterador(repositorio):
    try:
        print("Qual desses eventos vamos alterar?")
        listar_eventos(repositorio)
        chave = input().lower()

        if chave in repositorio:
            display(chave, repositorio)
            print("Qual campo deseja alterar?")
            print("1. Nome")
            print("2. Tipo")
            print("3. Data")
            print("4. Local")
            print("5. Orçamento")
            print("6. Convidados")

            alterar = input("> ")

            if alterar == "1":
                tipo = repositorio[chave][0]
                data = repositorio[chave][1]
                local = repositorio[chave][2]
                orca = repositorio[chave][3]
                convid = repositorio[chave][4]
                tarefas = repositorio[chave][5]

                repositorio.pop(chave)

                novo_nome = input("Digite o novo nome do evento: ").lower()
                repositorio[novo_nome] = [tipo, data, local, orca, convid, tarefas]
                print("Nome alterado com sucesso!")

            elif alterar == "2":
                novo_tipo = input("Novo tipo de evento: ")
                repositorio[chave][0] = novo_tipo
            elif alterar == "3":
                nova_data = validar_data("Nova data (DD/MM/AAAA): ")
                repositorio[chave][1] = nova_data
            elif alterar == "4":
                novo_local = input("Novo local: ")
                repositorio[chave][2] = novo_local
            elif alterar == "5":
                novo_orca = validar_orcamento("Novo orçamento: ")
                repositorio[chave][3] = novo_orca
            elif alterar == "6":
                novo_convid = validar_convidados()
                repositorio[chave][4] = novo_convid

            print("Dado atualizado com sucesso!")
        else:
            print("Evento não encontrado.")
    except Exception as e:
        print(f"Erro ao alterar: {e}")


def deletador(repositorio):
    print("Qual desses eventos vamos deletar?")
    listar_eventos(repositorio)
    deletar = input().lower()
    if deletar in repositorio:
        repositorio.pop(deletar)
        print(f"Evento '{deletar}' removido.")
    else:
        print("Evento não encontrado.")
