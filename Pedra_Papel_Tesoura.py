import random
import os

lista_jogadas = ['papel', 'pedra', 'tesoura']

pontuacao_jogador = 0
pontuacao_computador = 0

print('========================')
print('Bem-vindo ao jogo Papel, Pedra e Tesoura')

def exibir_menu_principal():
    """
    Exibe o menu principal do jogo com o placar atual e solicita ao usu rio
    que escolha seu lance.

    Não recebe nenhum parametro e não retorna nada.
    """
    print('========================')
    print('\nPLACAR:')
    print('Você: {}'.format(pontuacao_jogador))
    print('Computador: {}'.format(pontuacao_computador))
    print('\n')
    print('Escolha seu lance:')
    print('0 - Papel | 1 - Pedra | 2 - Tesoura')

def selecionar_jogada_computador():
    """
    Seleciona uma jogada aleatória para o computador.

    A jogada é escolhida randomicamente dentre as opções 'papel', 'pedra' e
    'tesoura'.

    :return: jogada escolhida pelo computador
    :rtype: str
    """
    return random.choice(lista_jogadas)

def obter_jogada_jogador():
    """
    Solicita ao usuário que escolha seu lance e retorna a jogada como string.

    A escolha é feita por meio de uma entrada numérica (0, 1 ou 2) e a jogada é retornada
    como string ('papel', 'pedra' ou 'tesoura').

    Se a entrada for inválida (não for 0, 1 ou 2), o programa solicita novamente a entrada
    até que seja válida.

    :return: jogada escolhida pelo usuário
    :rtype: str
    """
    while True:
        try:
            jogada_jogador = int(input())
            if jogada_jogador not in [0, 1, 2]:
                raise ValueError("Escolha uma opção válida (0, 1 ou 2).")
            return lista_jogadas[jogada_jogador]
        except ValueError as e:
            print(e)
        except:
            print("Entrada inválida. Por favor, digite 0, 1 ou 2.")

def selecionar_vencedor(jogada_jogador, jogada_computador):
    """
    Seleciona o vencedor de uma rodada do jogo.

    A função recebe as jogadas do jogador e do computador e retorna um caractere que
    indica o vencedor da rodada. Os possíveis valores de retorno são:

    - 'p' : vitória do jogador
    - 'c' : vitória do computador
    - 'd' : empate

    A função também atualiza as pontuações do jogador e do computador.

    :param jogada_jogador: jogada escolhida pelo jogador
    :type jogada_jogador: str
    :param jogada_computador: jogada escolhida pelo computador
    :type jogada_computador: str
    :return: caractere que indica o vencedor da rodada
    :rtype: str
    """
    global pontuacao_jogador, pontuacao_computador

    if jogada_jogador == 'papel':
        if jogada_computador == 'tesoura':
            pontuacao_computador += 1
            return 'c'  
        elif jogada_computador == 'papel':
            return 'd' 
        elif jogada_computador == 'pedra':
            pontuacao_jogador += 1
            return 'p' 

    if jogada_jogador == 'tesoura':
        if jogada_computador == 'tesoura':
            return 'd'
        elif jogada_computador == 'papel':
            pontuacao_jogador += 1
            return 'p'
        elif jogada_computador == 'pedra':
            pontuacao_computador += 1
            return 'c'

    if jogada_jogador == 'pedra':
        if jogada_computador == 'tesoura':
            pontuacao_jogador += 1
            return 'p'
        elif jogada_computador == 'papel':
            pontuacao_computador += 1
            return 'c'
        elif jogada_computador == 'pedra':
            return 'd'

jogar_novamente = 1

while jogar_novamente == 1:
    exibir_menu_principal()

    jogada_jogador = obter_jogada_jogador()
    jogada_computador = selecionar_jogada_computador()
    vencedor = selecionar_vencedor(jogada_jogador, jogada_computador)

    print('')
    print('========================')
    print('Sua jogada: {}'.format(jogada_jogador.upper()))
    print('Jogada do computador: {}'.format(jogada_computador.upper()))

    if vencedor == 'p':
        print('Você venceu!')
    elif vencedor == 'c':
        print('Você perdeu!')
    else:
        print('Empate')

    print('========================')

    while True:
        try:
            print('Jogar novamente? 0 - Sim | 1 - Não')
            resposta = int(input())
            if resposta == 0:
                break 
            elif resposta == 1:
                jogar_novamente = 0
                break
        except:
            print("Opção inválida. Digite 0 para Sim ou 1 para Não.")
    
    os.system('cls' if os.name == 'nt' else 'clear')