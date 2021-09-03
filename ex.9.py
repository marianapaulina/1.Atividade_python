#9. Faça um programa que leia um valor em metros, mostre o valor convertido em centímetros, e milímetros.

num = float(input('Digite a medida em metros:'))
cm = num * 100
milimetros = num * 1000
print('{} metros convertido para centímetros é igual a {:.0f}cm, e convertido para milímetros é {:.0f}mm.'.format(num, cm, milimetros))
