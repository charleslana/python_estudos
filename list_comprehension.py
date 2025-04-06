# sintaxe mais curta pra criar uma lista que já existe
# compreensão de lista

animais = ['cachorro', 'gato', 'tartaruga', 'girafa']

print(animais)

nova_lista = []

for animal in animais:
    if 't' in animal:
        nova_lista.append(animal)

print(nova_lista)

nova_lista_2 = [animal for animal in animais if 't' in animal]

print(nova_lista_2)