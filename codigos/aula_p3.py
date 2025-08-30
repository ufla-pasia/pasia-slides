# meu_app/main.py

def maior_palavra(palavras):
    if not palavras:
        return None
    maior = palavras[0]
    for p in palavras[1:]:
        if len(p) > len(maior):
            maior = p
    return maior

# testes/test_maior_palavra.py

from meu_app.main import maior_palavra

def test_maior_palavra_unica():
    assert maior_palavra(['gato', 'pássaro', 'cachorro']) == 'cachorro'

def test_maior_palavra_unica_lista_maior():
    assert maior_palavra(['feliz', 'aniversário', 'para', 'meu', 'cachorro']) == 'aniversário'

def test_maior_palavra_lista_1_elemento():
    assert maior_palavra(['feliz']) == 'feliz'

def test_maior_palavra_empate():
    assert maior_palavra(['gato', 'cão', 'sapo']) == 'gato'

def test_maior_palavra_strings_vazias():
    assert maior_palavra(['', '', '']) == ''

def test_maior_palavra_lista_vazia():
    assert maior_palavra([]) is None


# Situação 1

# Prompt usado no Gemini

# Crie o código da função abaixo:

def fileira_mais_livre(fileiras, tamanho_grupo):
    """
    fileiras é uma matriz (lista de listas) de booleanos representando as fileiras de uma sala de cinema.
    A primeira lista é a primeira fileira e assim por diante. 
    Um valor True indica que o assento da fileira está ocupado e False que está livre.

    tamanho_grupo é a quantidade de pessoas que gostaria de sentar lado a lado (na mesma fileira) na sala de cinema.

    A função retorna a fileira com a maior quantidade de assentos livres consecutivos, se essa quantidade for 
    maior ou igual o tamanho do grupo. A primeira fileira é identificada com 0, a segunda com 1, assim por diante.

    Se nenhuma fileira tiver uma quantidade de assentos livres maior ou igual ao tamanho do grupo, a função retorna -1.

    Se houver empate, ou seja, se mais de uma fileira tiver igual quantidade máxima de assentos livres, 
    deve ser retornada a última fileira da matriz.
    """
    max_consecutivos = -1
    fileira_selecionada = -1

    for i, fileira in enumerate(fileiras):
        consecutivos_atuais = 0
        maior_consecutivos_na_fileira = 0
        
        for assento in fileira:
            if not assento:  # Se o assento estiver livre (False)
                consecutivos_atuais += 1
            else:  # Se o assento estiver ocupado (True)
                consecutivos_atuais = 0
            
            if consecutivos_atuais > maior_consecutivos_na_fileira:
                maior_consecutivos_na_fileira = consecutivos_atuais
        
        if maior_consecutivos_na_fileira >= tamanho_grupo:
            if maior_consecutivos_na_fileira >= max_consecutivos:
                max_consecutivos = maior_consecutivos_na_fileira
                fileira_selecionada = i
                
    return fileira_selecionada

# Situação 2

def calcular_quantidade_gols(dados, pais):
    """
    dados contém dados estatísticos de futebol:
    - a terceira coluna traz o nome do país do jogador
    - a sexta coluna o nome da liga
    - a décima terceira coluna o número de gols feitos pelo jogador
    pais é a identificação do país de interesse (ex.: "br BRA")

    A função calcula e retorna a quantidade de gols feitos 
    por jogadores do país passado em cada liga
    """
