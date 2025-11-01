print('\033[0;30;41mOlá mundo!')
#para cor não ir até o final tirar usando a formatação novamente \033[m
print('\033[4;33;44m Olá mundo! \033[m')
print('\033[1;35;43m Olá mundo! \033[m')
print('\033[30;42m Olá mundo! \033[m')
print('\033[m Olá mundo! \033[m')
#o de cima volta para configuração padrã
print('\033[7;30m Olá mundo! \033[m')
#para a letra preta usa o código 7 para inverter.
print('\033[40m Olá mundo!\033[m')
print('\033[7;40m Olá mundo!\033[m')

print('Testando cores: \033[33m Amarelo, \033[31m Vermelho \033[m')
#para tirar a virgula em amarela
print('Testando cores: \033[33m Amarelo\033[m, \033[31m Vermelho \033[m')

#dentro das {} do format pode colocar cor também: abre a cor, o que vem no format, encerra a cor
#pode usar lista de cores se achar mais fácil, fazer como se fosse um input
'''aos 20 minutos
https://www.youtube.com/watch?v=0hBIhkcA8O8&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=47
'''
