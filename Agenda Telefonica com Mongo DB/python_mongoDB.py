#Autor: Vagner Franca
#TADS 2021.1
#Minipulando banco de dados MongoDB

#Imports do BD
import pymongo

ligando banco de dados
user = pymongo.MongoClient('localhost', 27017)
db = user.iptv
colection = db.clientes

###ligando banco de dados (TESTE)
##user = pymongo.MongoClient('localhost', 27017)
##db = user.test
##colection = db.clientes

#Funcoes
def cadastro(): #OK
    idCliente = int(colection.count_documents({}))+1
    print("")
    name = input("nome> ")
    contato = input("telefone> ")
    end = input("endereco> ")
    typ = int(input("plano(1-basic/2-premium)> "))

    if(typ == 1):
        typ = "basic"
        valor = 15
    else:
        plano = "premium"
        valor = 30

    pessoa = {"_id_cliente": idCliente,"nome":name,"telefone":contato,"endereco":end,"plano":typ,"preco":valor,"status":"on"}
    colection.insert_one(pessoa)
    
def listaTodos(): #OK
    for x in colection.find({},{"_id":0}):
        print(x)

def menuBusca(): #OK
    print("")
    print("-MENU DE BUSCA-")
    print("1- id")
    print("2- nome")
    print("3- status(on/off)")
    print("4- plano (basic/premium)")
    busca = int(input(">>> "))

    if(busca == 1):
        print("")
        idbusca = int(input("ID>> "))
        if(idbusca > colection.count_documents({}) or idbusca < 1):
            print("")
            print("invalido")
        else:
            print("")
            print(colection.find_one({"_id_cliente": idbusca}, {"_id": 0}))

    elif(busca == 2):
        nmBusca = input("Nome>> ")
        if(colection.find_one({"nome": nmBusca})):
            print(colection.find_one({"nome": nmBusca}, {"_id": 0}))
        else:
            print("Nao encontrado")

    elif(busca == 3):
        state = int(input("1- ON \ 2- OFF>> "))
        if(state == 1):
            print("")
            for x in colection.find({"status": "on"},{"_id":0}):
                print(x)
        else:
            print("")
            for x in colection.find({"status": "off"},{"_id":0}):
                print(x)

 
    elif(busca == 4):
        plane = int(input("1- BASIC \ 2- PREMIUM>> "))
        if(plane == 1):
            print("")
            for x in colection.find({"plano": "basic"},{"_id":0}):
                print(x)
        else:
            print("")
            for x in colection.find({"plano": "premium"},{"_id":0}):
                print(x)
    else:
        print("")
        print("invalido")
    
def desativa(): #OK
    achou = int(0);
    while(achou != 1):
        print("")
        print("-DESATIVAR CLIENTE-")
        print("1-Listar todos")
        print("2- Buscar")
        list = int(input(">>> "))
        
        if(list == 1):
            listaTodos()
        else:
            menuBusca()

        achou = int(input("encontrou(1-Sim \ 2- Nao)>>> ")) 
        
    print("")
    idbusca = int(input("Informe o id>>> "))
    colection.update_one({"_id_cliente": idbusca}, {'$set':{"status": "off"}})
    print(colection.find_one({"_id_cliente": idbusca}, {"_id": 0, "endereco": 0, "telefone":0}))

def ativa(): #OK
    achou = int(0);
    while(achou != 1):
        print("")
        print("-ATIVAR CLIENTE-")
        print("1-Listar todos")
        print("2- Buscar")
        list = int(input(">>> "))
        
        if(list == 1):
            listaTodos()
        else:
            menuBusca()

        achou = int(input("encontrou(1-Sim \ 2- Nao)>>> ")) 
        
    print("")
    idbusca = int(input("Informe o id>>> "))
    colection.update_one({"_id_cliente": idbusca}, {'$set':{"status": "on"}})
    print(colection.find_one({"_id_cliente": idbusca}, {"_id": 0, "endereco": 0, "telefone":0}))

def edita(): #OK
    achou = int(0)
    while(achou != 1):
        print("")
        print("-EDITAR CLIENTE-")
        print("1-Listar todos")
        print("2- Buscar")
        list = int(input(">>> "))
        
        if(list == 1):
            listaTodos()
        else:
            menuBusca()

        achou = int(input("encontrou(1-Sim \ 2- Nao)>>> "))

    x = int(0)

    while((x < 1) or (x > 3)):
        print("")
        print("EDITAR")
        print("1- Endereco")
        print("2- Plano")
        print("3- Telefone")
        x = int(input(">>> "))

    if(x == 1):
        print("")
        newEnd = input("Novo endereco>>> ")
        idbusca = int(input("Informe o id>>> "))
        colection.update_one({"_id_cliente": idbusca}, {'$set':{"endereco": newEnd}})
        print(colection.find_one({"_id_cliente": idbusca}, {"_id": 0, "plano": 0, "telefone":0}))

    elif(x == 2):
        print("")
        newPlan = input("Novo plano>>> ")
        idbusca = int(input("Informe o id>>> "))
        colection.update_one({"_id_cliente": idbusca}, {'$set':{"plano": newPlan}})
        print(colection.find_one({"_id_cliente": idbusca}, {"_id": 0, "endereco": 0, "telefone":0,}))

    elif(x == 3):
        print("")
        newContact = input("Novo Telefone>>> ")
        idbusca = int(input("Informe o id>>> "))
        colection.update_one({"_id_cliente": idbusca}, {'$set':{"telefone": newContact}})
        print(colection.find_one({"_id_cliente": idbusca}, {"_id": 0, "endereco": 0, "plano":0}))

    else:
        print("invalido")
            
def exclui(): #OK
    achou = int(0);
    while(achou != 1):
        print("")
        print("-EXCLUIR CLIENTE-")
        print("1-Listar todos")
        print("2- Buscar")
        list = int(input(">>> "))
        
        if(list == 1):
            listaTodos()
        else:
            menuBusca()

        achou = int(input("encontrou(1-Sim \ 2- Nao)>>> "))

    print("")
    idbusca = int(input("Informe o id>>> "))
    colection.delete_one({"_id_cliente": idbusca})
    print("Cliente Excluido...")

    
def menuPrincipal(): #OK
    menu = int(0)
    while(menu != 6):
        print("")
        print("-Bem vindo-")
        print(" Menu:")
        print("1- Cadastro")
        print("2- Busca")
        print("3- Ativar/Desativar")
        print("4- Editar")
        print("5- Excluir")
        print("6- Sair")
        menu = int(input(">>> "))

        if(menu == 1):
            cadastro()

        elif(menu == 2):
            print("")
            y = int(input("1-Listar Todos / 2- Buscar por campo>>> "))

            if(y == 1):
                listaTodos()
            elif(y == 2):
                menuBusca()
            else:
                print("")
                print("Invalido")
                    
        elif(menu == 3):
            print("")
            y = int(input("1-Ativar / 2-Desativar>>> "))

            if(y == 1):
                ativa()
            elif(y == 2):
                desativa()
            else:
                print("Invalido")

        elif(menu == 4):
            edita()

        elif(menu == 5):
            exclui()
            

        
#main
menuPrincipal()
#insert
