import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="desafiofinal_turmaa"
)

meucursor = banco.cursor()
pesquisa = 'select * from alunos;'
meucursor.execute(pesquisa)

#FETCHALL recebe tudo da pesquisa e retorna atraves de uma tupla
resultado=meucursor.fetchall()
for x in resultado:
    print(x)
nome1 = ''
telefone1='81 1111-2222'
cursor = banco.cursor()
sql = 'insert into alunos (nome, telefone) values (%s, %s)'
data = (nome1, telefone1)
cursor.execute(sql, data)
banco.commit()
userid = cursor.lastrowid
print(userid)
cursor.close()
banco.close()