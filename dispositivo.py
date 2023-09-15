# Codigo: comunicacao com broker MQTT
# Autora: Carla Edila Silveira
# Data: 15/09/2023

import paho.mqtt.client as mqtt # paho eh biblioteca principal para trabalhar com mqtt
import time # biblioteca de temporalizacao

# Configuracoes de credenciais para conexao com broker MQTT
user = '' # não preencher user e password porque HiveMQ nao precisa
password = '' # deve preencher para outros tipos de broker
client_id = 'abcdefghijk12345678' # para hive pode ser string sem espaços como identificador do dispositivo
server = 'mqtt-dashboard.com' # usar servidor que aparece na tela do HiveMQ
port = 1883 # usar porta padrao do mqtt (1883), dispensar porta que há na interface do navegador

# Faz a conexao
client = mqtt.Client(client_id) # objeto recebe a id do cliente
client.username_pw_set(user, password) # objeto recebe usuario e senha
client.connect(server, port) # objeto recebe servidor e porta

# Faz um publish
client.publish('pucpr/iotmc/carla/temperatura', '24.1') # argumentos sao topico e mensagem
# evitar envio de informacoes compostas na mensagem, a menos que tenha necessidade
time.sleep(1) # pausa para enviar a mensagem
# apos conectar o HIveMQ, criar topico 'pucpr/iotmc/carla/#' para monitoramento de mensagens via codigo

# Desconecta do broker
client.disconnect(0)