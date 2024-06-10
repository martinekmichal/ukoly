def mocniny(seznam, exponent):
    vysledek = [cislo ** exponent for cislo in seznam]
    return vysledek

data_seznamu = [1, 2, 4, 5, 6, 7]
exponent = 2
vysledek = mocniny(data_seznamu, exponent)

print(f"Exponent: {exponent}\nVýsledek čísel: {vysledek}")

