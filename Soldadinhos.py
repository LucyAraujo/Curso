# soldados recebidos
# montar fileiras
# a quantiDADE DE soldados por fila é igual ao numero da fila
#ex 1 -1
#2 - 1-2
#3 -1 - 2 - 3
#total 6 soldados
#listar a partir do num recebido qtd total de filas  qtd de soldados na ultima

qtdSoldados = int(input("Digite o número de soldadinhos: "))

##1
##12 
##123
##1234
##12345
##123456
##123
## =  24 soldados 

if qtdSoldados <= 0:
    print("a quantidade de soldados deve ser maior q 0");


#montar fileiras dividindo os soldadinhos
#cada fila contem o valor da fila anterior +1 
#ter o total de soldadosnos alocados nas filas

qtdFileiras = 0
totalSoldadosNaFila = 0


while qtdSoldados > 0 :

    totalSoldadosNaFila += 1
    qtdSoldados -= totalSoldadosNaFila
    qtdFileiras += 1 

print("Numero de fileiras formadas foi" ,  qtdFileiras)
if qtdSoldados < 0:
    print("restaram" , qtdSoldados + totalSoldadosNaFila, "soldados na ultima fila")





















