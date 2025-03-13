from funcoes import *
from classes import *
import sqlite3 as sql
import os
from datetime import date 

# Caminho absoluto para o banco de dados
caminho_db = os.path.join(os.path.dirname(__file__), "teste.db")

try:
    # Conectar ao banco de dados em modo de leitura/escrita
    conexao = sql.connect(caminho_db)
    
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos(
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            descricao VARCHAR(1000),
            quantidade_disponivel INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes(
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            cpf_cliente VARCHAR(11) unique
        )
    ''')
    # banco de dados com o id da venda, id do cliente que comprou, a data que realizou
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas(
            id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INT,
            data_venda DATE NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)          
        )
    ''') 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS itens_venda(
            id_item_vendido INTEGER PRIMARY KEY AUTOINCREMENT,
            id_venda INT,
            id_produto INT,
            quantidade INT NOT NULL,
            FOREIGN KEY (id_venda) REFERENCES vendas(id_venda),
            FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
            
        )
    ''')
    
    cursor.execute('''
                   ''')
    
except sql.Error as e:
    print(f'Erro no banco de dados: {e}')

def cad_produtos():
    while True:
        # limpar_tela()
        print('-' * colunas)
        print('1 - Incluir Produto')
        print('2 - Alterar Produto')
        print('3 - Exclusão de Produto')
        print('4 - Listagem Geral de Produto')
        print('-' * colunas)
        print('S - Retornar menu principal')
        print('=' * colunas)
        opcao = input(': ').strip().upper()

        match opcao:
            case '1':
                incluir_produto()
            case '2':
                alterar_produto()
            case '3':
                excluir_produto()
            case '4':
                print(listagem_geral())
            case 'S':
                print('Retornando ao menu principal...')
                return
            case _:
                print('Opção inválida. Tente novamente.')

def incluir_produto():
    limpar_tela()
    try:
        nome = input('Nome do produto:\n').upper().strip()
        descricao = input('Descrição do produto:\n').upper().strip()
        
        try: 
            quantidade_disponivel = int(input('Quantidade do produto:\n'))
            preco = float(input('Preço do produto:\n'))
            cursor.execute('''
                INSERT INTO produtos(
                    nome, descricao, quantidade_disponivel, preco)
                VALUES(?, ?, ?, ?)
            ''', (nome, descricao, quantidade_disponivel, preco))
            
            conexao.commit()
            print("Produto cadastrado com sucesso!")
        except ValueError:
            print('Valor inválido para esse campo')
    
    except sql.Error as e:
        print(f"Erro ao cadastrar o produto: {e}")

def alterar_produto():
    limpar_tela()
    nome = input('Nome do produto que você quer atualizar:\n').upper().strip()
    
    if not verificar_produto_se_existente(nome):
        print(f"Produto '{nome}' não encontrado.")
        return
    
    produto_alterado = input('Nome do produto atualizado:\n').upper().strip()
    descricao = input('Descrição do produto atualizado:\n').upper().strip()
    try:
        quantidade_disponivel = int(input('Quantidade do produto atualizado:\n'))
        preco = float(input('Preço do produto atualizado:\n'))
    except ValueError :
        print('Valor inválido para esse campo')
        return
    try:
        cursor.execute('''
            UPDATE produtos
            SET nome = ?,
                descricao = ?,
                quantidade_disponivel = ?,
                preco = ?
            WHERE nome = ?
        ''', (produto_alterado, descricao, quantidade_disponivel, preco, nome))
        
        print(f'''Os valores estão corretos? 
              De {nome} para {produto_alterado}
              Nova descrição: {descricao}
              Nova quantidade: {quantidade_disponivel}
              Novo preço: R${preco}''')
        
        prosseguir = input('Está correto? S/N: ').upper().strip()
        if prosseguir == 'S':
            conexao.commit()
            print('Produto atualizado com sucesso!')
        else:
            print('Alteração cancelada.')
    except sql.Error as e:
        print(f"Erro ao atualizar o produto: {e}")

def verificar_produto_se_existente(nome):
    cursor.execute('''
        SELECT nome, descricao, quantidade_disponivel, preco 
        FROM produtos 
        WHERE nome = ?
    ''', (nome,))
    return cursor.fetchone() is not None

def excluir_produto():
    try:
        nome = input('Nome do produto a ser excluido:  ').upper().strip()
        if verificar_produto_se_existente(nome):
            cursor.execute(f'''
        delete from produtos where nome = ? ''', (nome, ))
            conexao.commit()
            print('Produto removido com sucesso')
        else: 
            print('Produto inexistente')

    except sql.Error as e:
        print(f"Erro ao excluir o produto: {e}")


def listagem_geral(): 
    
    print('-' * colunas)
    
    cursor.execute('''
    select * from produtos''')
    
    lista_de_tuplas = cursor.fetchall()

    for tupla in lista_de_tuplas:
        print(f'ID: {tupla[0]}, Nome: {tupla[1]}, Descrição: {tupla[2]}, Quantidade: {tupla[3]}, Preço: R${tupla[4]}')


def cad_vendas():
    while True:
        limpar_tela()
        print('-' * colunas)
        print('1 - Realizar venda')
        print('-' * colunas)
        print('S - Retornar menu principal')
        print('=' * colunas)
        opcao = input(': ').strip().upper()

        match opcao:
            case '1':
                realizar_venda()               

            case 'S':
                print('Retornando ao menu principal...')
                return
            case _:
                print('Opção inválida. Tente novamente.')
def verificar_cpf_existente(cpf):
    cursor.execute('''
        SELECT cpf_cliente 
        FROM clientes 
        WHERE cpf_cliente = ?
    ''', (cpf,))
    return cursor.fetchone() is not None

def realizar_venda():
    limpar_tela()
    try: 
        cpf_cliente = input('CPF: ').strip()
        cpf_formatado = ''.join(filter(str.isdigit, cpf_cliente))
        if not validar_cpf(cpf_formatado):
            return ('CPF inválido')
        if verificar_cpf_existente(cpf_formatado): # quer dizer que tem o cpf na tabela
            pass
        else:
            nome_cliente = input('Nome do cliente:   ').strip().upper()
            cliente = Cliente(nome_cliente, cpf_formatado)
            cursor.execute('''
                insert into clientes (nome, cpf_cliente) values (?,?)''', (cliente.nome_cliente, cliente.cpf_cliente))
            # conexao.commit()
            
        data_venda = modelar_data()
        venda = Vendas(data_venda)
        cursor.execute('''
            select id_cliente from clientes where cpf_cliente = ? ''', (cpf_formatado,))
        
        id_cliente = cursor.lastrowid
        cursor.execute(''' INSERT INTO vendas (data_venda, id_cliente ) VALUES (?, ?)
        ''', (venda.data, id_cliente))
        
        id_venda = cursor.lastrowid
        
        quantidade_produtos_diferentes_comprados = int(input('Quantidade de produtos diferentes comprados:   '))
        for i in range(1 , quantidade_produtos_diferentes_comprados+1):
             produto_comprado = input(f'Produto {i}:  ').strip().upper()
             quantidade_produto = int(input(f'Quantidade de {produto_comprado}:  '))                   
             cursor.execute('''
                SELECT id_produto, quantidade_disponivel FROM produtos WHERE nome = ?
            ''', (produto_comprado,))
             produto = cursor.fetchone()
             
             if produto:
                id_produto, quantidade_estoque = produto

                # Verificar se há estoque suficiente
                if quantidade_produto > quantidade_estoque:
                    print(f"Erro: Estoque insuficiente para o produto {produto_comprado}.")
                    conexao.rollback()  # Desfazer a transação
                    return

                # Inserir o item vendido na tabela "itens_venda"
                cursor.execute('''
                    INSERT INTO itens_venda (id_venda, id_produto, quantidade) VALUES (?, ?, ?)
                ''', (id_venda, id_produto, quantidade_produto))
                # conexao.commit()

                # Atualizar a quantidade em estoque na tabela "produtos"
                nova_quantidade = quantidade_estoque - quantidade_produto
                cursor.execute('''
                    UPDATE produtos SET quantidade_disponivel = ? WHERE id_produto = ?
                ''', (nova_quantidade, id_produto))
                             
             else:
                print(f"Erro: Produto {produto_comprado} não encontrado.")
                conexao.rollback()  # Desfazer a transação
                return
        conexao.commit()
        print(f"Venda para o cliente {nome_cliente} realizada com sucesso!")
       
    except sql.Error as e:
            print(f"Erro ao realizar a venda: {e}")
    
   
    

