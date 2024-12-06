# 1 IMPORTAR O DRIVER
import mariadb

# 2 CRIAR A CONEXÃO COM O BD
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="inventario")

# 3 CRIAR UM CURSOR
c = conexao.cursor()

#print("CONECTADO AO BANCO DE DADOS")

def cadastrar():
    print('\n\n==== CADASTRAR EQUIPAMENTO ====')
    descricao = input("Descrição do equipamento: ")
    local = input("Local do equipamento: ")
    c.execute(
    f"INSERT INTO equipamentos VALUES(null, '{descricao}','{local}')")
    conexao.commit()
    print("GRAVADO COM SUCESSO \n\n")


def pesquisar():
    print('\n\n==== PESQUISAR EQUIPAMENTO ====')
    descricao = input("Descrição do equipamento: ")
    local = input("Local do equipamento: ")
    c.execute(f'''SELECT * FROM equipamentos WHERE
                descricao LIKE '%{descricao}%' AND
                localizacao LIKE '%{local}%' ''')
    
    for linha in c:
        print(linha)
    
    print(c.rowcount, "resultados encontrados.\n\n")


def excluir():
    print("\n\n==== EXCLUIR EQUIPAMENTO ====")
    cod = input("Digite o código do equipamento: ")
    c.execute(f"SELECT * FROM equipamentos WHERE codigo = {cod}")
    if c.rowcount == 0 :
        print("CÓDIGO NÃO ENCONTRADO\n\n")
    else:
        print(c.fetchone())
        resposta = input("Confirma a exclusão? (s/n) ")
        if resposta.lower() == 's' :
            c.execute(f"DELETE FROM equipamentos WHERE codigo = {cod}")
            conexao.commit()
            print("EXCLUÍDO COM SUCESSO.\n\n")
        else:
            print("CANCELADO. NADA MUDOU. \n\n")


def alterar():
    print("\n\n==== ALTERAR DADOS ====")
    cod = input("Digite o código do equipamento: ")
    c.execute(f"SELECT * FROM equipamentos WHERE codigo = {cod}")
    if c.rowcount == 0 :
        print("CÓDIGO NÃO ENCONTRADO\n\n")
    else:
        print(c.fetchone())
        col = input("Alterar qual coluna? (1-Descricao/2-Local) ")
        if col   == "1" : col = "descricao"
        elif col == "2" : col = "localizacao"
        
        valor = input("Novo valor: ")
        c.execute(f'''UPDATE equipamentos SET {col} = '{valor}'
                    WHERE codigo = {cod} ''')
        conexao.commit()
        print("ATUALIZADO COM SUCESSO\n\n")
        
        
        
opcao = 1
while opcao < 5 :
    print("==== INVENTÁRIO DE EQUIPAMENTOS ====")
    print("1 - Cadastrar")
    print("2 - Pesquisar")
    print("3 - Excluir")
    print("4 - Alterar")
    print("5 - Sair")
    opcao = int(input("Digite a opção: "))
    
    if   opcao == 1 : cadastrar()
    elif opcao == 2 : pesquisar()
    elif opcao == 3 : excluir()
    elif opcao == 4 : alterar()
    else            : print("Até logo!")

    
