""" Modulo com as funções internas do jogo e que não fazem interação direta com o jogador """

from constantes import *
from random import randint 


def criaTab():

    """ Função respnsável por criar a matriz que será usada como tabuleiro """

    tabuleiro = []
    for i in range(TAMANHO_TABULEIRO):
        tabuleiro.append([])
        for j in range(TAMANHO_TABULEIRO):
            tabuleiro[i].append(0)


    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):

            if (i+j)%2 == 0:
                tabuleiro[i][j] = ESPACO_VAZIO
            
            elif (i+j)%2 == 1:
                if i <= LIMITE_PRETAS:
                    tabuleiro[i][j] = PECAS_PRETAS
                elif i >= LIMITE_BRANCAS:
                    tabuleiro[i][j] = PECAS_BRANCAS
                else:
                    tabuleiro[i][j] = ESPACO_VAZIO
    
    return tabuleiro



def inicia_partida():
       
    """ Esvolhe aleatoriamente que iniciará o jogo """

    dado = randint(0,1)
    if dado == 0:
        return JOG_1
    else:
        return JOG_2



def jogada_valida(x: int, y: int):

    """ função que verifica se a jogada indicada pelo usuario está dentro do tabuleiro """

    return 0 <= x < TAMANHO_TABULEIRO and 0 <= y < TAMANHO_TABULEIRO



def possui_peca(x: int, y: int, tabuleiro, t):

    """ funcção que verifica se existe peça no local inicial escolhido pelo jogador """

    if tabuleiro[x][y] == t:
        return True
    else:
        return False



def movimentos_possiveis(tab, x, y):
    movimentos = []

    """ funcção que cria uma lista com as possibilidades de movimento de uma peça,
        se a jogada escolhida estiver dentro da lista, a jogada será realizada"""
    
    
    if movimentos == []:
        linha = x 
        coluna = y


        if tab[linha][coluna] == PECAS_BRANCAS:

            if linha > 0:
                if coluna < 7:
                    if tab[linha-1][coluna+1] == ESPACO_VAZIO:
                        movimentos.append([linha-1, coluna+1])
            
                if coluna > 0:
                    if tab[linha-1][coluna-1] == ESPACO_VAZIO:
                        movimentos.append([linha-1, coluna-1])
        
        elif tab[linha][coluna] == PECAS_PRETAS:
            if linha < 7:
                if coluna < 7:
                    if tab[linha+1][coluna+1] == ESPACO_VAZIO:
                        movimentos.append([linha+1, coluna+1])
                
                if coluna > 0:
                    if tab[linha+1][coluna-1] == ESPACO_VAZIO:
                        movimentos.append([linha+1, coluna-1])

    return movimentos



def capturaDisponivel(tab, x, y):

    captura = []
    #captura = [peça capturada,posicção final da peça que capturou]
    """ modulo responsável por identificar uma peça inimiga proxima e verficar se pode ser capturada """

    if captura == []:
        linha = x 
        coluna = y

        if coluna >= 0 and coluna < TAMANHO_TABULEIRO:

            if tab[linha][coluna] == PECAS_BRANCAS:


                if linha < TAMANHO_TABULEIRO:
                    
                    if coluna < 6 and linha > 1:
                        if tab[linha-1][coluna+1] ==  PECAS_PRETAS:
                            if tab[linha-2][coluna+2] == ESPACO_VAZIO:
                                captura.append([linha-1, coluna+1, linha-2, coluna+2])
                
                    if coluna > 1 and linha > 1:
                        if tab[linha-1][coluna-1] == PECAS_PRETAS:
                            if tab[linha-2][coluna-2] == ESPACO_VAZIO:
                                captura.append([linha-1, coluna-1, linha-2, coluna-2])

                            """ realizar captura para trás """
                            
                    if coluna < 6 and linha < 6:
                        if tab[linha+1][coluna+1] == PECAS_PRETAS:
                            if tab[linha+2][coluna+2] == ESPACO_VAZIO:
                                captura.append([linha+1, coluna+1, linha+2, coluna+2])
                    
                    if coluna > 1 and linha < 6:
                        if tab[linha+1][coluna-1] == PECAS_PRETAS:
                            if tab[linha+2][coluna-2] == ESPACO_VAZIO:
                                captura.append([linha+1, coluna-1, linha+2, coluna-2])

            
            elif tab[linha][coluna] == PECAS_PRETAS:

                if linha >= 0:

                    if coluna < 6 and linha < 6:
                        if tab[linha+1][coluna+1] == PECAS_BRANCAS:
                            if tab[linha+2][coluna+2] == ESPACO_VAZIO:
                                captura.append([linha+1, coluna+1, linha+2, coluna+2])
                    
                    if coluna > 1 and linha < 6:
                        if tab[linha+1][coluna-1] == PECAS_BRANCAS:
                            if tab[linha+2][coluna-2] == ESPACO_VAZIO:
                                captura.append([linha+1, coluna-1, linha+2, coluna-2])
                    
                    """ realizar captura para trás """

                    if coluna < 6 and linha > 1:
                        if tab[linha-1][coluna+1] ==  PECAS_BRANCAS:
                            if tab[linha-2][coluna+2] == ESPACO_VAZIO:
                                captura.append([linha-1, coluna+1, linha-2, coluna+2])
                
                    if coluna > 1 and linha > 1:
                        if tab[linha-1][coluna-1] == PECAS_BRANCAS:
                            if tab[linha-2][coluna-2] == ESPACO_VAZIO:
                                captura.append([linha-1, coluna-1, linha-2, coluna-2])

    return captura



def capturar(x, y, tab, captura, op):

    """ modulo responsável por realizar a captura da peça inimiga, realizando as devidas substituiçoes na matriz que representa o tabuleiro e peças do jogo """

    linha_ini = x
    coluna_ini = y
    tp = tab[linha_ini][coluna_ini]

    linha_p_cap = captura[op][0]
    coluna_p_cap = captura[op][1]

    linha_final = captura[op][2]
    coluna_final = captura[op][3]

    tab[linha_final][coluna_final] = tp
    tab[linha_p_cap][coluna_p_cap] = ESPACO_VAZIO
    tab[linha_ini][coluna_ini] = ESPACO_VAZIO



def trocaTurno(t):

    """ realiza a troca do jogador conforme as rodadas se passam """

    if t == JOG_1:
        return JOG_2
    else:
        return JOG_1



def joga(tab, x, y, w, z):
    
    """ Função que realiza a jogada e mexe as peças no tabuleiro """

    linha_ini = x
    colu_ini = y
    temp = tab[linha_ini][colu_ini]
    
    tab[w][z] = temp
    tab[linha_ini][colu_ini] = ESPACO_VAZIO


p = 0
b = 0
def contaPecas(p, b, tab):

    """ função que calcula a quantidade de peças de cada jogador """

    for i in range(TAMANHO_TABULEIRO):

        qtd_p = tab[i].count(PECAS_PRETAS)
        p += qtd_p
        qtd_b = tab[i].count(PECAS_BRANCAS)
        b += qtd_b

    return p, b



def verificaVencedor(resultado):

    """ recebe a quantidade de peças e retorna o resultado da partida """

    if resultado[0] == 0:
        return JOG_1

    elif resultado[1] == 0:
        return JOG_2
    
    elif resultado[0] == 1 and resultado[1] == 1:
        return "Empate"


