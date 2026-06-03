import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='SistemadeLogin'  
)

cursor = conexao.cursor()

comando = 'select * from Usuario'
cursor.execute(comando)
# conexao.commit()
resultado = cursor.fetchall()

print("Dados da tabela Usuario:")
for usuario in resultado:
    print(usuario)

