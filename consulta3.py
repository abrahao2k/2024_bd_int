import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="filmes_sql")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM ator ORDER BY nome")

dados = cursor.fetchall()  # transfere todos as linhas
print(dados)
print(cursor.rowcount, "resultados.")

#dados2 = cursor.fetchall()
#print(dados2)

#linha = cursor.fetchone() # transfere uma linha por vez
#print(linha)

#varios = cursor.fetchmany(3) # indica a quantidade de linhas
#print(varios)

#print(cursor.description) # detalhes sobre a tabela e colunas

cursor.close()
conexao.close()