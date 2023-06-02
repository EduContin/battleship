import os

# Mapas PLAYER e BOT
mapaPlayer = [
  ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
  ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
  ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
  ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
  ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
]

mapaBot = [
  ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
  ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
  ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
  ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
  ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
]

# Siglas dos barcos
destroier = "DE"
submarino = "SU"
contraTorpedeiro = "CT"
navioTanque = "NT"
portaAvioes = "PA"

# Listagem dos tipos de barcos
barcosSiglas = [destroier, submarino, contraTorpedeiro, navioTanque, portaAvioes]
barcosNomes = ['Destroier','Submarino','Contra Torpedeiro', 'Navio Tanque', 'Porta Aviões']

# Clear console
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Função de printar os mapas formatado
def printMap(mapa):
    numDaLinha = 0

    print("| X  | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |")
    print("--------------------------------------------------------")
    for linha in mapa:
      print(f"| {numDaLinha}  | "  + " | ".join(linha) + " |")
      print("--------------------------------------------------------")
      numDaLinha += 1
  