# sistema que vai verificar se ha login , se nao tiver Criar um novo e 
# armazenar no banco de dados
# ver o seu email e usuario
#atualizar o email ou o usuario
#excluir os mesmo


import mysql.connector


    
EMAIL = ""
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
    print("Segue dados : ")
    print(para1, para2, para3)
    
    


# READ

select_Usuario = "SELECT NomeUsuario from Usuario "
cursor.execute(select_Usuario)
verusuario = cursor.fetchall()
print(verusuario)

Nomes = []
for row in verusuario:
    print(row)
    Nomes.append (row[0])

print (Nomes)

select_Senha = "SELECT SenhaUsuario from Usuario "
cursor.execute(select_Senha)
versenha = cursor.fetchall()

Senhas = []
for row2 in versenha:
    print(row2)
    Senhas.append (row2[0])

print (Senhas)



select_Senha = "SELECT Email from Usuario "
cursor.execute(select_Senha)
veremails = cursor.fetchall()

Emails = []
for row3 in veremails:
    print(row3)
    Emails.append (row3[0])

print (Emails)



#UPDATE
# cursor.execute(update)




# DELETE
def deletyou():
    email = input("Digite o email que deseja excluir: ")

    delete = f'DELETE FROM Usuario WHERE Email = "{email}"'

    cursor.execute(delete)
    conexao.commit()

    print("User delete succesfuly")





#funcoes
def cadastro():
    while True:
        print("Vamos te cadastrar em Nosso Banco de Dados")
        User = input("Enter your username: ")
        Password = input("Enter your password: ")
        Email = input("Enter your best email: ")

        if User in Nomes:
            print("Your username is already in use.")
            continue
        elif len(User) < 5:
            print("Invalid: username must have at least 5 characters.")
            continue
        elif len(Password) < 5:
            print("Password cannot be less than five characters.")
            continue  
        else:
            insertnobanco(User, Password, Email)
            print("Cadastro concluído com sucesso")
            return User, Password, Email 



#Backeeend 
Question_Principal = input("Voce quer Criar seu cadastro ->(cadastrar) , logar ->(login) , excluir ->(delete) ou Atualizar ->(update) ?")
if Question_Principal.lower() in ["logar","log","login"]:
    print("Bem Vindo ao sistema de login ")
    pergunta1 = input("e seu primeiro login ?")
elif Question_Principal.lower() in {"cadastrar","cadastro"}:
    cadastro()

elif Question_Principal.lower() in {"update","upd","updat","upar","atualizar"}:print()

elif Question_Principal.lower() in {"cadastrar","cadastro"}:
    cadastro()
elif Question_Principal.lower() in {"delete","deletar","delet"}:
    deletyou()
    if cursor.rowcount == 0:
        print("Email não encontrado")
    else: print("Usuário excluído")
    s = input("so isso ? ")    
    conexao.commit()