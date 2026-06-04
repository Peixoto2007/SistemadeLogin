import mysql.connector


    

conexao = mysql.connector.connect(
         host='localhost',
         user='root',
         password='123456',
         database='SistemadeLogin'
)
cursor = conexao.cursor()

# CREATE

# update ='UPDATE Usuario set SenhaUsuario = "Dyegoprocuraestagioagosto" WHERE id = 1 '



# insert = 'INSERT into Usuario values ( 2 , "Maria" , "marialuciana1982@" , "maria192luciana@hotmail.com" )'

# cursor.execute(update),
# cursor.execute(insert)


# READ

select_Banco = "SELECT NomeUsuario from Usuario "
cursor.execute(select_Banco)
verbanco = cursor.fetchall()

Nomes = []
for row in verbanco:
    print(row)
    Nomes.append (row[0])

print (Nomes)
# print(verbanco)

# select_usuario = "SELECT NomeUsuario from Usuario"
# ver = cursor.execute(select_usuario)
# for NamesUsu in Seenames:
#     print (NamesUsu)



# conexao.commit()



#Backeeend manito
#funcoes
def cadastro():
    while True:
        print("Vamos te cadastrar em Nosso Banco de Dados")
        User= input("Digita o Nome do seu usuario :  ")
        Email = input ("Your best Email :  ")
        if User in Nomes: 
            print( 'Invalid')
            continue
        else : break

#funcoes
print("Bem Vindo ao sistema de login ")
pergunta1 = input("e seu primeiro login ?")
if pergunta1.lower() in {"sim","s","si","ss"}:
    cadastro()

    
