import random
from time import sleep

import global_vars as var

tamanho= 5

# Variaveis caso o barco não tenha caido, caso seja destruido, a variavel se torna falsa
PativoPA = True
PativoNT = True
PativoCT = True
PativoSU = True
PativoDE = True

BativoPA = True
BativoNT = True
BativoCT = True
BativoSU = True
BativoDE = True

# Define quem ganhará
playerGanha = False
botGanha = False


# Verifica quais barcos ainda estão de pé
def checkBarcoPlayer(x, y):
    found = False
    for linha in range(0,5):
        if found == True:
            break
        for coluna in range(0,10):
            if x in var.mapaPlayer[linha][coluna] and y:
                y = True
                found = True
                break
    if found == False:
        y = False
        print(f"""
-~-~-~-~-~-~-~-~-~-~-~-
# Barco abatido: {x}. #
-~-~-~-~-~-~-~-~-~-~-~-
""")
        sleep(2)
    return y

def checkBarcoBot(x, y):
    found = False
    for linha in range(0,5):
        if found == True:
            break
        for coluna in range(0,10):
            if x in var.mapaBot[linha][coluna] and y:
                y = True
                found = True
                break
    if found == False:
        y = False
        print(f"""
-~-~-~-~-~-~-~-~-~-~-~-
# Barco abatido: {x}. #
-~-~-~-~-~-~-~-~-~-~-~-
""")
        sleep(2)
    return y


#jogadas
for i in range(0,101):
    print("Mapa do BOT")
    var.printMap(var.mapaBotDisplay)
    
    print("Seu mapa")
    var.printMap(var.mapaPlayer)
    
#jogada player
    if i % 2 == 0:
        while True:
            jogadaY = int(input("\nDigite a LINHA que você quer atacar (0 a 4): "))
            if jogadaY >= 0 and jogadaY <= 4:
                break
        while True:
            jogadaX = int(input("Digite a COLUNA que você quer atacar (0 a 9): "))
            if jogadaX >= 0 and jogadaX <= 9:
                break


        if var.mapaBot[jogadaY][jogadaX] == "O " or var.mapaBot[jogadaY][jogadaX] == "X ":
            while True:
                while True:
                    jogadaY = int(input("\nDigite a LINHA que você quer atacar (0 a 4): "))
                    if jogadaY >= 0 and jogadaY <= 4:
                        break
                while True:
                    jogadaX = int(input("Digite a COLUNA que você quer atacar (0 a 9): "))
                    if jogadaX >= 0 and jogadaX <= 9:
                        break

                if var.mapaBot[jogadaY][jogadaX] != "O " and var.mapaBot[jogadaY][jogadaX] != "X ":
                    break

        if var.mapaBot[jogadaY][jogadaX] != "  ":
            var.mapaBotDisplay[jogadaY][jogadaX] = "X "
            var.mapaBot[jogadaY][jogadaX] = "X "
            print("""
-~-~-~-~-~-~-~-~-~-~-~-~-~
# Você acertou um barco! #
-~-~-~-~-~-~-~-~-~-~-~-~-~""")
            sleep(2)
            var.clear()
        else:
            print("""
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
# Você NÃO acertou um barco! #
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~""")
            sleep(2)
            var.clear()
            var.mapaBotDisplay[jogadaY][jogadaX] = 'O '

        if BativoPA:
            BativoPA = checkBarcoBot(var.portaAvioes, BativoPA)
        if BativoNT:
            BativoNT = checkBarcoBot(var.navioTanque, BativoNT)
        if BativoCT:
            BativoCT = checkBarcoBot(var.contraTorpedeiro, BativoCT)
        if BativoSU:
            BativoSU = checkBarcoBot(var.submarino, BativoSU)
        if BativoDE:
            BativoDE = checkBarcoBot(var.destroier, BativoDE)
        if not BativoPA and not BativoNT and not BativoCT and not BativoSU and not BativoDE:
            playerGanha = True
            break
        
#jogada bot
    else:
        jogadaY = random.randint(0,4)
        jogadaX = random.randint(0,9)

        if var.mapaPlayer[jogadaY][jogadaX] == "O " or var.mapaPlayer[jogadaY][jogadaX] == "X ":
            while True:
                jogadaY = random.randint(0,4)
                jogadaX = random.randint(0,9)

                if var.mapaPlayer[jogadaY][jogadaX] != "O " and var.mapaPlayer[jogadaY][jogadaX] != "X ":
                    break

        if var.mapaPlayer[jogadaY][jogadaX] != "  ":
            var.mapaPlayer[jogadaY][jogadaX] = 'X '
            print("""
-~-~-~-~-~-~-~-~-~-~-~-~
# Acertaram seu barco! #
-~-~-~-~-~-~-~-~-~-~-~-~""")
            sleep(2)
            var.clear()
        else:
            print("""
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
# Não acertaram o seu barco. #
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~""")
            sleep(2)
            var.clear()
            var.mapaPlayer[jogadaY][jogadaX] = 'O '
        
        if PativoPA:
            PativoPA = checkBarcoPlayer(var.portaAvioes, PativoPA)
        if PativoNT:
            PativoNT = checkBarcoPlayer(var.navioTanque, PativoNT)
        if PativoCT:
            PativoCT = checkBarcoPlayer(var.contraTorpedeiro, PativoCT)
        if PativoSU:
            PativoSU = checkBarcoPlayer(var.submarino, PativoSU)
        if PativoDE:
            PativoDE = checkBarcoPlayer(var.destroier, PativoDE)

        if not PativoPA and not PativoNT and not PativoCT and not PativoSU and not PativoDE:
            botGanha = True
            break


if botGanha:
    print('O computador ganhou!!!')

elif playerGanha:
    print('Você ganhou!!!')