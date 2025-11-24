from datetime import datetime


def validar_data(mensagem):
    while True:
        try:
            data = input(mensagem)
            evento = datetime.strptime(data, "%d/%m/%Y").date()
            agora = datetime.now().date()

            if evento >= agora:
                break
            else:
                print("Erro: A data do evento não pode ser no passado!")
                continue
        except ValueError:
            print("Erro: Formato inválido ou data inexistente. Use DD/MM/AAAA.")
            continue
    return data


def validar_orcamento(mensagem):
    while True:
        try:
            orcamento = float(input(mensagem))
            if orcamento >= 0:
                break
            else:
                print("Erro: O orçamento não pode ser negativo.")
        except ValueError:
            print("Erro: Digite um valor numérico válido (use ponto para centavos).")
            continue
    return orcamento


def validar_convidados():
    while True:
        try:
            convidados = int(input("Quantos convidados para o evento: "))
            if convidados >= 0:
                break
            else:
                print("Erro: O número de convidados não pode ser negativo.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")
            continue
    return convidados
