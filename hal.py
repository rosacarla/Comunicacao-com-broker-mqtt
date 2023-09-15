# Codigo: cria camada de abstração de hardware (HAL)
# Reescrever codigo para embarcar em dispositivos diferentes
# Autora: Carla Edila Silveira
# Data: 15/09/2023

# Define 3 metodos para a camada de abstracao de hardware
import random # escolha aleatoria de valores do metodos

def temperatura():
    return random.randrange(2, 32)

def umidade():
    return random.randrange(10, 95)

def aquecedor(estado: str):
    if estado == 'on':
        print("Aquecedor LIGADO")
    else:
        print("Aquecedor DESLIGADO")