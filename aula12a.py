nome = str(input('Qual seu nome? '))
if nome == 'Andriele' :
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana Vitória' :
#aqui está diferenciando o acento.
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}'.format(nome))
#o else é opcional.