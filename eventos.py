from arquivos import adc_arquivo
from validacoes import validar_data, validar_orcamento, validar_nova_data, validar_novo_orcamento, validar_convidados


def create():
    lista = []
    nome_evento = input("Nome do evento: ").lower()
    lista.append(nome_evento)  # O primeiro elemento da Lista sempre vai ser o nome

    tipo_de_evento = input("Tipo de evento? (Caso não saiba, digite '-')")
    lista.append(tipo_de_evento)

    data_do_evento = validar_data()
    lista.append(data_do_evento)

    local_de_evento = input("Local de evento? ")
    lista.append(local_de_evento)

    orca_de_evento = validar_orcamento()
    lista.append(orca_de_evento)

    convidados_de_evento = validar_convidados()
    lista.append(convidados_de_evento)
    return lista


def display(nome, repositorio):
    tipo = repositorio[nome][0]
    data = repositorio[nome][1]
    local = repositorio[nome][2]
    orca = repositorio[nome][3]
    convid= repositorio[nome][4]
    print(f"Nome: {nome}")
    print(f"Tipo: {tipo}")
    print(f"Data: {data}")
    print(f"Local: {local}")
    print(f"Orçamento: {orca}")
    print(f"Convidados: {convid}\n")


def display_arquivo(nome, repositorio):
    tipo = repositorio[nome][0]
    data = repositorio[nome][1]
    local = repositorio[nome][2]
    orca = repositorio[nome][3]
    convid= repositorio[nome][4]
    adc_arquivo(nome, tipo, local, orca, data, convid)


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
        if chave in repositorio:  # Verifica se a chave solicitada está no repositório
            display(chave, repositorio)
            alterar = input(
                "Qual desses vamos alterar?\n'1' para Nome\n'2' para Tipo\n'3' para Data\n'4' para Local\n'5' para Orçamento\n'6' para Convidados"
            )
            if (
                alterar == "1"
            ):  # Se o cara quer trocar o nome do evento, eu salvo as "caracteristicas" em uma variavel e deleto o evento inteiro.
                tipo = repositorio[chave][0]
                data = repositorio[chave][1]
                local = repositorio[chave][2]
                orca = repositorio[chave][3]
                convid= repositorio[chave][4]
                repositorio.pop(chave)
                novo_nome = input("Digite o novo nome do evento: ")  # Peço o novo nome
                repositorio[novo_nome] = [
                    tipo,
                    data,
                    local,
                    orca,
                    convid
                ]  # Crio um novo usando as variaveis que guardam as caracteristicas antigas
            elif alterar == "2": # A Partir daqui, só precisa alterar o tipo requisitado e não mudar a chave
                novo_tipo = input("Novo tipo de evento: ")
                repositorio[chave][0] = novo_tipo
            elif alterar == "3":
                nova_data = validar_nova_data()
                repositorio[chave][1] = nova_data
            elif alterar == "4":
                novo_local=input("Novo local do evento: ")
                repositorio[chave][2] = novo_local
            elif alterar == "5":
                novo_orca = validar_novo_orcamento()
                repositorio[chave][3] = novo_orca
            elif alterar == "6":
                novo_convid = validar_convidados()
                repositorio[chave][4] = novo_convid
    except:
        print()


def deletador(repositorio):
    print("Qual desses eventos vamos deletar?")
    listar_eventos(repositorio)
    deletar = input().lower()
    if deletar in repositorio:
        repositorio.pop(deletar)
