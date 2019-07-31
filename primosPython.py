#calculo de primos
# resto da divisão por ele mesmo ser =  0 é primo

#tstar recebendo o numero

numero = int(input("Digite o  número para testar se é primo: "))

#count da quantidade de divisores ele tem

qtdDividores = 0

for i in range(1, numero +1 , 1):
    if numero % i == 0:
        qtdDividores = qtdDividores + 1

if(qtdDividores == 2):
    print()
    print( numero , " é um número primo")
else:
    print()
    print( numero , " Não é um número primo")

    
