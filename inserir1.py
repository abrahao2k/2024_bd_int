import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="dois")
cursor = conexao.cursor()

print("=== CADASTRO DE DUPLAS ===")
primeiro = input("Primeiro: ")
segundo = input("Segundo: ")

cursor.execute(f''' INSERT INTO DUPLAS VALUES(null,
'{primeiro}','{segundo}') ''')

conexao.commit()  # efetiva a gravação no bd
print("Gravado com sucesso.")