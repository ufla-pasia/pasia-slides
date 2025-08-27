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
