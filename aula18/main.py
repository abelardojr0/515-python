import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "mysqladmin102030",
    "database": "locadora"
}
def mexer_no_banco(query):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(query)
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Alteração realizada com sucesso")

def consultar_o_banco(query):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(query)
    lista_de_livros = cursor.fetchall()
    cursor.close()
    conexao.close()
    return lista_de_livros






while True:
    menu = int(input("""
    Escolha uma opção:
    1 - Adicionar Filme
    2 - Ver todos os Filmes
    3 - Editar Filme
    4 - Deletar Filme
    0 - Sair
"""))
    match menu:
        case 1:
            nome_do_filme = str(input("Digite o nome do filme: "))
            genero_do_filme = str(input("Digite o gênero do filme: "))
            ano_do_filme = int(input("Digite o ano do filme: "))
            preco_do_filme = float(input("Digite o preço do filme: "))

            consulta = f"""
                INSERT INTO filmes (nome, genero, ano, preco)
                VALUES 
                    ("{nome_do_filme}", "{genero_do_filme}", {ano_do_filme}, {preco_do_filme});
            """
            mexer_no_banco(consulta)
        case 2:
            consulta = "SELECT * FROM filmes"
            lista_de_filmes = consultar_o_banco(consulta)
            for filme in lista_de_filmes:
                print(filme)
        case 3:
            consulta = "SELECT * FROM filmes"
            lista_de_filmes = consultar_o_banco(consulta)

            for filme in lista_de_filmes:
                print(filme)

            escolha_id = int(input("Digite o número do filme que você quer editar: "))
            novo_nome_do_filme = str(input("Digite o novo nome do filme: "))
            novo_genero_do_filme = str(input("Digite o novo gênero do filme: "))
            novo_ano_do_filme = int(input("Digite o novo ano do filme: "))
            novo_preco_do_filme = float(input("Digite o novo preço do filme: "))

            consulta = f"""UPDATE filmes SET
            nome = "{novo_nome_do_filme}",
            genero = "{novo_genero_do_filme}",
            ano = {novo_ano_do_filme},
            preco = {novo_preco_do_filme}
            WHERE id = {escolha_id}
              """
            
            mexer_no_banco(consulta)
        case 4:
            consulta = "SELECT * FROM filmes"
            lista_de_filmes = consultar_o_banco(consulta)

            for filme in lista_de_filmes:
                print(filme)
            escolha_id = int(input("Digite o número do filme que você quer deletar: "))

            consulta = f"DELETE FROM filmes WHERE id = {escolha_id}"
            mexer_no_banco(consulta)
            
        case 0:
            break
        case _:
            print("Opção Inválida")




        
