# Sistema de Gestão de Produtos e Vendas

Este projeto é um **sistema de gestão simples para produtos e vendas**, implementado em Python. Ele permite o cadastro de produtos e clientes, a realização de vendas e o gerenciamento de informações por meio de um banco de dados SQLite.

## 🚀 Funcionalidades
- Cadastro, alteração, exclusão e listagem de produtos.
- Registro e verificação de clientes (com validação de CPF).
- Realização de vendas e atualização automática do estoque.
- Registro detalhado de itens vendidos.

## 🛠️ Arquivos do Projeto
O projeto é organizado em quatro arquivos `.py` e um banco de dados `.db`:

1. **main.py**  
   O ponto de entrada do programa, onde o menu principal é exibido. Permite navegar entre as funcionalidades de "Vendas" e "Produtos".
   
2. **cadastros.py**  
   Contém as funções relacionadas ao cadastro de produtos e vendas, como:
   - Cadastro de produtos.
   - Gerenciamento de vendas (realizar vendas e cancelar vendas).
   
3. **funcoes.py**  
   Fornece funções auxiliares, como limpar a tela, validação de CPF, formatação de datas, entre outras.

4. **classes.py**  
   Define as classes usadas no sistema, como `Cliente` e `Vendas`, encapsulando os dados e as operações relacionadas.

5. **teste.db**  
   O banco de dados SQLite usado para armazenar:
   - Produtos cadastrados.
   - Clientes registrados.
   - Vendas realizadas e itens vendidos.

## 📦 Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **SQLite**: Banco de dados leve e integrado ao Python.
- **Bibliotecas do Python**: 
  - `sqlite3` para manipulação do banco de dados.
  - `os` para manipulação de arquivos e diretórios.
  - `datetime` para gerenciamento de datas.

## 📖 Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
