
from funcoes import *
class Vendas:
    
    # codigo_venda = 0
    
    def __init__(self, data =None):
        # self.id_venda = self.gerar_venda()
        self.data = data
        
        
def __str__(self):
        return f"Cliente: {self.nome}, Produtos: R${self.quantidade_produtos}"
    # def gerar_venda():
    #     return (Vendas.codigo_venda + 1)


class Produtos:
    
    # codigo_produto = 0
    
    def __init__(self, nome, descricao, quantidade_disponivel, preco):
        # self.codigo_produto = self.gerar_produto()
        self.nome = nome
        self.descricao = descricao
        self.quantidade_disponivel = quantidade_disponivel
        self.preco = preco
    
    # def gerar_produto():
        # return (Produtos.codigo_produto + 1)

class Cliente:
     def __init__(self, nome_cliente, cpf_cliente):
        self.nome_cliente= nome_cliente
        self.cpf_cliente = cpf_cliente
        