import random
from global_vars import mapaBot, mapaPlayer, barcosSiglas, barcosNomes, printMap, clear

listaTemp = []  # Utilizado para o checker()

# Verifica disponibilidade do espaço para posicionar um barco
def checker():
    for posicao in listaTemp:
        if posicao != "  ":  # Se não estiver vázio, não pode
            return False


# Posicionamento do BOT
def posicionarBarcosBot():
    # Loop para cada tamanho de barco
    for tamanho in range(5, 0, -1):
        while True:

            # Vertical (0) / Horizontal (1)
            sentido = random.randint(0, 1)

            if sentido == 0:  # Se VERTICAL
                if tamanho == 5:
                    anchorY = 0

                else:
                    anchorY = random.randint(0, 4 - tamanho)  # Posição Y aleatória

                anchorX = random.randint(0, 9)  # Posicão X aleatória

                for tamanhoAdic in range(0, tamanho):
                    listaTemp.append(
                        mapaBot[anchorY + tamanhoAdic][anchorX]
                    )  # Envia coordenadas para a lista temporária

                if checker() != False:  # Envia dados da lista temporária pro checker
                    for tamanhoAdic in range(0, tamanho):
                        mapaBot[anchorY + tamanhoAdic][anchorX] = barcosSiglas[
                            tamanho - 1
                        ]
                    break

            elif sentido == 1:  # Se HORIZONTAL

                anchorY = random.randint(0, 4)  # Posição Y aleatória
                anchorX = random.randint(0, 9 - tamanho)  # Posicão X aleatória

                for tamanhoAdic in range(0, tamanho):
                    listaTemp.append(
                        mapaBot[anchorY][anchorX + tamanhoAdic]
                    )  # Envia coordenadas para a lista temporária

                if checker() != False:  # Envia dados da lista temporária pro checker
                    for tamanhoAdic in range(0, tamanho):
                        mapaBot[anchorY][anchorX + tamanhoAdic] = barcosSiglas[
                            tamanho - 1
                        ]
                    break

            listaTemp.clear()  # Limpa a lista temporária


# Posicionamento do PLAYER
def posicionarBarcosPlayer():

    # Loop para cada tamanho de barco
    for tamanho in range(5, 0, -1):

        while True:

            clear()  # Limpa o console

            # Instruções para o player
            print(
                f"""
INSTRUÇÕES PARA POSICIONAMENTO:
- Digite o valor, e somente o valor solicitado.
- A coordenada será solicitada a partir de um valor da linha e coluna no mapa.
- O barco sera posicionado SEMPRE para a direita (se na HORIZONTAL), ou para baixo (se na VERTICAL)
- Não é possível posicionar um barco por cima do outro. Será solicitado uma nova coordenada.
- O mapa tem tamanho 5x10.

SEU MAPA:
            """
            )

            # Mostra o mapa do Player
            printMap(mapaPlayer)

            # Informações do barco atual
            print(f"Posicionando o barco: {barcosNomes[tamanho - 1]}")

            # Vertical (0) / Horizontal (1)
            sentido = "whatever"  # Apenas para a lógica do while
            while sentido != 0 and sentido != 1:
                sentido = int(input("\nDigite 0 para VERTICAL | 1 para HORIZONTAL: "))
                print(sentido)

            if sentido == 0:  # Se VERTICAL

                if tamanho == 5:
                    anchorY = 0
                    anchorX = int(input(f"Digite a coluna de 0 a 9: "))  # Posicão X

                else:
                    anchorY = int(
                        input(f"Digite a linha de 0 a {5 - tamanho}: ")
                    )  # Posição Y
                    anchorX = int(input(f"Digite a coluna de 0 a 9: "))  # Posicão X

                for tamanhoAdic in range(0, tamanho):
                    listaTemp.append(
                        mapaPlayer[anchorY + tamanhoAdic][anchorX]
                    )  # Envia coordenadas para a lista temporária

                if checker() != False:  # Se estiver disponível, adiciona no mapa
                    for tamanhoAdic in range(0, tamanho):
                        mapaPlayer[anchorY + tamanhoAdic][anchorX] = barcosSiglas[
                            tamanho - 1
                        ]
                    break

            elif sentido == 1:  # Se HORIZONTAL

                anchorY = int(input(f"Digite a linha de 0 a 4: "))  # Posição Y
                anchorX = int(
                    input(f"Digite a coluna de 0 a {10 - tamanho}: ")
                )  # Posicão X

                for tamanhoAdic in range(0, tamanho):
                    listaTemp.append(
                        mapaPlayer[anchorY][anchorX + tamanhoAdic]
                    )  # Envia coordenadas para a lista temporária

                if checker() != False:  # Se estiver disponível, adiciona no mapa
                    for tamanhoAdic in range(0, tamanho):
                        mapaPlayer[anchorY][anchorX + tamanhoAdic] = barcosSiglas[
                            tamanho - 1
                        ]
                    break

            listaTemp.clear()  # Limpa a lista temporária


# Lógica de start
def run():
    posicionarBarcosBot()  # Posicionamento BOT
    posicionarBarcosPlayer()  # Posicionamento PLAYER

    printMap(mapaBot)  # Mapa BOT
    printMap(mapaPlayer)  # Mapa PLAYER
