def maksos(lista):
    licznik = 1
    naj = 0
    for i in range(1, len(lista)):
        if lista[i]-lista[i-1] <= 3:
            licznik += 1
        else:
            if licznik > naj:
                naj = licznik
            licznik = 1
    if lista[0] < 3:
        licznik += 1
        i = 1
        while i < len(lista) and lista[i] - lista[i-1] <= 3:
            licznik += 1
            i += 1
    if licznik > naj:
        naj = licznik
    if naj == 2 * len(lista):
        return len(lista)
    return naj
