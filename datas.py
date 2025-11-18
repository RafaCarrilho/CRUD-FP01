from datetime import datetime

data_do_evento = input("Quando é a data do evento? (formato AAAA-MM-DD): ")

evento = datetime.strptime(data_do_evento, "%Y-%m-%d")

agora = datetime.now()

diferenca = evento - agora

dias = diferenca.days

print(f"Faltam: {dias} dias.")
