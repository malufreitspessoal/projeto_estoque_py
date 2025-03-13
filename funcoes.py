import os
import platform
from datetime import datetime 


colunas = 60


def limpar_tela():
        sistema = platform.system()
        if sistema == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

def modelar_data():
    data = datetime.now()
    data_alterada = data.strftime('%d/%m/%Y %H:%M:%S')
    return( data_alterada)

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos ou se todos são iguais
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    # Verifica se os dígitos calculados são iguais aos do CPF
    return cpf[-2:] == f"{digito1}{digito2}"