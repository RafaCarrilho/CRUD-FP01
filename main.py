import os
import datetime
from eventos import (
    create,
    display,
    display_arquivo,
    listar_eventos,
    alterador,
    deletador,
)


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


limpar_tela()
repositorio = {}
while True:
    options = input("Digite:\n'1' para Criar\n'2' para Ler\n'3' para Alterar\n'4' para Deletar\n'0' para Encerrar\n")
    if options == "1":
        lista_recebida = create()
        repositorio[lista_recebida[0]] = lista_recebida[
            1:6
        ]  # Chave do repositório é o primeiro membro da lista, vulgo o nome do evento
        print(repositorio)

    elif options == "2":
        try:
            file = open("eventos.csv", "w", encoding="utf8")
            for nome in repositorio:  # Vamos ver todas as chaves e seus filhos por nome
                display_arquivo(nome, repositorio)
            file.close()
        except:
            print("Algum Erro")

    elif options == "3":
        alterador(repositorio)

    elif options == "4":
        deletador(repositorio)

    elif options == "0":
        break
