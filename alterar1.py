import mariadb
conexao = mariadb.connect(host='localhost', user='root',
                          password='', database='filmes_sql')
cursor = conexao.cursor()

id = input("Digite o id do filme a ser alterado: ")

cursor.execute(f"SELECT * FROM filme WHERE idFilme = {id}")

if cursor.rowcount == 0 :
    print("REGISTRO NÃO ENCONTRADO.")

else:  # achou o registro
    dados = cursor.fetchone()
    print("Titulo :", dados[1])
    print("Ano :", dados[2])
    print("Orçamento :", dados[3])
    print("idDiretor :", dados[4])
    
    coluna = input("Qual culuna deseja alterar? ")
    
    if coluna.lower() in ('titulo','ano','orçamento','iddiretor'):
        valor = input("Digite a nova informação: ")
        cursor.execute(
        f"UPDATE filme SET {coluna} = '{valor}' WHERE idfilme={id}")
        conexao.commit()
        print("ATUALIZADO COM SUCESSO.")
    else:
        print("Coluna inválida.")

cursor.close()
conexao.close()