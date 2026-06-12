from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

playerName     =   input   ('digite seu id: ')
game            =   input   ('informe o jogo desejado: ')
playerLevel    =   input   ('informe seu level: ')
allData = [playerName,game,playerLevel]

clientSocket.sendto(allData.encode(),(serverName, serverPort))
allData, serverAddress = clientSocket.recvfrom(2048)

print(allData)
clientSocket.close()
