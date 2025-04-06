# função anonima

def nome_da_funcao():
    print('funcao_normal_sem_lambda')

nome_da_funcao()    

multiplicar_por_3 = lambda a:a*3

print(f'Multiplicação com o valor 5 = {multiplicar_por_3(5)}')

print(multiplicar_por_3(4))

soma = lambda a,b:a+b

print(soma(7, 7))