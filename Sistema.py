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
def update_nome(para1,para2):
    comando = f'UPDATE Usuario SET NomeUsuario = "{para1}" WHERE Email = "{para2}"'
    cursor.execute(comando)

def update_senha(para1,para2):
    comando = f'UPDATE Usuario SET SenhaUsuario = "{para1}" WHERE Email = "{para2}"'
    cursor.execute(comando)





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


def senha_certa(email,senha):
    print()

#Backeeend 
while True:
    Question_Principal = input("Voce quer Criar seu cadastro ->(cadastrar) , logar ->(login) , excluir ->(delete), Atualizar ->(update) ou Sair -> (Exit or Sair) ?")
    if Question_Principal.lower() in {"logar","log","login"}:
            logando = input("Digite seu Email ou User : ")
            if logando in Emails or Nomes:
                senhauser= input("Digite sua senha : ")
            
            else: print(" Esse email não esta cadastrado ")

    elif Question_Principal.lower() in {"cadastrar","cadastro"}:
        cadastro()
        break



    elif Question_Principal.lower() in ["update","upd","updat","upar","atualizar"]:
        while True:
            Atualizaroque=input(" O que voce quer atualizar ? ( Name , Email or Password ?)")
            if Atualizaroque.lower() in ["name","nome","nombre"]:
                seuEmail = input("Digita seu Email: ")
                Userupdate = input("Novo User : ")
                if seuEmail in Emails:
                    update_nome(Userupdate,seuEmail)
                    something_name1 = input("Something more ?")
                    if something_name1.lower() in ["yes","sim","ya","si"]:
                            continue
                    else: break 

            elif Atualizaroque.lower() in ["senha","password","send"]:
                while True:
                    seuEmail = input("Digita seu Email: ")
                    senhaupdate = input("New Password : ")
                    if seuEmail in Emails:
                        update_senha(senhaupdate,seuEmail)
                        something_name2 = input("Something more ?")
                        if something_name2.lower() in ["yes","sim","ya","si"]:
                            continue
                        else: break
            
    elif Question_Principal.lower() in ["delete","deletar","delet"]:
        while True:
            deletyou()
            if cursor.rowcount == 0:
                print("Email não encontrado")
                continue
            else: print("Usuário excluído") 
            break
    elif Question_Principal.lower() in ["sair","exit"]:
        break
s = input("so isso ? ") 
if s in ["sim","yes","s","ye"]:  
    print("commit")
    conexao.commit()
    print("commit feito")
