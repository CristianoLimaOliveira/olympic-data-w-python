import matplotlib.pyplot as plt
import numpy as np
import csv

def graficoL2(dicionarioAthlete,dicionarioComiteOlimpico):
	paisEscolhido=1
	paises=[]
	while(paisEscolhido!=0):
		print("Escolha abaixo um país:")
		contador=0
		for chave, valor in dicionarioComiteOlimpico.items():
			print("	"+str(contador+1)+" - "+valor["region"])
			paises.append(chave)
			contador=contador+1
		print("	0 - Voltar")
		print("Resposta: ", end="")
		paisEscolhido=int(input())
		if(paisEscolhido>0 and paisEscolhido<=len(paises)):
			x=[]
			for key, value in dicionarioAthlete.items():
				if(value['noc']==paises[paisEscolhido-1]):
					if value['year'] not in x:
						x.append(value['year'])
			x.sort()

			opcao=3
			while(opcao!=1 and opcao!=2 and opcao!=0):
				print ("\n" * 130)
				print("Escolha a temporada:")
				print("	1 - Verão")
				print("	2 - Inverno")
				print("	0 - Voltar")
				print("Resposta: ", end="")
				opcao=int(input())
				print ("\n" * 130)

			homemArray=[]
			mulherArray=[]
			ambosArray=[]
			if(opcao==1):
				for i in x:
					homem=0
					mulher=0
					ambos=0
					for key, value in dicionarioAthlete.items():
						if(value['noc']==paises[paisEscolhido-1]):
							if(value['sex']=='M' and value['season']=='Summer' and value['year']==i):
								homem=homem+1
							elif(value['sex']=='F' and value['season']=='Summer' and value['year']==i):
								mulher=mulher+1
					homemArray.append(homem)
					mulherArray.append(mulher)
					ambos=homem+mulher
					ambosArray.append(ambos)
			elif(opcao==2):
				for i in x:
					homem=0
					mulher=0
					ambos=0
					for key, value in dicionarioAthlete.items():
						if(value['noc']==paises[paisEscolhido-1]):
							if(value['sex']=='M' and value['season']=='Winter' and value['year']==i):
								homem=homem+1
							elif(value['sex']=='F' and value['season']=='Winter' and value['year']==i):
								mulher=mulher+1
					homemArray.append(homem)
					mulherArray.append(mulher)
					ambos=homem+mulher
					ambosArray.append(ambos)
			x1 = np.array(x)
			y1 = np.array(homemArray)
			y2 = np.array(mulherArray)
			y3 = np.array(ambosArray)
			plt.figure(figsize=(10,7))
			plt.plot(x1, y1, "-r", label="Mulheres")
			plt.plot(x1, y2, "-b", label="Homens")
			plt.plot(x1, y3, "-y", label="Ambos")
			plt.legend(loc="upper left")
			plt.plot(y1, marker = 'o')
			plt.plot(y2, marker = 'o')
			plt.plot(y3, marker = 'o')
			plt.grid(axis = 'y')
			plt.grid(axis = 'x')
			plt.xlabel("Anos de olimpíadas do país")
			plt.ylabel("Quantidade de atletas")
			plt.title("Gráfico L2 (Linhas) - " + paises[paisEscolhido-1])
			plt.show()
		elif(paisEscolhido==0):
			return
		paises.clear()
		print ("\n" * 130)

def graficoB3(dicionarioAthlete,dicionarioComiteOlimpico):
	identificadorPaisEscolhido=1
	paises=[]
	paisesEscolhidos=[]
	print("Escolha abaixo um país:")
	contador=0
	for chave, valor in dicionarioComiteOlimpico.items():
		print("	"+str(contador+1)+" - "+valor["region"])
		paises.append(chave)
		contador=contador+1
	print("	0 - Concluir")
	while(identificadorPaisEscolhido!=0):
		print("Resposta: ", end="")
		identificadorPaisEscolhido=int(input())
		if(identificadorPaisEscolhido>0 and identificadorPaisEscolhido<=len(paises)):
			if identificadorPaisEscolhido-1 not in paisesEscolhidos:
				paisesEscolhidos.append(paises[identificadorPaisEscolhido-1])
		elif(identificadorPaisEscolhido!=0):
			print("Valor inválido, digite um indicador válido de país.")
	print ("\n" * 130)

	if(len(paisesEscolhidos)>0):
		identificadorJogoOlimpicoEscolhido=1
		jogos=[]
		while(identificadorJogoOlimpicoEscolhido!=0):
			print("Escolha abaixo uma olimpíada:")
			contador=0
			for chave, valor in dicionarioAthlete.items():
				if valor["games"] not in jogos:
					print("	"+str(contador+1)+" - "+valor["games"])
					jogos.append(valor["games"])
					contador=contador+1
			print("	0 - Voltar")
			print("Resposta: ", end="")
			identificadorJogoOlimpicoEscolhido=int(input())
			if(identificadorJogoOlimpicoEscolhido>0 and identificadorJogoOlimpicoEscolhido<=len(jogos)):
				homens=[0 for i in range(len(paisesEscolhidos))]
				mulheres=[0 for i in range(len(paisesEscolhidos))]
				for chave, valor in dicionarioAthlete.items():
					if valor['noc'] in paisesEscolhidos:
						if(valor['sex']=='M' and valor['games']==jogos[identificadorJogoOlimpicoEscolhido-1]):
							homens[paisesEscolhidos.index(valor['noc'])]=homens[paisesEscolhidos.index(valor['noc'])]+1
						if(valor['sex']=='F' and valor['games']==jogos[identificadorJogoOlimpicoEscolhido-1]):
							mulheres[paisesEscolhidos.index(valor['noc'])]=mulheres[paisesEscolhidos.index(valor['noc'])]+1

				larguraDaBarra=0.25
				plt.figure(figsize=(10,5))
				posicaoDaBarraHomem=np.arange(len(homens))
				posicaoDaBarraMulher=[x+larguraDaBarra for x in posicaoDaBarraHomem]
				plt.bar(posicaoDaBarraHomem, homens, color="#6A5ACD", width=larguraDaBarra, label='Homens')
				plt.bar(posicaoDaBarraMulher, mulheres, color="#6495ED", width=larguraDaBarra, label='Mulheres')
				plt.xlabel('Países')
				plt.xticks([posicao+0.125 for posicao in range(len(homens))], paisesEscolhidos)
				plt.ylabel('Quantidade de Atletas')
				plt.title('Gráfico B3 (Barras) - Quantidade de homens e mulheres por país na olimpíada '+jogos[identificadorJogoOlimpicoEscolhido-1])
				plt.legend()
				plt.show()

			elif(identificadorJogoOlimpicoEscolhido!=0):
				print("Valor inválido, digite um indicador válido de jogos olímpicos.")
			jogos.clear()
			homens.clear()
			mulheres.clear()
			print ("\n" * 130)
	else:
		print("Nenhum país foi selecionado.")

