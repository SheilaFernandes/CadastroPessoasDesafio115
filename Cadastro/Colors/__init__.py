def colorstress(txt, c=10, space= 1):
    '''
    >> Cores em negrito
    :param txt: texto a ser formatado
    :param c: campo opcional da cor a ser formatada, se não digitar nenhuma das cores abaixo será branco (10)
    1: Vermelho
    2: Verde
    3: amarelo
    4: Azul
    5: LILAS/ROXO
    6: Azul
    7: Cinza
    :param space: campo opcional, para definir ou nao a quebra de linha. Por padrão ele sempre quebra a linha.
    Digite qualquer número diferente de 1 para quebra de linha não seja feita.
    :return: retorna o texto devidamente formato com a cor escolhida em negrito.
    '''
    if space == 1:
        if c == 1:
            print(f'\033[1;31m{txt}\033[m')
        elif c == 2:
            print(f'\033[1;32m{txt}\033[m')
        elif c == 3:
            print(f'\033[1;33m{txt}\033[m')
        elif c == 4:
            print(f'\033[1;34m{txt}\033[m')
        elif c == 5:
            print(f'\033[1;35m{txt}\033[m')
        elif c == 6:
            print(f'\033[1;36m{txt}\033[m')
        elif c == 7:
            print(f'\033[1;37m{txt}\033[m')
        elif c == 10:
            print(f'\033[1m{txt}\033[m')
    else:
        if c == 1:
            print(f'\033[1;31m{txt}\033[m', end=' ')
        elif c ==2:
            print(f'\033[1;32m{txt}\033[m', end=' ')
        elif c == 3:
            print(f'\033[1;33m{txt}\033[m', end=' ')
        elif c == 4:
            print(f'\033[1;34m{txt}\033[m', end=' ')
        elif c == 5:
            print(f'\033[1;35m{txt}\033[m', end=' ')
        elif c == 6:
            print(f'\033[1;36m{txt}\033[m', end=' ')
        elif c == 7:
            print(f'\033[1;37m{txt}\033[m', end=' ')
        elif c == 10:
            print(f'\033[1m{txt}\033[m', end=' ')

def color(txt, c=10, space=1):
    """
        >> Cores em negrito
    :param txt: texto a ser formatado
    :param c:  campo opcional da cor a ser formatada, se não digitar nenhuma das cores abaixo será branco (10)
    1: Vermelho
    2: Verde
    3: amarelo
    4: Azul
    5: LILAS/ROXO
    6: Azul
    7: Cinza
    :param space: campo opcional, para definir ou nao a quebra de linha. Por padrão ele sempre quebra a linha.
    Digite qualquer número diferente de 1 para quebra de linha não seja feita.
    :return: retorna o texto devidamente formato com a cor escolhida em negrito.
    """
    if space == 1:
        if c == 1:
            print(f'\033[31m{txt}\033[m')
        elif c == 2:
            print(f'\033[32m{txt}\033[m')
        elif c == 3:
            print(f'\033[33m{txt}\033[m')
        elif c == 4:
            print(f'\033[34m{txt}\033[m')
        elif c == 5:
            print(f'\033[35m{txt}\033[m')
        elif c == 6:
            print(f'\033[36m{txt}\033[m')
        elif c == 7:
            print(f'\033[37m{txt}\033[m')
        elif c == 10:
            print(f'\033[m{txt}\033[m')
    else:
        if c == 1:
            print(f'\033[31m{txt}\033[m', end=' ')
        elif c == 2:
            print(f'\033[32m{txt}\033[m', end=' ')
        elif c == 3:
            print(f'\033[33m{txt}\033[m', end=' ')
        elif c == 4:
            print(f'\033[34m{txt}\033[m', end=' ')
        elif c == 5:
            print(f'\033[35m{txt}\033[m', end=' ')
        elif c == 6:
            print(f'\033[36m{txt}\033[m', end=' ')
        elif c == 7:
            print(f'\033[37m{txt}\033[m', end=' ')
        elif c == 10:
            print(f'\033[m{txt}\033[m', end=' ')
