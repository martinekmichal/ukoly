def smaz_cislo(seznam, c_smazani):
    pocet_smazanych = 0
    for c_smazani in seznam:
        seznam.remove(c_smazani)
        pocet_smazanych += 1
    return pocet_smazanych

data_seznam = [2, 5, 6, 8, 7, 10, 11, 5, 8, 13, 4, 9]
c_smazani = int(input("Zadej číslo na smazani: "))

print(smaz_cislo(data_seznam, c_smazani))
print(f"Seznam obsahuje: {data_seznam}")
