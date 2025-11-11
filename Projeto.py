
def create ():
    lista=[]
    nome_evento=input("Nome do evento: ").lower()
    lista.append(nome_evento)
            
    tipo_de_evento = input("Tipo de evento? (Caso não saiba, digite '-')")
    lista.append(tipo_de_evento)

    data_do_evento = input("Quando é a data do evento?  formato DD-MM-AAAA)")
    lista.append(data_do_evento)

    local_de_evento = input("Local de evento? ")
    lista.append(local_de_evento)

    orca_de_evento = float(input("Orçamento do evento? "))
    lista.append(orca_de_evento)
    return(lista)

repositorio = {}
while True:
    options = input("Digite:\n'1' para Criar\n'2' para Ler\n'3' para Alterar\n'4' para Deletar\n'0' para Encerrar")
    if options == '1':
        lista_recebida=create()
        repositorio [lista_recebida[0]]= lista_recebida[1:5]
        print (repositorio)
    if options == '2':
        try:
            for nome in repositorio:
                tipo = repositorio[nome][0]
                data = repositorio[nome][1]
                local = repositorio[nome][2]
                orca = repositorio[nome][3]
                print(f"Nome: {nome}")
                print(f"Tipo: {tipo}")
                print(f"Data: {data}")
                print(f"Local: {local}")
                print(f"Orçamento: {orca}\n")
        except:
            print()
    elif options  == '3':
        try:
            print("Qual desses eventos vamos alterar?")
            for nome in repositorio:
                print(nome)
            print()
            ipt=input().lower()
            if ipt in repositorio:
                tipo = repositorio[ipt][0]
                data = repositorio[ipt][1]
                local = repositorio[ipt][2]
                orca = repositorio[ipt][3]
                print(f"Nome: {ipt}")
                print(f"Tipo: {tipo}")
                print(f"Data: {data}")
                print(f"Local: {local}")
                print(f"Orçamento: {orca}\n")
                ipt1=input(f"Qual desses vamos alterar?\n'1' para Nome\n'2' para Tipo\n'3' para Data\n'4' para Local\n'5' para Orçamento")
                if ipt1 == '1':
                    tipo = repositorio[ipt][0]
                    data = repositorio[ipt][1]
                    local = repositorio[ipt][2]
                    orca = repositorio[ipt][3]
                    repositorio.pop(ipt)
                    novo_nome=input("Digite o novo nome do evento: ")
                    repositorio[novo_nome]=[tipo,data,local,orca]
                elif ipt1 == '2':
                    novo_tipo=input("Novo tipo de evento: ")
                    repositorio[ipt][0]=novo_tipo
                elif ipt1 == '3':
                    nova_data=input("Nova data do evento: ")
                    repositorio[ipt][1]=nova_data
                elif ipt1 == '4':
                    novo_local=input("Novo local do evento: ")
                    repositorio[ipt][2]=novo_local
                elif ipt1 == '5':
                    novo_orca=float(input("Novo orçamento do evento: "))
                    repositorio[ipt][3]=novo_orca
        except:
            print()



        