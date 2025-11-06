
def create ():
    lista=[]
    nome_evento=input("Nome do evento: ")
    lista.append(nome_evento)
            
    tipo_de_evento = input("Tipo de evento? (Caso não saiba, digite '-')")
    lista.append(tipo_de_evento)

    data_do_evento = input("Quando é a data do evento? (separe por barras '/' usando o formato DD/MM/AAAA)\n(Caso não saiba, digite '-')")
    lista.append(data_do_evento)

    local_de_evento = input("Local de evento? ")
    lista.append(local_de_evento)

    orca_de_evento = float(input("Orçamento do evento? "))
    lista.append(orca_de_evento)
    return(lista)

repositorio = {}
lista_recebida=create()

repositorio ["{lista_recebida[0]}"= lista_recebida[1:4]]