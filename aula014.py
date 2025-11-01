'''for c in range (1, 10):
    print(c)
print("Fim")'''

'''c=1
while c< 10:
    print(c)
    c = c+1
print('fim')'''

n = 1
i = 0
p = 0
while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        if (n%2 != 0) :
            i = i+1
        else:
            p = p+1
print("Acabou!")
print("A quantidade de números pares foi {} e Impares foi {}.".format(p, i))