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

    return f"Decoração: {sugestao}"


def sugerir_cardapio(tipo_de_evento, convidados):
    opcoes = {
        "casamento": {
            "vegetariano": {
                "pequeno": ["Risoto de Gorgonzola com Pera e Nozes", "Ravioli de Búfala ao Molho Sugo com Manjericão"],
                "grande": [
                    "Ilha de Massas (Penne, Farfalle) com molhos variados (Queijo, Tomate, Funghi)",
                    "Buffet de Antepastos com queijos finos, frutas secas e pães artesanais",
                ],
            },
            "vegano": {
                "pequeno": [
                    "Moqueca de Palmito e Banana da Terra com farofa de dendê",
                    "Medalhão de Cogumelos com Risoto de Açafrão (sem queijo)",
                ],
                "grande": [
                    "Jantar Árabe Completo (Falafel, Homus, Tabule, Charuto de folha de uva sem carne)",
                    "Buffet de Feijoada Vegana com tofu defumado e couve mineira",
                ],
            },
            "kosher": {  # restrições judaícas
                "pequeno": [
                    "Salmão Grelhado com crosta de ervas e purê de mandioquinha (Parve)",
                    "Frango Assado ao molho de laranja com batatas coradas",
                ],
                "grande": [
                    "Estação de Carnes (Brisket e Rosbife) com acompanhamentos sem laticínios",
                    "Buffet de Peixes finos e saladas variadas (evitando mistura carne/leite)",
                ],
            },
            "halal": {  # restrições islâmicas
                "pequeno": [
                    "Cordeiro Assado lentamente com Cuscuz Marroquino",
                    "Kebab de Carne Bovina no prato com arroz de lentilhas",
                ],
                "grande": [
                    "Banquete Libanês com Kafta, Espetinhos de Frango e Arroz com Amêndoas",
                    "Estação de Shawarma com molhos típicos e pão pita fresco",
                ],
            },
            "sem restricao": {
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
        },
        "aniversario": {
            "vegetariano": {
                "pequeno": [
                    "Rodízio de Pizzas (Marguerita, 4 Queijos, Rúcula, Abobrinha)",
                    "Noite de Fondue de Queijo com pães e batatas",
                ],
                "grande": [
                    "Salgadinhos fritos e assados (Bolinha de queijo, Esfiha de ricota, Pastel de palmito)",
                    "Crepe Francês (vários recheios de queijos e vegetais)",
                ],
            },
            "vegano": {
                "pequeno": [
                    "Hambúrguer de Grão de Bico e Lentilha com maionese verde vegana",
                    "Nachos com Guacamole, Pico de Gallo e Chilli de soja",
                ],
                "grande": [
                    "Coxinha de Jaca e Kibe de Abóbora (volantes)",
                    "Ilha de 'Monte seu Taco' com recheios de cogumelos e feijão refrito",
                ],
            },
            "kosher": {  # restrições judaícas
                "pequeno": [
                    "Deli Judaica: Sanduíches de Pastrami e Corned Beef no pão de centeio",
                    "Hambúrguer de carne 100% bovina (sem queijo)",
                ],
                "grande": [
                    "Ilha de Falafel no pão pita com salada israelense e tahine",
                    "Churrasco Kosher (espetinhos variados e salsichões)",
                ],
            },
            "halal": {  # restrições islâmicas
                "pequeno": [
                    "Esfihas abertas (Carne e Zaatar) e Kibes fritos",
                    "Tábua de Grelhados Mistos (Frango e Carne Bovina)",
                ],
                "grande": [
                    "Rodízio de Mini Hambúrgueres (carne Halal certificada)",
                    "Festa Temática Árabe com salgados variados e doces sírios",
                ],
            },
            "sem restricao": {
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
        },
        "corporativo": {
            "vegetariano": {
                "pequeno": [
                    "Almoço executivo: Lasanha de Berinjela e Salada Caprese",
                    "Brunch com Quiches (Alho Poró, Tomate Seco) e frutas",
                ],
                "grande": [
                    "Sanduíches de Metro (opções: Pasta de Ovos, Queijo Branco, Rúcula)",
                    "Coffee Break com pães de queijo, bolos caseiros e salada de frutas",
                ],
            },
            "vegano": {
                "pequeno": ["Poke Bowl com Tofu, Manga, Pepino e Arroz Gohan", "Wrap de Hummus com vegetais grelhados"],
                "grande": [
                    "Kit Lanche Individual (Sanduíche de pasta de grão de bico, fruta e suco)",
                    "Buffet de Saladas completas e grãos (Quinoa, Grão de bico)",
                ],
            },
            "kosher": {  # restrições judaícas
                "pequeno": [
                    "Bagels com Salmão Defumado (Lox) e Cream Cheese",
                    "Almoço Executivo de Peixe (Tilápia ou Linguado)",
                ],
                "grande": [
                    "Mesa de Frios e Pães (Parve/Laticínios) sem carnes frias",
                    "Box Lunch certificado (Sanduíche de Peito de Peru Kosher)",
                ],
            },
            "halal": {  # restrições islâmicas
                "pequeno": [
                    "Prato feito: Arroz, Feijão, Bife Acebolado (carne Halal) e Salada",
                    "Marmita Executiva de Frango Grelhado com legumes",
                ],
                "grande": [
                    "Finger Foods (Samosas de carne e vegetais)",
                    "Buffet Self-Service com carnes certificadas (sem derivados de porco)",
                ],
            },
            "sem restricao": {
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
        },
        "generico": {
            "vegetariano": {
                "pequeno": ["Strogonoff de Palmito", "Omelete recheado com salada"],
                "grande": ["Massa Penne ao molho branco e vermelho", "Tortas Salgadas variadas"],
            },
            "vegano": {
                "pequeno": [
                    "Espaguete de Abobrinha ao molho bolonhesa de lentilha",
                    "Risoto de cogumelos sem manteiga",
                ],
                "grande": ["Arroz carreteiro vegano (com legumes e soja)", "Salpicão vegano com maionese de batata"],
            },
            "kosher": {  # restrições judaícas
                "pequeno": ["Frango assado com batatas", "Peixe ao forno com legumes"],
                "grande": ["Buffet de carnes assadas", "Sanduíches de carne fria"],
            },
            "halal": {  # restrições islâmicas
                "pequeno": ["Frango ao Curry com arroz", "Kibe de forno"],
                "grande": ["Estrogonofe de carne (Halal) e batata palha", "Arroz temperado com frango desfiado"],
            },
            "sem restricao": {
                "pequeno": ["Jantar em restaurante reservado", "Pizza e refrigerante"],
                "grande": ["Churrasco", "Salgados variados"],
            },
        },
    }

    if tipo_de_evento.lower() in opcoes:
        evento = opcoes[tipo_de_evento.lower()]
    else:
        evento = opcoes["generico"]

    restricao = input(">> Existe alguma restrição ao cardápio? (Vegano, vegetariano, kosher ou halal): ").lower()

    if restricao in evento:
        cardapio = evento[restricao]
    else:
        cardapio = evento["sem restricao"]

    if convidados > 50:
        tamanho = "grande"
    else:
        tamanho = "pequeno"

    sugestao = random.choice(cardapio[tamanho])

    return f"Cardápio ({tamanho}): {sugestao}"


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

    return f"Entretenimento: {sugestao}"
