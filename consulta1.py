import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="filmes_sql")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM ator ORDER BY nome")

for linha in cursor:
    print(linha[1])

cursor.close()
conexao.close()

