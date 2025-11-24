from datetime import datetime


def contagem_regressiva(data_do_evento):
    evento = datetime.strptime(data_do_evento, "%d/%m/%Y")
    agora = datetime.now()

    diferenca_dias = (evento - agora).days + 1
    rest_meses = diferenca_dias//30
    rest_dias = diferenca_dias%30

    anos = evento.year - agora.year
    meses = evento.month - agora.month
    total_meses = anos * 12 + meses

    if evento.day < agora.day:
        rest_meses -= 1
    if total_meses >= 1:
        rest_dias = diferenca_dias - (total_meses * 30)

    return f"Faltam {rest_meses} meses e {rest_dias} dias!"
