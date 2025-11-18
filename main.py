import os; os.system("cls")
import datetime;

def create ():
    lista=[]
    nome_evento=input("Nome do evento: ").lower()
    lista.append(nome_evento) #O primeiro elemento da Lista sempre vai ser o nome
            
    tipo_de_evento = input("Tipo de evento? (Caso não saiba, digite '-')")
    lista.append(tipo_de_evento)

    data_do_evento = input("Quando é a data do evento?  formato AAAA-MM-DD)")
    lista.append(data_do_evento)

    local_de_evento = input("Local de evento? ")
    lista.append(local_de_evento)

    orca_de_evento = float(input("Orçamento do evento? "))
    lista.append(orca_de_evento)
    return(lista)

def display (nome, repositorio):
    tipo = repositorio[nome][0]
    data = repositorio[nome][1]
    local = repositorio[nome][2]
    orca = repositorio[nome][3]
    print(f"Nome: {nome}")
    print(f"Tipo: {tipo}")
    print(f"Data: {data}")
    print(f"Local: {local}")
    print(f"Orçamento: {orca}\n")

def display_arquivo (nome, repositorio):
    tipo = repositorio[nome][0]
    data = repositorio[nome][1]
    local = repositorio[nome][2]
    orca = repositorio[nome][3]
    file=open ("Eventos.txt", 'a', encoding='utf8')
    file.writelines(f"Nome: {nome}\n")
    file.writelines(f"Tipo: {tipo}\n")
    file.writelines(f"Data: {data}\n")
    file.writelines(f"Local: {local}\n")
    file.writelines(f"Orçamento: {orca}\n\n")

def listar_eventos(repositorio):
    if not repositorio:
        print("Nenhum evento cadastrado.\n")
    else:
        print("\nEventos cadastrados:")
        for nome in repositorio:
            print(f"- {nome}")
        print()
def alterador (repositorio):
    try:
        print("Qual desses eventos vamos alterar?")
        listar_eventos(repositorio)
        chave=input().lower()
        if chave in repositorio: #Verifica se a chave solicitada está no repositório
            display (chave, repositorio)
            alterar=input(f"Qual desses vamos alterar?\n'1' para Nome\n'2' para Tipo\n'3' para Data\n'4' para Local\n'5' para Orçamento")
            if alterar == '1': #Se o cara quer trocar o nome do evento, eu salvo as "caracteristicas" em uma variavel e deleto o evento inteiro.
                tipo = repositorio[chave][0]
                data = repositorio[chave][1]
                local = repositorio[chave][2]
                orca = repositorio[chave][3]  
                repositorio.pop(chave)
                novo_nome=input("Digite o novo nome do evento: ") #Peço o novo nome
                repositorio[novo_nome]=[tipo,data,local,orca] #Crio um novo usando as variaveis que guardam as caracteristicas antigas
            elif alterar == '2': # A Partir daqui, só precisa alterar o tipo requisitado e não mudar a chave
                novo_tipo=input("Novo tipo de evento: ")
                repositorio[chave][0]=novo_tipo
            elif alterar == '3':
                nova_data=input("Nova data do evento: ")
                repositorio[chave][1]=nova_data
            elif alterar == '4':
                novo_local=input("Novo local do evento: ")
                repositorio[chave][2]=novo_local
            elif alterar == '5':
                novo_orca=float(input("Novo orçamento do evento: "))
                repositorio[chave][3]=novo_orca
    except:
            print()

def deletador (repositorio):
    print("Qual desses eventos vamos deletar?")
    listar_eventos(repositorio)
    deletar = input().lower()
    if deletar in repositorio:
        repositorio.pop(deletar)

repositorio = {}
while True:
    options = input("Digite:\n'1' para Criar\n'2' para Ler\n'3' para Alterar\n'4' para Deletar\n'0' para Encerrar\n")
    if options == '1':
        lista_recebida=create()
        repositorio [lista_recebida[0]]= lista_recebida[1:5] #Chave do repositório é o primeiro membro da lista, vulgo o nome do evento
        print (repositorio)
    
    elif options == '2':
        try:
            file=open ("Eventos.txt", 'w', encoding='utf8')
            for nome in repositorio: #Vamos ver todas as chaves e seus filhos por nome
                display_arquivo(nome,repositorio)
            file.close()
        except:
            print("Algum Erro")
    
    elif options  == '3':
        alterador(repositorio)
        
    elif options == '4':
        deletador(repositorio)
        
    elif options == '0':
        break





        
