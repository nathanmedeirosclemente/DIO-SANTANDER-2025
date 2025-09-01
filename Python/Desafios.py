def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))

    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    confirmadas = []
    recusadas = []
    disponiveis = set(quartos_disponiveis)
    for reserva in reservas_solicitadas:
        if reserva in disponiveis:
            confirmadas.append(reserva)
            disponiveis.remove(reserva)
        else:
            recusadas.append(reserva)
    if confirmadas:
        print("Reservas confirmadas:", " ".join(str(q) for q in confirmadas))
    else:
        print("Reservas confirmadas:")
    if recusadas:
        print("Reservas recusadas:", " ".join(str(q) for q in recusadas))
    else:
        print("Reservas recusadas:")


# Chamada da função principal
processar_reservas()
