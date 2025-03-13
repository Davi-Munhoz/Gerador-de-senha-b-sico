tam = 40

def cabecalho(msg):
    '''
    Faz um cabeçalho formatado.
    :param msg: O texto que será adicionado ao cabeçalho
    '''
    linha()
    print(msg.center(tam))
    linha()

def menu():
    '''
    Imprime um menu na tela com 4 opções
    '''
    print('''Escolha uma opção:
1- Senha Simples (somente números)
2- Senhas medianas (Numeros e Letras)
3- Senhas complexas (números, letras e caracteres especiais)
4- Sair''')
    linha()

def linha():
    '''
    Imprime uma linha com um tamanho pré determinado
    '''
    print('-'*tam)
