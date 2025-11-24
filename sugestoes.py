import random


def sugerir_decoracao(tipo_de_evento):
    opcoes = {
        "casamento": [
            "Arranjos florais clássicos com rosas brancas e velas",
            "Estilo Rústico Chic com madeira e luzes de fada (varal de luzes)",
            "Minimalista com muitas folhagens verdes e tecidos drapeados",
            "Boho Chic com capim dos pampas e tapetes persas",
        ],
        "aniversario": [
            "Arco de balões desconstruído e painel de LED neon",
            "Temática 'Boteco' com toalhas xadrez e lousas de giz",
            "Estilo Tropical/Havaiano com cores vibrantes",
            "Decoração monocromática (All Black ou All White)",
        ],
        "corporativo": [
            "Ambiente clean com cores da marca e banners informativos",
            "Iluminação focal nos produtos e projetores de alta qualidade",
            "Mesas em formato de ilhas para facilitar o networking",
        ],
        "generico": ["Decoração neutra com flores da estação", "Iluminação cênica colorida"],
    }

    if tipo_de_evento.lower() in opcoes:
        evento = opcoes[tipo_de_evento.lower()]
    else:
        evento = opcoes["generico"]

    sugestao = random.choice(evento)

    return f"Sugestão de Decoração: {sugestao}"


def sugerir_cardapio(tipo_de_evento, convidados):
    opcoes = {
        "casamento": {
            "pequeno": [
                "Jantar empratado com opções de Filé Mignon ou Salmão",
                "Menu degustação em 5 tempos (Alta Gastronomia)",
                "Brunch sofisticado com mimosas e quiches",
            ],
            "grande": [
                "Buffet self-service com ilha de massas e risotos",
                "Ilha gastronômica com frios, pães e antepastos",
                "Coquetel volante com finger foods e mini porções",
            ],
        },
        "aniversario": {
            "pequeno": [
                "Rodízio de pizzas artesanais",
                "Noite de Hambúrguer (Monte o seu)",
                "Mesa de Comida Mexicana (Tacos e Nachos)",
            ],
            "grande": [
                "Salgadinhos tradicionais e docinhos variados",
                "Crepes feitos na hora (Doce e Salgado)",
                "Churrasco completo com guarnições",
            ],
        },
        "corporativo": {
            "pequeno": [
                "Coffee break reforçado (pães de queijo, bolos e sucos)",
                "Almoço executivo em restaurante parceiro",
            ],
            "grande": [
                "Coquetel de encerramento com espumante",
                "Brunch corporativo (manhã e tarde)",
                "Kit lanche individual (Sanduíche natural e fruta)",
            ],
        },
        "generico": {
            "pequeno": ["Jantar em restaurante reservado", "Pizza e refrigerante"],
            "grande": ["Churrasco", "Salgados variados"],
        },
    }

    if tipo_de_evento.lower() in opcoes:
        evento = opcoes[tipo_de_evento.lower()]
    else:
        evento = opcoes["generico"]

    if convidados > 50:
        tamanho = "grande"
    else:
        tamanho = "pequeno"

    sugestao = random.choice(evento[tamanho])

    return f"Sugestão de Cardápio ({tamanho}): {sugestao}"


def sugerir_entreten(tipo_de_evento):
    opcoes = {
        "casamento": [
            "Banda de baile ao vivo (Repertório variado)",
            "Quarteto de cordas para a cerimônia e Jazz para o jantar",
            "Cabine de fotos instantâneas para lembranças",
            "DJ Open Format com pista de dança interativa",
        ],
        "aniversario": [
            "DJ com playlist personalizada (Pop/Funk/Eletrônica)",
            "Karaokê com sistema de pontuação",
            "Barman fazendo drinks performáticos",
            "Plataforma 360º para vídeos",
        ],
        "corporativo": [
            "Música ambiente instrumental (Lo-fi ou Jazz)",
            "Palestras curtas estilo 'TED Talks'",
            "Dinâmicas de grupo rápidas (Quebra-gelo)",
        ],
        "generico": ["Playlist variada no Spotify", "Música ao vivo voz e violão"],
    }

    if tipo_de_evento.lower() in opcoes:
        evento = opcoes[tipo_de_evento.lower()]
    else:
        evento = opcoes["generico"]

    sugestao = random.choice(evento)

    return f"Sugestão de Entretenimento: {sugestao}"
