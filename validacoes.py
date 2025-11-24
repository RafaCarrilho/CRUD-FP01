from datetime import datetime

def validar_data(mensagem):
    while True:
        try:
            # tenta transformar a data, caso consiga vai retornar, se nao conseguir vai pedir outra data
            data = input(mensagem)
            evento = datetime.strptime(data, "%d/%m/%Y")
            agora = datetime.now()
            if (evento - agora).days >= 0:
                break
            else:
                print("data inválida")
                continue
        except ValueError:
            # Se der erro, o formato ou a data são inválidos
            print("data inválida")
            continue
    return data

def validar_orcamento(mensagem):
    while True:
        try:
            orcamento = float(input(mensagem))
            break
        except ValueError:
            print("valor inválido")
            continue
    return orcamento

def validar_convidados():
    while True:
        try:
            convidados = int(input("quantos convidados para o evento: "))
            break
        except ValueError:
            print("valor inválido")
            continue
    return convidados
