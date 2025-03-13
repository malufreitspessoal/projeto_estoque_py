from cadastros import (cad_vendas, cad_produtos)
from funcoes import *
from classes import *

while True:
    print('-' * colunas)
    print('1 -  Vendas')
    print('2 -  Produtos')
    print('-' * colunas)
    print('S - Sair\n')
    opcao = input().strip().upper()
    # limpar_tela()
    
    match (opcao):
        case '1':
            cad_vendas()  #sub programa
        
        case '2':
            cad_produtos() #sub programa

        case 'S':
            print('Até mais :)')
            exit()
        case _:
            print('Opção inválida')