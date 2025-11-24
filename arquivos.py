def arquivoEventos(nome, tipo, local, orca, data, convid):
    try:
        with open("eventos.csv", "a", encoding="utf8") as file:
            file.write(f"Nome: {nome}\n")
            file.write(f"Tipo: {tipo}\n")
            file.write(f"Data: {data}\n")
            file.write(f"Local: {local}\n")
            file.write(f"Orçamento: {orca}\n")
            file.write(f"Convidados: {convid}\n")
    except Exception as e:
        print(f"Erro ao salvar evento no arquivo: {e}")


def arquivoTarefas(repositorio):
    try:
        with open("tarefas.csv", "w", encoding="utf8") as file:
            for nome_evento, dados in repositorio.items():
                if len(dados) > 5:
                    tarefas = dados[5]

                    for t in tarefas:
                        nome = t["nome"].replace(";", ",")
                        linha = f"{nome_evento};{nome};{t['valor']}\n"
                        file.write(linha)

        print("Tarefas salvas e atualizadas em 'tarefas.csv'!")
    except Exception as e:
        print(f"Erro ao salvar tarefas: {e}")
