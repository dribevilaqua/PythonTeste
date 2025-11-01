nome = input('Qual seu nome?')
print('Prazer te conhecer {:15}!'.format(nome))
#acima o :15 indica o número de caracteres que serão usados para escrever o nome, completando o que faltar com espaços.

nome = input ('Qual seu nome?')
print('Gostei de te conhecer {:>15}!'.format(nome))
#aqui o < indica que será alinhado a direita, assim < a esquerda, o ^ é centralizado.

nome = input('Qual seu nome?')
print('Prazer em te conhercer {:=^15}!'.format(nome))
#aqui tudo junto com o = preenchendo os espaços e centralizado

n1 = int(input("Digite um valor:"))
n2 = int(input("Digite outro valor:"))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1 // n2
e = n1**n2
print('A soma desses número é {}, o produto é {}, a divisão é {}'.format(s, m, d), end=' ')
print('A divisão inteira desses números é {}, \n a potência {}'.format(di, e))
#para limitar a casa decimais coloca dentro da {} exemplo: {:.3} para três casas decimais.
#end para mesma linha e \n para nova linha




