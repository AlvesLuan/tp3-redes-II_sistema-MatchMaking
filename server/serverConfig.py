from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

#jogos disponiveis
fifa = []
valorant = []
cs = []

jogosDisponiveis = ["fifa", "valorant", "cs"]

print ('O servidor matchmaking está pronto.')


while 1:
	allData, clientAddress = serverSocket.recvfrom(2048)
	allData = allData.decode()
	playerName, game, playerLevel = allData.split(";")

	print("id do player: ", playerName)
	modifiedId = playerName.lower()
	print("jogo escolhido: ", game)
	modifiedGame = game.lower()
	print("level do jogador:", playerLevel)


	if modifiedGame not in jogosDisponiveis:
		messageToClient = ("Jogo indisponivel")

	# registros
	else:
		if modifiedGame == 'fifa':
			fifa.append(modifiedId)

			if len(fifa) >= 2:
				messageToClient = (f"partida iniciada!\n {fifa[0]} vs {fifa[1]}")
			else:
				messageToClient = "Aguardando mais jogadores..."



		elif modifiedGame == 'cs':
			cs.append(modifiedId)
			
			if len(cs) >= 4:
				messageToClient = (f"o jogo será: {cs[0]}, {cs[1]}\n vs \n{cs[2]}, {cs[3]}")
			else:
				messageToClient = "Aguardando mais jogadores..."



		elif modifiedGame == 'valorant':
			valorant.append(modifiedId)
			
			if len(valorant) >= 4:
				messageToClient = (f"o jogo será: {valorant[0]}, {valorant[1]}\n vs \n{valorant[2]}, {valorant[3]}")
			else:
				messageToClient = "Aguardando mais jogadores..."

		

	serverSocket.sendto(messageToClient.encode(), clientAddress)
