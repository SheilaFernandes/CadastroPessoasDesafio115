from Cadastro import Colors
def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido \033[m')
            continue #ele retorna para o while
        else:
            return n

def Msg(msg):
    """
    >> Layout de Menu Principal
    :param msg: Texto de titulo do menu de funcionalidades
    :return: retorna a mensagem formata em caixa com texto centralizado
    """
    print('-'*50)
    print(msg.center(50))
    print('-'*50)

def Options(lista):
    Msg('Sistema de Cadastro')
    for posi, txt in enumerate(lista):
        Colors.color(f'{posi +1} -', 2, 0)
        Colors.colorstress(f'{txt}', 4)
    print('-'*50)
    opc = LeiaInt('Sua Opção: ')
    return opc




