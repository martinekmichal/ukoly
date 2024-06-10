def prvocislo_1(cislo):
    if cislo <= 1:
        return False
    if cislo == 2:
        return True
    if cislo % 2 == 0:
        return False
    m_d = int(cislo ** 0.5) + 1
    for delitel in range(3, m_d, 2):
        if cislo % delitel == 0:
            return False

    return True

def prvocislo(seznam):
    p = 0
    for cislo in seznam:
        if prvocislo_1(cislo):
            p += 1
    return p

data_seznamu = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(f"Počet prvočísel je: {prvocislo(data_seznamu)}")
