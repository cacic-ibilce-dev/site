from glob import glob
from operator import itemgetter

#Definindo as constantes

#Diretorios:
MEMBROS = 'conteudo/membros/*.tsv'



# retorna listas no senguinte formato:
# [ [ Ano1, [[nome, apelido,função, mensagem, foto ], [nome, ...]] 
#   [ Ano2, [[nome, apelido,função, mensagem, foto ], [nome, ...]]
#	...
# ]
#
# Cada ano é separado em um arquivo tsv(tabela separada por tabs)
# em que as  colunas são:
#	0) timestamp
#	1) email
#	2) nome
# 	3) apelido
#	4) foto
#	5) função
#	6) mensagem
# Esse arquivo .tsv é feito a partir das resposta do formulário do drive
# que foi passada para as pessoas do CA
#
# Como os anos já são ordenados a lista final saíra ordenada
def Chapas():
	#Le os arquivos .tsv dentro da pasta membros e retorna uma lista do diretorio
	# desses arquivos
	arquivos = glob(MEMBROS)
	
	# Lista que conterá todas as chapas
	Chapas = []

	# Cada Arquivo é uma chapa
	for diretorio in arquivos:
		#Abre o arquivo
		arq = open(diretorio,'r')
		
		# Temos que achar o ano da chapa
		# O ano é o nome do arquivo
		#Então parseamos o diretorio
		# 'conteudo/membros/2018.tsv' =split=> [conteudo,membros,2018.tsv]
		ano = diretorio.split('/')
		# e pegamos o ultimo elemento da lista
		# [conteudo,membros,2018.tsv] => [2018.tsv]
		ano = ano[-1]
		
		# '2018.tsv' = tira os ultimos 4 caracteres -> '2018'
		ano = ano[:-4]
		print(ano)
		# Armazenaremaos a chapa em uma lista
		novaChapa = []
		# inicializamos pelo ano da chapa
		novaChapa.append(ano)

		# Criamos uma lista de membros novo, em que cada membro
		# é uma lista com o [nome, apelido,função, mensagem, foto ]
		novosMembros = []
		novoMembro=[]

		# vamos ler os novo membros do arquivo
		# Cada Arquivo é uma chapa
		# Cada linha do arquivo é um membro

		presidente = []
		vice = []
		for linha in arq:
			novoMembro=[] #reseta o membro

			# Os campos do membro são separados por tabulações '\t' que nem especificado
			# no começo da função
			# timestamp\temail...\tmensagemsplit('\t') -> [timestamp,email,...,mensagem]
			linha = linha.split('\t')
			novoMembro.append(linha[2]) #Nome
			novoMembro.append(linha[3]) #Apelido
			novoMembro.append(linha[5]) #Função
			novoMembro.append(linha[6]) #Mensagem
			novoMembro.append(linha[4]) #Foto

			#Separamos o vice e o presidente para colocar-los no começo da lista
			if ("Vice Presidente" in linha[5]):
				vice = novoMembro
			elif ("Presidente" in linha[5]):
				presidente = novoMembro
			else:
				novosMembros.append(novoMembro)

		#deleta a primeira fileira, pois é apenas o cabeçalho do arquivo
		# (tem o nome das perguntas do google forms)
		novosMembros = novosMembros[1:]
		
		#Ordena os membros por nome (itemgetter é usado para ordernar uma lista de lista)
		novosMembros.sort(key=itemgetter(0))

		#Adiciona o vice e o presidente no começo da lista
		novosMembros.insert(0,vice)
		novosMembros.insert(0,presidente)
		
		#Adiciona os novosMembros a nova chapa
		novaChapa.append(novosMembros)

		# adiciona a nova chapa na nossa lista final
		Chapas.append(novaChapa)



	return Chapas