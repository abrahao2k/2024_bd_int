import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="livraria")
cursor = conexao.cursor()

cursor.execute("SHOW TABLES")

for tabela in cursor:
    print(tabela)
    
cursor.execute("SELECT * FROM AUTOR ORDER BY NOME")

for linha in cursor:
    print(linha[1])