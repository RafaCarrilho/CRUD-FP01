def adc_arquivo(nome, tipo, local, orca, data, convid):
    file = open("eventos.csv", "a", encoding="utf8")
    file.writelines(f"Nome: {nome}\n")
    file.writelines(f"Tipo: {tipo}\n")
    file.writelines(f"Data: {data}\n")
    file.writelines(f"Local: {local}\n")
    file.writelines(f"Orçamento: {orca}\n")
    file.writelines(f"Convidados: {convid}\n\n")
    file.close()
