def soucin(seznam):
    s = 1
    for cislo in seznam:
        s *= cislo
    return s

data = [5,6,4,8]
#print(soucin(data))
print(f"Task1 = {soucin(data)}")
print()
