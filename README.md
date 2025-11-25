
# 🎉 Organiza Festa

**Organiza Festa** é um sistema simples de **planejamento de eventos** desenvolvido em **Python** para ser executado e ter sua navegação através do terminal.  
O objetivo é ajudar pessoas no papel de organizadores de eventos com as diversas áreas de atuação — como controlar convidados, tarefas, fornecedores e orçamentos — ajudando a manter tudo sob controle de forma prática e eficiente.

---

## 📋 Funcionalidades

### 🗓️ 1. CRUD de Eventos

Utiliza de funções para **criar, visualizar, editar e excluir** eventos com as seguintes informações:

- Nome do evento  
- Tipo (aniversário, casamento, reunião, etc.)  
- Data  
- Local  
- Orçamento disponível  
- Número de Convidados  

### 💸 2. Tarefas e Orçamento

- Cadastre tarefas (decoração, buffet, música ao vivo, etc.)  
- Registre o custo de cada tarefa  
- O sistema atualiza automaticamente o **saldo restante do orçamento**

### ⏳ 3. Contagem Regressiva

- Mostra **quantos dias faltam** para o evento acontecer.

### 💾 4. Armazenamento de Dados

- Todos os dados são **salvos em arquivos `.csv`**, garantindo acesso posterior ao histórico de eventos e tarefas e garantindo a continuação das informações dos eventos após o programa ser reiniciado.

### 💡 5. Sugestões Personalizadas

- Com base no tipo do evento e número de convidados, o sistema sugere:
  - Decoração  
  - Cardápio  
  - Entretenimento  

---

## ⚙️ Requisitos Técnicos

- Desenvolvido em **Python**, **sem uso de bibliotecas externas** (exceto as listadas abaixo).  
- Interface por **linha de comando (terminal)**.

### Bibliotecas utilizadas

- `os` → para limpar o terminal
- `datetime` → para manipular datas  
- `random` → para sugestões e funcionalidades dinâmicas  

---

## 🧠 Boas Práticas Exigidas

O código contém:

- **Modularização** (uso de funções para evitar repetições)  
- **Tratamento de exceções**  
- **Código legivel**, com nomes claros de variáveis, funções e aplicação das boas práticas restantes

---

## Grupo 03

- Integrante 1: Arthur Vitorino
- Integrante 2: Juan Riquelme
- Integrante 3: Kelwin Karan
- Integrante 4: Pedro Bedor
- Integrante 5: Rafael Carrilho
- Integrante 6: Victor Carraly



# Manual De Uso

Este programa permite gerenciar eventos e tarefas através do terminal, utilizando o arquivo principal:
- main.py

### ▶️ Execução
- Navegue até o arquivo main.py dentro da pasta CRUD-FP01 que você baixou.

- Abra o terminal para o arquivo anteriormente mencionado!  


### 🧭 Menu Principal
Ao iniciar, o programa exibirá:  

1 - Criar evento  
2 - Listar eventos  
3 - Alterar Dados do Evento  
4 - Deletar Evento  
5 - Gerenciar Tarefas e Gastos  
6 - Salvar Tudo  
0 - Sair 

- Funções principais:

  - Criar evento: cadastra um novo evento.

  - Listar eventos: mostra eventos registrados.

  - Alterar evento: permite modificar dados de um evento.

  - Deletar Evento: Remove o evento anteriormente criado dos arquivos.

  - Gerenciar tarefas: acessa um submenu para criar, listar, editar e excluir tarefas.

  - Salvar tudo: grava manualmente as alterações nos arquivos .csv.

### 📂 Armazenamento
Todos os dados são automaticamente salvos nos arquivos

- eventos.csv –> eventos cadastrados  
- tarefas.csv –> tarefas cadastradas  

### ❗ Importante
- O programa salva automaticamente ao sair.  
- Use apenas o terminal para interação com o programa!
- Os arquivos.csv não devem ser editados manualmente devido a diferença de sua formatação.

\
[_Aperte aqui para ser redirecionado ao  
documento de exigências para o Organiza Festa_](https://docs.google.com/document/d/1xvYXM7tCDu6KCbbe0Si-3ugaNu-uH8AnQUj7vaEfAfA/edit?tab=t.0)  
