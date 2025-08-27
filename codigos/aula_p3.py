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


# Situação 2

def calcular_quantidade_gols(dados, pais):
    """
    dados contém dados estatísticos de futebol:
    - a terceira coluna traz o nome do país do jogador
    - a sexta coluna o nome da liga
    - a nona coluna o número de gols feitos pelo jogador
    pais é a identificação do país de interesse (ex.: "br BRA")

    A função calcula e retorna a quantidade de gols feitos 
    por jogadores do país passado em cada liga
    """
