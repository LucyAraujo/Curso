import time
import os

#aguarda a entrada do dado
def Wait():
    k = input("Pressione uma enter para continuar")

#maxFloor -> maior 
#actualFloor -> andar atual
#minFloor -> menor andar
#floorNumber -> numero do andar a visitar

#desenha os andares
def Floors(maxFloor, actualFloor, minFloor):
    for i in range(maxFloor, minFloor-1, -1):
        if i == actualFloor:
            print("(|)", actualFloor)
        else:
            print(" | ", i)

def FromToUp(actualFloor,floorNumber,minFloor):
    
    print("atual", actualFloor," | irei visitar ", floorNumber," | minFloor ", minFloor )
    Floors(maxFloor, floorNumber, minFloor)
    return floorNumber

## Loop
while True:
    os.system('cls')
    maxFloor = int(input("Quantos andares tem o prédio ?"))

    actualFloor = 0
    minFloor = 0
    end = False

    while end == False:
        
        #chamada dos desenhos dos andares
        Floors(maxFloor, actualFloor, minFloor)

        #floorNumber = minFloor-1
        #while (floorNumber < minFloor or floorNumber > maxFloor)

        floorNumber = int(input("digite qual andar quer visitar: "))

        # Check posição
        #destino  é igual o local onde estamos
        if( actualFloor == floorNumber ):
            print("Já estamos nesse andar")

        #destino é maior que andar atual
        if (floorNumber > actualFloor):
            print( "Vamos subir")
            actualFloor = FromToUp(actualFloor, floorNumber, minFloor)

        elif (floorNumber < actualFloor):
            print("Vamos descer")
            actualFloor = FromToDown(actualFloor, floorNumber, minFloor)

        print('Voce chegou ao seu destino!')
        Wait()

        # Check
        x = input("Deseja ir para outro andar ? <sim/nao> ").lower().strip()
        if x == "sim":
            continue
        elif x == "nao":
            end = True


















