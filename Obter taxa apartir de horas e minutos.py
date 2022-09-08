def taxa(h: int, m: int) -> float:
    if h >= 2:
        return 3.5 + ((h - 2) * 60 + m) / 60
    if h == 1:
        return 3.5 if m > 0 else 2.0
    return 2.0 if m > 0 else 0.0

Horas = int(input("Digite aqui as Horas: "))
Minutos = int(input("Digite aqui os Minutos: "))
print("Taxa: R$", taxa(Horas, Minutos))
