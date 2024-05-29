import Funcoes
sair = False
while sair == False:
	inicio = int(input("Digite <1> - Login, <2> - Cadastro, <3> - Enciclopedia, <4> - sair \n"))
	match inicio:
		case 1:
			entrou = Funcoes.login()
			if(entrou):
				Funcoes.logado()
		case 2:
			user = Funcoes.addUser()
			Funcoes.tudoCertoUser(user)
		case 3:
			Funcoes.imprimir()
		case 4:
			sair = True
		case _:
			print("Você digitou algo que está fora das opções")