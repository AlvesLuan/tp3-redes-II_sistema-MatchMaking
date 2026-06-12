from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

#jogos disponiveis
fifa = []
valorant = []
cs = []

jogosDisponiveis = [fifa, valorant, cs]

print ('O servidor matchmaking está pronto.')


while 1:
	allData, clientAddress = serverSocket.recvfrom(2048)
	print("id do player: ", allData[playerName])
	modifiedName = allData[playerName].lower()
	print("jogo escolhido: ", allData[game])
	modifiedGame = allData[game].lower()
	print("level do jogador: ", allData[playerLevel])


	if modifiedGame not in jogosDisponiveis:
		print ("Jogo Indisponivel")

	else:
		#registro
		jogosDisponiveis[]


	print("mensagem que sera enviada: ", modifiedEscolha)
	serverSocket.sendto(modifiedEscolha, clientAddress)
