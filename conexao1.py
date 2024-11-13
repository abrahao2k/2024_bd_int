# 1. importar o driver
import mariadb
print("Driver carregado.")

# 2. estabelecer a conexao
conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="")
print("Conexão estabelecida.")

# 3. criar um cursor que executa comandos sql
cursor = conexao.cursor()
print("Cursor criado.")

# 4. executar comandos sql no bd
cursor.execute("SHOW DATABASES")

for banco in cursor:
    print(banco)
    
    