import time
import os

#aguarda a entrada do dado
def Wait():
    k = input("Pressione uma enter para continuar")

#desenha os andares
def Floors(maxFloor, actualFloor, minFloor):
    for i in range(maxFloor, minFloor-1, -1):
        if i == actualFloor:
            print("(|)", actualFloor)
        else:
            print(" | ", i)

#function subir
def FromToUp(actualFloor,floorNumber,minFloor):
    for actualFloor in range(actualFloor, floorNumber+1):
        os.system('cls')
        Floors(maxFloor, actualFloor, minFloor)
        time.sleep(1)
    return actualFloor

#function descer
def FromToDown(actualFloor, floorNumber,minFloor):
    for actualFloor in range( actualFloor, floorNumber-1, -1):
        os.system('cls')
        Floors(maxFloor, actualFloor, minFloor)
        time.sleep(1)
    return actualFloor

## Loop
while True:
    os.system('cls')
    maxFloor = int(input("Quantos andares tem o prédio ?"))
    actualFloor = 0
    minFloor = 0
    end = False
    existsSub = input("Existe subsolo? (S ou N) ").lower().strip()

    if(existsSub == "s" or existsSub == "S"):
        minFloor = int(input("Quantos subsolos tem o prédio ? (ex -2)" ))
        
    while end == False:
        
        #chamada dos desenhos dos andares
        Floors(maxFloor, actualFloor, minFloor)

        ##floorNumber = minFloor-1
        #while (floorNumber < minFloor or floorNumber > maxFloor)

        floorNumber = int(input("digite qual andar quer visitar: "))

        ## Check posição
        
        #destino  é igual o local onde estamos
        if( actualFloor == floorNumber ):
            print("Já estamos nesse andar!")

        #destino é maior que andar atual
        if (floorNumber > actualFloor):
            print( "Vamos subir")
            actualFloor = FromToUp(actualFloor, floorNumber, minFloor)
                      
        #destino é menor que andar atual
        elif floorNumber < actualFloor :
            print("Vamos descer")

            print("fdgdgrd", actualFloor, floorNumber, minFloor)
            actualFloor = FromToDown(actualFloor, floorNumber, minFloor)
                               
        print('Voce chegou ao seu destino!')
        Wait()

        # Check
        x = input("Deseja ir para outro andar ? <sim/nao> ").lower().strip()
        if x == "sim":
            continue
        elif x == "nao":
            end = True


















