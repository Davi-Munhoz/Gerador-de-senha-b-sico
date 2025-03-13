import estilizacao
import uteis
from time import sleep

while True:
    estilizacao.cabecalho('GERADOR DE SENHAS')
    estilizacao.menu()
    opc = uteis.verificaInt('R: ')
    estilizacao.linha()

    if opc == 4:
        uteis.opcoes(opc)
        break
    elif opc > 4 or opc < 0:
        uteis.opcoes(opc)
    else:
        escolha = uteis.verificaInt('Quantos digitos terá a senha: ')
        estilizacao.linha()
        sleep(1)
        uteis.opcoes(opc, escolha)