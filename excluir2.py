import mariadb
conexao = mariadb.connect(host='localhost', user='root',
                          password='', database='filmes_sql')
cursor = conexao.cursor()

id = input("Digite o id do filme a ser excluído: ")

cursor.execute(f"SELECT * FROM filme WHERE idFilme = {id}")

if cursor.rowcount == 0 :
    print("REGISTRO NÃO ENCONTRADO.")

else:  # achou o registro
    print(cursor.fetchone())
    resposta = input("Apagar esse registro? (s/n) ")
    if resposta == 's' :
        cursor.execute(f"DELETE FROM filme WHERE idFilme = {id}")
        conexao.commit()
        print("EXCLUÍDO COM SUCESSO.")

conexao.close()