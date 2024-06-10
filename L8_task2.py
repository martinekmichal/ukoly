def minimum(seznam):
    min = seznam[0]
    for cislo in seznam:
        if cislo < min:
            min = cislo
    return min

data_seznamu = [8,9,15,25,48,72,5]
print(f"Nejmenší číslo ze seznamu je: {minimum(data_seznamu)}")
