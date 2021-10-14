""" Modulo com as funções que possuem alguma interação com o jogador """

from constantes import *
from funcoes_tabu import *
from termcolor import colored

def printTabuleiro(tabuleiro):

    """Imprime o tabuleiro formatado com valores para as linhas e colunas """

    print("  | 0 1 2 3 4 5 6 7\n--+----------------")
    for i in range(TAMANHO_TABULEIRO):
        print(i,'|',end=' ')
        for j in range(TAMANHO_TABULEIRO):

            if j != TAMANHO_TABULEIRO-1:
                print(tabuleiro[i][j],end= " ")
            else:
                print(tabuleiro[i][j])
        
    return()



def verifica_formato(j):

    """ verifica se a entrada do jogador possui dois números """

    return j.isnumeric() and len(j) == 2



def recebe_jogada1(t):

    """ recebe a primeira coordenada que representa a peça que o jogador deseja mover """

    while True:
        print(colored("Jogador {}, é a sua vez!".format(t), "blue"))
        print(colored("Digite a peça que deseja mover no formato xy, onde x é a linha e y a coluna:", "blue"))
        jogada_ini = input()
        if verifica_formato(jogada_ini):
            break
        print(colored("Jogada fora do formato correto!\n", "red"))
        printTabuleiro(tab)
    
    return int(jogada_ini[0]), int(jogada_ini[1])



def recebe_jogada2():

    """ recebe a coordenada que representa o local onde o jogador deseja mover a peça escolhida na função anterior """

    while True:
        print(colored("Indique os valores xy correspondentes ao local que deseja colocar a peça!", "blue"))
        jogada_fim = input()
        if verifica_formato(jogada_fim):
            break
        print(colored("Jogada fora do formato correto!\n", "red"))

    return int(jogada_fim[0]), int(jogada_fim[1])



def texto_captura(captura):

    while True:
        if len(captura) > 1:

            print(colored("voce possui mais de uma captura disponivel. A seguinte lista mostra as capturas disponiveis, sendo que os dois primeiros valores de cada sub-lista representam a peça a ser capturada", "green"))
            print(colored(captura,"yellow"))
            op = int(input(colored("digite 0 para realizar a primeira opção de captura ou 1 para realizar a segunda possibilidade!\n", "yellow")))

            if op == 0 or op == 1:
                return op
            else:
                print(colored("por favor, digite as opções indicadas!\n", "red"))

        else:

            """ Quando o jogador seleciona uma peça que possui captura disponivel, essa função é chamada para avisar o jogador que existe captura disponivel """

            op = int(input(colored("voce possui uma captura disponivel. digite 0 para realizar a captura\n", "green")))
            if op == 0:
                return op
                
            else:
                print(colored("por favor, digite o número 0\n", "red"))



#laço principal

tab = criaTab()
t = inicia_partida()



while True:
    printTabuleiro(tab)

    try:

        #recebendo a posição da peça a ser movida
        x, y = recebe_jogada1(t)

        if jogada_valida(x, y): #verifica se as coordenadas estão dentro do tabuleiro

            podeCapturar = capturaDisponivel(tab, x, y) #verifiva se há possibilidade de captura para a peça escolhida

            if possui_peça(x, y, tab, t): #verifica se a posição escolhida possui peça

                if podeCapturar != []:

                    """ recebe a lista com possbilidade de captura e indica elas ao jogador """
                
                    catch = texto_captura(podeCapturar)
                    if catch == 0 or catch == 1:
                        capturar(x, y, tab, podeCapturar, catch)

                else:

                    """ caso não exista captura disponivel, simplesmente pede o lugar para onde mover a peça """

                    w, z = recebe_jogada2()

                    if jogada_valida(w, z):

                        """ dps de verificar se o movimento pode ser feito, realiza a jogada, conta as peças e verifiva se há um vencedor da partida """

                        if [w,z] in movimentos_possiveis(tab, x, y):
                            joga(tab, x, y, w, z)
                            placar = contaPeças(p,b,tab)
                            resultado = verificaVencedor(placar)

                            if resultado == JOG_1:
                                print(colored("Parabens, o jogador com as peças brancas venceu!", "green"))
                                break
                            elif resultado == JOG_2:
                                print(colored("Parabens, o jogador com as peças pretas venceu!", "green"))
                                break
                            elif resultado == "Empate":
                                print(colored("O jogo empatou!", "green"))
                                break

                            else:
                                t = trocaTurno(t)
                        else:
                            print(colored("Não é possivel realizar esse movimento. Tente novamente!\n", "yellow"))
                    
                    else:
                        print(colored("Jogada fora do tabuleiro, porfavor tente novamente\n", "red"))
                    
            else:
                print(colored("Escolha as coordenada que possuam uma peça!\n", "red"))

        else:
            print(colored("Jogada fora do tabuleiro, porfavor tente novamente\n", "red"))
    
    except ValueError:
        print(colored("Jogada inválida", "red"))

        
            
            


