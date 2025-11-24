from datetime import datetime

def validar_data():
    while True:
        try:
            # tenta transformar a data, caso consiga vai retornar, se nao conseguir vai pedir outra data
            data = input("Quando é a data do evento? (formato DD/MM/AAAA): ")
            evento = datetime.strptime(data, "%d/%m/%Y")
            agora = datetime.now()
            if (evento - agora).days > 0:
                break
            else:
                print("data inválida")
                continue
        except ValueError:
            # Se der erro, o formato ou a data são inválidos
            print("data inválida")
            continue
    return data

def validar_orcamento():
    while True:
        try:
            orcamento = float(input("qual o orcamento do evento: "))
            break
        except ValueError:
            print("valor inválido")
            continue
    return orcamento

def validar_nova_data():
    while True:
        try:
            # tenta transformar a data, caso consiga vai retornar, se nao conseguir vai pedir outra data
            data = input("Nova data do evento (formato DD/MM/AAAA): ")
            evento = datetime.strptime(data, "%d/%m/%Y")
            agora = datetime.now()
            if (evento - agora).days > 0:
                break
            else:
                print("data inválida")
                continue
        except ValueError:
            # Se der erro, o formato ou a data são inválidos
            print("data inválida")
            continue
    return data
    
def validar_novo_orcamento():
    while True:
        try:
            orcamento = float(input("Novo orçamento do evento: "))
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
