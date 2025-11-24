def arquivoEventos(nome, tipo, local, orca, data, convid):
    file = open("eventos.csv", "a", encoding="utf8")
    file.writelines(f"Nome: {nome}\n")
    file.writelines(f"Tipo: {tipo}\n")
    file.writelines(f"Data: {data}\n")
    file.writelines(f"Local: {local}\n")
    file.writelines(f"Orçamento: {orca}\n")
    file.writelines(f"Convidados: {convid}\n\n")
    file.close()

def arquivoTarefas(repositorio):
    try:
        with open("tarefas.csv", "a", encoding="utf8") as file:
            for nome_evento, dados in repositorio.items():
                tarefas = dados[4]
                for t in tarefas:
                    linha = f"{nome_evento};{t['nome']};{t['valor']}\n"
                    file.write(linha)
        print("Tarefas salvas em 'tarefas.csv'!")
    except Exception as e:
        print(f"Erro ao salvar tarefas: {e}")
