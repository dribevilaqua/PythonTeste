for c in range(0, 8, 2):
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('FIM')

i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
#começa no inicio, vai até o fim +1, vai pulando de passo em passo.