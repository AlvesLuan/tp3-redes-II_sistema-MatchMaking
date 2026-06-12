from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

'''Recebo todas as informações, junto na string allData e mando pro server, pra lá ele mesmo fazer a separação do que cada coisa é em sua categoria respectiva.'''
playerName     =   input   ('digite seu Nickname: ')
game           =   input   ('informe o jogo desejado: ')
playerLevel    =   input   ('informe seu level: ')

allData = (f"{playerName};{game};{playerLevel}")

clientSocket.sendto(allData.encode(),(serverName, serverPort))
allData, serverAddress = clientSocket.recvfrom(2048)

print(allData.decode())

clientSocket.close()
