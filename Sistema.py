# sistema que vai verificar se ha login , se nao tiver Criar um novo e 
# armazenar no banco de dados
# ver o seu email e usuario
#atualizar o email ou o usuario
#excluir os mesmo


import mysql.connector


    

conexao = mysql.connector.connect(
         host='localhost',
         user='root',
         password='123456',
         database='SistemadeLogin'
)
cursor = conexao.cursor()

# CREATE

def insertnobanco (para1, para2, para3):
    insertinbanco = 'INSERT into Usuario ( NomeUsuario , SenhaUsuario , Email )' \
    f' values ("{para1}" , "{para2}" , "{para3}" )'
    cursor.execute(insertinbanco)
    

    







# READ

select_Banco = "SELECT NomeUsuario from Usuario "
cursor.execute(select_Banco)
verbanco = cursor.fetchall()

Nomes = []
for row in verbanco:
    print(row)
    Nomes.append (row[0])

print (Nomes)

select_Senha = "SELECT SenhaUsuario from Usuario "
cursor.execute(select_Senha)
versenha = cursor.fetchall()

Senhas = []
for row2 in versenha:
    print(row2)
    Nomes.append (row2[0])

print (Senhas)



select_Senha = "SELECT Email from Usuario "
cursor.execute(select_Senha)
veremails = cursor.fetchall()

Emails = []
for row3 in veremails:
    print(row3)
    Nomes.append (row3[0])

print (Emails)


print(verbanco)


#UPDATE
# cursor.execute(update)




#DELETE

# def deletyou(Email):
#     comando = 





#funcoes
def cadastro():
    while True:
        
        print("Vamos te cadastrar em Nosso Banco de Dados")
        User= input("Enter your ursername :  ")
        Password = input(" enter your send")
        Email = input ("Enter Your best Email :  ")
        if User in Nomes:
            print("your username is already in use.") 
            continue
        elif len(User) < 5:
            print( 'Invalid your user have -5 words')
            continue
        elif len(Password) <5:
            print("the Password cannot less than five words")
        else: 
            insertnobanco(User,Password,Email)
            print("Cadastro concluido com Sucesso")

            break




#Backeeend 
Question_Principal = input("Voce quer Criar seu cadastro(cadastrar) , logar (login) , excluir(delete) ou Atualizar(update) ?")
if Question_Principal.lower() in ["logar","log","login"]:
    print("Bem Vindo ao sistema de login ")
    pergunta1 = input("e seu primeiro login ?")
elif Question_Principal.lower() in {"cadastrar","cadastro"}:
    cadastro()

elif Question_Principal.lower() in {"update","upd","updat","upar","atualizar"}:print()

    
conexao.commit()