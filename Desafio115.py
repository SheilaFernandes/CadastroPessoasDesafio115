from Cadastro import Menu
from Cadastro import Colors
from Cadastro import Arquivo
from time import sleep
arq = 'dataBase.txt'
if not Arquivo.arquivoExiste(arq):
    #print('Arquivo encontrado com sucesso')
#else:
   #print('Arquivo não encontrado!')
    Arquivo.criarArquivo(arq)

while True:
    sleep(2)
    resposta = Menu.Options(['Ver Pessoas Cadastradas', 'Cadastrar pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteudo do arquivo
        Arquivo.lerArquivo(arq)
    elif resposta == 2:
        Menu.Msg('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = Menu.LeiaInt('Idade: ')
        Arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        Colors.color('Saindo do Sistema!', 3)
        sleep(0.5)
        Colors.colorstress('Até mais! Volte Sempre!!!', 5)
        break
    else:
        Colors.colorstress('ERRO! Digite uma opção válida.', 1)

