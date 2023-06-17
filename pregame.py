import random

from global_vars import mapaBot, mapaPlayer, barcosSiglas, barcosNomes, printMap, clear

listaTemp = []


def checker():
    for posicao in listaTemp:
        if posicao != "  ":
            return False

def posicionarBarcosBot():
    # Loop para cada tamanho de barco
    for tamanho in range(5, 0, -1):
        while True:

            # Vertical (0) / Horizontal (1)
            sentido = random.randint(0, 1)

            if sentido == 0: # Se VERTICAL
                if tamanho == 5:
                    anchorY = 0
                
                else:
                    anchorY = random.randint(0, 4 - tamanho) # Posição Y aleatória
                    
                anchorX = random.randint(0, 9) # Posicão X aleatória

                for tamanhoAdic in range(0, tamanho):
                    listaTemp.append(mapaBot[anchorY + tamanhoAdic][anchorX])

                if checker() != False:
                    for tamanhoAdic in range(0, tamanho):
                        mapaBot[anchorY + tamanhoAdic][anchorX] = barcosSiglas[tamanho - 1]
                    break

            elif sentido == 1: # Se HORIZONTAL

                anchorY = random.randint(0, 4) # Posição Y aleatória
                anchorX = random.randint(0, 9 - tamanho) # Posicão X aleatória

                for tamanhoAdic in range(0, tamanho):
                    listaTemp.append(mapaBot[anchorY][anchorX + tamanhoAdic])

                if checker() != False:
                    for tamanhoAdic in range(0, tamanho):
                        mapaBot[anchorY][anchorX + tamanhoAdic] = barcosSiglas[tamanho - 1]
                    break
        
            listaTemp.clear() # Limpa a lista temporária

def posicionarBarcosPlayer():
    errorExistent = False
    # Loop para cada tamanho de barco

    for tamanho in range(5, 0, -1):
        while True:
            clear() # Limpa o console

            if errorExistent == True:
                print("""
#################################
#   POSIÇÃO DO BARCO OCUPADA    #
#################################
                """)

            errorExistent = False

            # Instruções para o player
            print(f"""
INSTRUÇÕES PARA POSICIONAMENTO:
- Digite o valor, e somente o valor solicitado.
- A coordenada será solicitada a partir de um valor da linha e coluna no mapa.
- O barco sera posicionado SEMPRE para a direita (se na HORIZONTAL), ou para baixo (se na VERTICAL)
- O mapa tem tamanho 5x10.

SEU MAPA:
            """)
            # Mostra o mapa do Player
            printMap(mapaPlayer)

            # Informações do barco atual
            print(f"Posicionando o barco: {barcosNomes[tamanho - 1]}")

            # Vertical (0) / Horizontal (1)
            sentido = "whatever" # Apenas para a lógica do while
            while sentido != 0 and sentido != 1:
                sentido = int(input("\nDigite 0 para VERTICAL | 1 para HORIZONTAL: "))

            if sentido == 0: # Se VERTICAL

                if tamanho == 5:
                    anchorY = 0

                    while True:
                        anchorX = int(input(f"Digite a coluna de 0 a 9: ")) # Posicão X

                        if anchorX >= 0 and anchorX <= 9:
                            break
                        else:
                            print("Posição inválida.")

                else:
                    while True:
                        anchorY = int(input(f"Digite a linha de 0 a {5 - tamanho}: ")) # Posição Y

                        if anchorY >= 0 and anchorY <= (5 - tamanho):
                            break
                        else:
                            print("Posição inválida.")

                    while True:
                        anchorX = int(input(f"Digite a coluna de 0 a 9: ")) # Posicão X

                        if anchorX >= 0 and anchorX <= 9:
                            break
                        else:
                            print("Posição inválida.")
                
                for tamanhoAdic in range(0, tamanho):
                    listaTemp.append(mapaPlayer[anchorY + tamanhoAdic][anchorX])

                if checker() != False:
                    for tamanhoAdic in range(0, tamanho):
                        mapaPlayer[anchorY + tamanhoAdic][anchorX] = barcosSiglas[tamanho - 1]
                    break

            elif sentido == 1: # Se HORIZONTAL

                while True:
                        anchorY = int(input(f"Digite a linha de 0 a 4: ")) # Posição Y

                        if anchorY >= 0 and anchorY <= 4:
                            break
                        else:
                            print("Posição inválida.")

                while True:
                    anchorX = int(input(f"Digite a coluna de 0 a {10 - tamanho}: ")) # Posicão X

                    if anchorX >= 0 and anchorX <= (10 - tamanho):
                        break
                    else:
                            print("Posição inválida.")

                for tamanhoAdic in range(0, tamanho):
                    listaTemp.append(mapaPlayer[anchorY][anchorX + tamanhoAdic])

                if checker() != False:
                    for tamanhoAdic in range(0, tamanho):
                        mapaPlayer[anchorY][anchorX + tamanhoAdic] = barcosSiglas[tamanho - 1]
                    break
        
            listaTemp.clear() # Limpa a lista temporária

posicionarBarcosBot()
posicionarBarcosPlayer()