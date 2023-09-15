# Codigo: configura credenciais para conexao com broker MQTT
# Autora: Carla Edila Silveira
# Data: 15/09/2023

# Declara dados para conexao
user = '' # não preencher user e password porque HiveMQ nao precisa
password = '' # deve preencher para outros tipos de broker
client_id = 'abcdefghijk12345678' # para hive pode ser string sem espaços como id do dispositivo
server = 'mqtt-dashboard.com' # usar servidor que aparece na tela do HiveMQ
port = 1883 # usar porta padrao do mqtt (1883), dispensar porta que esta do navegador