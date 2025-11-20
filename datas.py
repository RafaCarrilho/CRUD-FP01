from datetime import datetime

data_do_evento = input("Quando é a data do evento? (formato DD/MM/AAAA): ")

evento = datetime.strptime(data_do_evento, "%d/%m/%Y")

agora = datetime.now()

diferenca = evento - agora

dias = diferenca.days

print(f"Faltam: {dias} dias.")
