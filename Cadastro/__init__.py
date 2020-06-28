from Cadastro import Colors
def cadastro():
    """
    Realiza o cadastro por Nome e Idade. Sendo a idade deve ser digitada em número inteiro.
    :return: Mensagem informando que o Nome e Idade foram registrados
    """
    Dados = dict()
    listaDados = list()
    while True:
        try:
            Dados['nome'] = str(input('Nome: '))
        except (TypeError, ValueError):
            print(f'{Colors.color("ERRO! Digite um NOME válido:", 1)}')
            continue
        else:
            while True:
                try:
                    Dados['idade'] = int(input('Idade: '))
                except (TypeError, ValueError):
                    print(f'{Colors.color("ERRO! Digite um IDADE válido:", 1)}')
                    continue
                else:
                    print(f'Novo Registro de {Dados["nome"]} idade {Dados["idade"]} adicionado.')
                break
            break
    listaDados.append(Dados.copy())
    Dados.clear()


#def dataBase():