def graficoX3(dicionarioAthlete):
	paises=[]
	auxiliarParaTrocarNomesEixoX=[]
	cont=0
	for chave, valor in dicionarioAthlete.items():
		if valor['noc'] not in paises:
			paises.append(valor['noc'])
			auxiliarParaTrocarNomesEixoX.append(cont+1)
			cont=cont+1
	listasDeIdadesPorPais=[[] for i in range(len(paises))]
	for chave, valor in dicionarioAthlete.items():
		if (valor['age'] not in listasDeIdadesPorPais[paises.index(valor['noc'])] and valor['age']!='NA'):
			listasDeIdadesPorPais[paises.index(valor['noc'])].append(int(valor['age']))
	plt.figure(figsize=(10,7))
	plt.boxplot(listasDeIdadesPorPais)
	plt.xticks(auxiliarParaTrocarNomesEixoX,paises)
	plt.xlabel('Países')
	plt.ylabel('Idade dos Atletas')
	plt.title("Gráfico X3 (Bloxpot) - Idades dos atletas de cada país")
	plt.show()

def carregandoDados(dicionarioAthlete,dicionarioComiteOlimpico,dicionarioContinentes):
	with open("athlete_events.xls","r") as csvarquivo:
		arquivo=csv.reader(csvarquivo)
		for linha in arquivo:
			dicionarioAthlete[linha[0]]={
				"name":linha[1],
				"sex":linha[2],
				"age":linha[3],
				"height":linha[4],
				"weight":linha[5],
				"team":linha[6],
				"noc":linha[7],
				"games":linha[8],
				"year":linha[9],
				"season":linha[10],
				"city":linha[11],
				"sport":linha[12],
				"event":linha[13],
				"medal":linha[14],
			}
	csvarquivo.close()

	with open("noc_regions.csv", "r") as csvarquivo:
		arquivo=csv.reader(csvarquivo)
		next(arquivo)
		for linha in arquivo:
			dicionarioComiteOlimpico[linha[0]]={
				"region":linha[1],
				"notes":linha[2],
			}
	csvarquivo.close()
	
	with open("countries-continents.csv", "r") as csvarquivo:
		arquivo=csv.reader(csvarquivo)
		next(arquivo)
		for linha in arquivo:
			dicionarioContinentes[linha[1]]={
				"continente":linha[0],
			}
	csvarquivo.close()

def main():
	opcao=1
	dicionarioAthlete={}
	dicionarioComiteOlimpico={}
	dicionarioContinentes={}
	carregandoDados(dicionarioAthlete,dicionarioComiteOlimpico,dicionarioContinentes)
	while(opcao!=0):		
		print("Escolha abaixo qual gráfico deseja exibir:")
		print("	1 - Gráfico de linhas L2")
		print("	2 - Gráfico de barras B3")
		print("	3 - Gráfico de boxplot X3")
		print("	4 - Resposta textual T7")
		print("	0 - Sair")
		print("Resposta: ", end="")
		opcao=int(input())
		print ("\n" * 130)
		if(opcao==1):
			graficoL2(dicionarioAthlete,dicionarioComiteOlimpico)
		elif(opcao==2):
			graficoB3(dicionarioAthlete,dicionarioComiteOlimpico)
		elif(opcao==3):
			graficoX3(dicionarioAthlete)
		elif(opcao==4):
			#respostaTextualT7()
			print("em breve T7")
		elif(opcao==0):
			return
main()