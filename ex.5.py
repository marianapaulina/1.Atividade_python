#5. Faça um programa que receba um valor, e traga informações sobre esse valor, dizendo se é alfanumérico, numérico e etc.

a = input('Digite algo para que o item seja verificado:')
print('O tipo primitivo desse dado é:', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É uma letra?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('É uma letra maiúscula?', a.isupper())
print('É uma letra minúscula?', a.islower())
print('É um título?',a.istitle())
