# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:


# Loop para armazenar participantes e seus temas
for _ in range(n):
    entrada = input().strip()
    participante, tema = [x.strip() for x in entrada.split(",")]
    if tema not in eventos:
        eventos[tema] = []
    eventos[tema].append(participante)


# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
