from datetime import datetime


def contagem_regressiva(data_do_evento):
    try:
        evento = datetime.strptime(data_do_evento, "%d/%m/%Y").date()
        agora = datetime.now().date()

        if evento < agora:
            return "O evento já ocorreu!"

        if evento == agora:
            return "É hoje!"

        diferenca_dias = (evento - agora).days

        if diferenca_dias >= 30:
            meses = diferenca_dias // 30
            dias_rest = diferenca_dias % 30
            return f"Faltam aproximadamente {meses} meses e {dias_rest} dias!"
        else:
            return f"Faltam {diferenca_dias} dias!"

    except ValueError:
        return "Data inválida"
