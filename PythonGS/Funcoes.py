import Animal
import Usuario
def addUser():
    nome = input("Nome: ")
    usuario = input("Usuario: ")
    senha = input("Senha: ")
    confiSenha = input("Confirmar Senha: ")
    email = input("Email:")
    arroba = False
    while nome == "":
        nome = input("Voce não um digitou um nome \nNome: ")
    while usuario == "":
        usuario = input("Voce não um digitou um nome de usuario \nUsuario: ")
    while senha != confiSenha or senha == "" or confiSenha=="":
        if senha != confiSenha:
            print("a senha e a confirmação de senha não são iguais")
        if senha == "":
            print("voce não digitou a senha")
        if confiSenha == "":
            print("voce não digitou a confirmação de senha")
        senha = input("Senha: ")
        confiSenha = input("Confirmar Senha: ")
    while email == "":
        email = input("Voce não digitou o Email \nEmail:")
    for i in email:
        if i == "@":
            arroba = True
    if arroba == False:
        email += "@gmail.com"
    user = Usuario.Usuario(nome=nome,usuario=usuario,senha=senha,email=email)
    return user
def tudoCertoUser(user):
    print(f'\nConfirmando as informações de cadastro \nNome: {user.nome} \nUsuario: {user.usuario} \nEmail: {user.email}')
    veri = int(input("digite <1> - para sim está tudo certo ou <2> - quero corrigir informação \n"))
    match veri:
        case 1:
            Usuario.listaUsuarios.append(user)
            print("\nCADASTRADO COM SUCESSO")
        case 2:
            addUser()
def login():
    user = input("Usuario: \n")
    senha = input("Senha: \n")
    logou = False
    for i in range(len(Usuario.listaUsuarios)):
        if user == Usuario.listaUsuarios[i].usuario and senha == Usuario.listaUsuarios[i].senha:
            logou = True
            print("Logou com sucesso")
            break
        else:
            print("USUARIO OU SENHA INCORRETOS")
    return logou
def logado():
    cadastrado = int(input("digite <1> - Cadastrar animal <2> - Editar um cadastro \n"))
    match cadastrado:
        case 1:
            '''
            risco, descricao, habitat, populacao
            '''
            especie = input("Espécie: ")
            while especie == "":
                especie = input("Espécie: ")
            risco = bool(input("Risco: "))
            while risco == "":
                risco = bool(input("Risco: "))
            habitat = input("Habitat: ")
            while habitat == "":
                habitat = input("Habitat: ")
            descricao = input("De uma breve Descrição: ")
            while descricao == "":
                descricao = input("De uma breve Descrição: ")
            populacao = input("População: ")
            while populacao == "":
                populacao = input("População: ")
            animal = Animal.Animal(especie,risco,descricao,habitat,populacao)
            Animal.listAnimais.append(animal)
        case 2:
            alterar = int(input("o que voce deseja alterar: <1> - Especie <2> - Risco <3> - Habitat <4> - Descricao <5> - População"))
            match alterar:
                case 1:
                    Animal.listAnimais[0].especie = input("Espécie: ")
                case 2:
                    Animal.listAnimais[0].risco = bool(input("Risco: "))
                case 3:
                    Animal.listAnimais[0].habitat = input("Habitat: ")
                case 4:
                    Animal.listAnimais[0].descricao = input("De uma breve Descrição: ")
                case 5:
                    Animal.listAnimais[0].populacao = input("População: ")
def imprimir():
    print(f"\nEspecie: {Animal.listAnimais[0].especie} \nRisco: {Animal.listAnimais[0].risco} \nHabitat: {Animal.listAnimais[0].habitat} \nPopulação: {Animal.listAnimais[0].populacao} \n\nDescrição: {Animal.listAnimais[0].descricao}")

