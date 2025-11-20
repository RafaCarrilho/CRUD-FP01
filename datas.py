from datetime import datetime

def contagem_regressiva(data_do_evento):
    
    evento = datetime.strptime(data_do_evento, "%d/%m/%Y")
    agora = datetime.now()

    diferenca_dias = (evento - agora).days

    anos = evento.year - agora.year
    meses = evento.month - agora.month
    total_meses = anos * 12 + meses

    if evento.day < agora.day:
        total_meses -= 1
    if total_meses >= 1:
        diferenca_dias  = diferenca_dias - (total_meses*30)

    return total_meses, diferenca_dias

