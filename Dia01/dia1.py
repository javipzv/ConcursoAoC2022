with open('input.txt', 'r') as f:
    lines = f.readlines()

suma = 0
sumas = []
for element in lines:
    if element == "\n":
        sumas += [suma]
        suma = 0
        continue
    suma += int(element)

max_cantidad = max(sumas)
lista_ordenada = sorted(sumas, reverse=True)
suma_top3 = sum(lista_ordenada[:3])

print(max_cantidad)
print(suma_top3)