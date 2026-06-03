import mysql.connector

conexao = mysql.connector.connect(
         host='localhost',
         user='root',
         password='123456',
         database='SistemadeLogin'
)
cursor = conexao.cursor()
# 
# CREATE
# 
# update ='UPDATE Usuario set SenhaUsuario = "Dyegoprocuraestagioagosto" WHERE id = 1 '
# 
# 
# 
# insert = 'INSERT into Usuario values ( 2 , "Maria" , "marialuciana1982@" , "maria192luciana@hotmail.com" )'
# 
# cursor.execute(update),
# cursor.execute(insert)
# 
# READ

select_usuario = "SELECT * from Usuario "
cursor.execute(select_usuario)
resultado = cursor.fetchall() 


for i in resultado:
    print (i)



conexao.commit()

# drop =0 ,  
# 
# 
# def verificar_login(email, senha):
#    
    # 
    # 
    # )
    # 
    # cursor = conexao.cursor()
    # select = 'Select * from Usuario Where Email * '
    # 