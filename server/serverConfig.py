from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

'''Crio a fila de espera para cada jogo, 
onde os jogadores serão adicionados até que o número mínimo de jogadores 
seja atingido para criar uma partida.'''
fifa = []
valorant = []
cs = []
minecraft = []
leagueofLegends = []

'''aqui crio o array com os jogos disponíveis(e seus outros apelidos), para verificar se o jogo escolhido pelo jogador é válido ou não.'''
jogosDisponiveis = ["fifa", "valorant", "vava", "cs", "counter strike", "counter-strike", "minecraft", "league of legends", "lol"]

'''variavel de controle do id das partidas, para que cada partida criada tenha um id único.'''
partidaId = 100

print ('O servidor matchmaking está pronto.')

'''Aqui trato erros, como id vazio, jogo indisponível e level inválido. '''
while 1:
	allData, clientAddress = serverSocket.recvfrom(2048)
	allData = allData.decode()
	playerName, game, playerLevel = allData.split(";") #separo os dados do cliente nas variaveis correspondentes
	#deixo em minusculo para padronizar
	modifiedId = playerName.lower()
	modifiedGame = game.lower()

	#tento transformar a string de nivel em INT, se n der, acusa o erro.
	try:
		playerLevel = int(playerLevel)
	except ValueError:
		messageToClient = ("Erro: o level deve ser numérico.")
		serverSocket.sendto(messageToClient.encode(), clientAddress)
		continue

	#erro se o id estiver vazio.
	if playerName.strip() == "":
		messageToClient = ("Erro: informe um Nickname válido.")
		serverSocket.sendto(messageToClient.encode(), clientAddress)
		continue

	#erro se o jogo nao estiver na lista
	elif modifiedGame not in jogosDisponiveis:
		messageToClient = ("Erro: jogo indisponível.")
		serverSocket.sendto(messageToClient.encode(), clientAddress)
		continue

	#erro se o level for menor que 1 ou maior que 100.
	elif playerLevel < 1 or playerLevel > 100:
		messageToClient = ("Erro: level inválido. Informe um valor entre 1 e 100.")
		serverSocket.sendto(messageToClient.encode(), clientAddress)
		continue

	


	'''se o jogo escolhido for válido, o jogador é adicionado a fila de espera do jogo correspondente. 
	quando o número mínimo de jogadores for atingido, uma nova partida é criada, o id da partida é incrementado e os jogadores são removidos da fila de espera.'''
	
#======================================== FIFA ==============================================================#
	if modifiedGame == "fifa":
		fifa.append(modifiedId)

		if len(fifa) >= 2:
			messageToClient = (	f"Uma nova partida foi criada.\n"
								f"Jogo: FIFA \n"
								f"ID da partida: {partidaId} \n"
								f"2 jogadores  foram selecionados")
			partidaId += 1
			fifa.pop(0)
			fifa.pop(0)
		else:
			messageToClient = ("Voce foi adicionado a fila de espera do fifa.\nAguardando mais jogadores...")


#======================================== MINECRAFT ==============================================================#
	elif modifiedGame == "minecraft":
		minecraft.append(modifiedId)

		if len(minecraft) >= 2:
			messageToClient = (	f"Uma nova partida foi criada.\n"
								f"Jogo: Minecraft \n"
								f"ID da partida: {partidaId} \n"
								f"2 jogadores  foram selecionados")
			partidaId += 1
			minecraft.pop(0)
			minecraft.pop(0)
		else:
			messageToClient = ("Voce foi adicionado a fila de espera do minecraft.\nAguardando mais jogadores...")


#======================================== Counter Strike ==============================================================#
	elif modifiedGame == "cs" or modifiedGame == "counter strike" or modifiedGame == "counter-strike":
		cs.append(modifiedId)
		
		if len(cs) >= 4:
			messageToClient = (	f"Uma nova partida foi criada.\n"
								f"Jogo: Counter-Strike \n"
								f"ID da partida: {partidaId} \n"
								f"4 jogadores  foram selecionados.")
			partidaId += 1
			cs.pop(0)
			cs.pop(0)
			cs.pop(0)
			cs.pop(0)
		else:
			messageToClient = ("Voce foi adicionado a fila de espera do CS.\nAguardando mais jogadores...")


#======================================== Valorant ==============================================================#
	elif modifiedGame == "valorant" or modifiedGame == "vava":
		valorant.append(modifiedId)
		
		if len(valorant) >= 4:
			messageToClient = (f"Uma nova partida foi criada.\n"
								f"Jogo: Valorant \n"
								f"ID da partida: {partidaId} \n"
								f"4 jogadores  foram selecionados.")
			partidaId += 1
			valorant.pop(0)
			valorant.pop(0)
			valorant.pop(0)
			valorant.pop(0)
		else:
			messageToClient = ("Voce foi adicionado a fila de espera do Valorant.\nAguardando mais jogadores...")


#======================================== League of Legends ==============================================================#
	elif modifiedGame == "lol" or modifiedGame == "league of legends":
		leagueofLegends.append(modifiedId)

		if len(leagueofLegends) >= 5:
			messageToClient = (f"Uma nova partida foi criada.\n"
								f"Jogo: League of Legends \n"
								f"ID da partida: {partidaId} \n"
								f"5 jogadores  foram selecionados.")
			partidaId += 1
			leagueofLegends.pop(0)
			leagueofLegends.pop(0)
			leagueofLegends.pop(0)
			leagueofLegends.pop(0)
			leagueofLegends.pop(0)
		else:
			messageToClient = ("Voce foi adicionado a fila de espera do League of Legends.\nAguardando mais jogadores...")
								


		print("id do player: ", playerName)
		print("jogo escolhido: ", game)
		print("level do jogador:", playerLevel, "\n")

		serverSocket.sendto(messageToClient.encode(), clientAddress)
