def verificaInt(msg):
    '''
    Solicita um número e verifica se foi digitado um número inteiro
    :param msg: Mensagem de solicitação
    :return: O número digitado
    '''
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print('\033[31mOpção inválida! Tente novamente.\033[m')
        else:
            return n

def caso1(valor):
    '''
    Gera uma senha simples composta somente de números
    :param valor: Quantidade de caracteres
    :return: Volta ao menu caso não seja possível gerar a senha
    '''
    from random import randint
    senha = []
    while len(senha) < valor:
        n = randint(0, 9)
        if str(n) not in senha:
            senha.append(str(n))
    senha = ''.join(senha)
    print(f'\nA sua senha é: {senha}\n')


def caso2(valor):
    '''
    Gera uma senha mediana composta de números e letras
    :param valor: Quantidade de caracteres
    :return: Volta ao menu caso não seja possível gerar a senha
    '''
    import random
    import string
    caracteres = string.ascii_letters + string.digits
    if valor > len(caracteres):
        print("\033[31mNão é possível gerar uma senha com tantos caracteres sem repetição.\033[m")
        return
    senha = random.sample(caracteres, valor)
    senha = ''.join(senha)
    print(f'\nA sua senha é: {senha}\n')


def caso3(valor):
    '''
    Gera uma senha complexa
    :param valor: Quantidade de caracteres
    :return: Volta ao menu caso não seja possível gerar a senha
    '''
    import random
    import string
    caracteres = string.ascii_letters + string.digits + string.punctuation
    if valor > len(caracteres):
        print("\033[31mNão é possível gerar uma senha com tantos caracteres sem repetição.\033[m")
        return
    senha = random.sample(caracteres, valor)
    senha = ''.join(senha)
    print(f'\nA sua senha é: {senha}\n')

def opcoes(opc, n = 0):
    '''
    Verifica a opção escolhida e inicia a função
    :param opc: Opção escolhida
    :param n: Quantidade de digitos
    '''
    opcoes = {
        1: lambda: caso1(n),
        2: lambda: caso2(n),
        3: lambda: caso3(n),
        4: lambda: print('Saindo... Obrigado por usar nosso sistema!')
    }
    opcoes.get(opc, lambda: print('\033[31mOpção inválida!\033[m'))()