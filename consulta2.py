import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="filmes_sql")
cursor = conexao.cursor()

nome = input("Nome do ator? ")

cursor.execute(f"SELECT * FROM ator WHERE nome LIKE '%{nome}%' ")

for linha in cursor:
    print(linha[1])
    
print(cursor.rowcount, "resultados encontrados.")

cursor.close()
conexao.close()
