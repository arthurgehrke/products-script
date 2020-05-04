import mysql.connector

connection = mysql.connector.connect(
    host='', database='', user='', password='', port=)

cursor = connection.cursor()
cursor.execute('select descricao, preco from produto;')
for r in cursor.fetchall():
    print(r)

cursor.execute("insert into produto(descricao,preco) values('teste','50')")
connection.commit()
