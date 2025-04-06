list = ['cachorro', 'pato', 'gato']

list_2 = ['elefante', 'girafa']

sum_list = list + list_2

print(sum_list)

# ordem alfabetica

sum_list.sort()

print(sum_list)

# ordem decrescente

sum_list.reverse()

print(sum_list)

check = 'pato' in sum_list

print(check)

numeros = [10, 50, 40, 10]

print(sum(numeros))

# append acrescenta no final da lista

numeros.append(100)

print(numeros)

print(numeros.count(10))

print(numeros.index(10))

# insert acrescenta no primeiro index

print(numeros.insert(0, '200'))

print(numeros)

numeros.remove(10)

print(numeros)

# remove o valor na posição 0 (que é o 200)

del numeros[0]
print(numeros)

# usando o pop removendo o ultimo da lista

numeros.pop(-1)

print(numeros)