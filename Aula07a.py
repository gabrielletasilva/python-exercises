"""
nome = str(input('Qual é seu nome?'))
print('Prazer em te conhecer{:^20}!'.format(nome))

name = input('Whats your name?')
print(f'Nice to meet you, {name:=^20}!')

print('A soma é {}, a multiplicação é {} e a divisão é {:.3f}'.format(s, m, d))

print('A soma é {}, a multiplicação é {} e a divisão é {}'.format(s, m, d), end=' ')

"""


n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a multiplicação é {} e a divisão é {}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))

