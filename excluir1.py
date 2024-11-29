import mariadb
conexao = mariadb.connect(host='localhost', user='root',
                          password='', database='filmes_sql')
cursor = conexao.cursor()

id = input("Digite o id do filme a ser excluído: ")

cursor.execute(f"DELETE FROM filme WHERE idFilme = {id}")
conexao.commit()

print("EXCLUÍDO COM SUCESSO.")
conexao.close()