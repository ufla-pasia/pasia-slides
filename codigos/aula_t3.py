def numero_de_pontos(palavra):
    """
    Cada letra na palavra vale os seguintes pontos:
    a, e, i, o, u, m, s, r, t: 1 ponto
    d, l, c, p: 2 pontos
    n, b, ç: 3 pontos
    f, g, h, v: 4 pontos
    j: 5 pontos
    q: 6 pontos
    x, z: 8 pontos

    palavra é uma palavra formada por letras caracteres minúsculos
    Retorna a soma dos pontos de cada letra da palavra
    """
    pontos = 0
    for letra in palavra:
        if letra in "aeioumsrt":
            pontos += 1
        elif letra in "dlcp":
            pontos += 2
        elif letra in "nbç":
            pontos += 3
        elif letra in "fghv":
            pontos += 4
        elif letra == "j":
            pontos += 5
        elif letra == "q":
            pontos += 6
        elif letra in "xz":
            pontos += 8
    return pontos

def melhor_palavra(palavras):
    """
    palavras é uma lista de palavras.

    Retorna a palavra com a maior pontuação.
    """
    melhor = palavras[0]
    max_pontos = numero_de_pontos(melhor)

    for palavra in palavras[1:]:
        pontos = numero_de_pontos(palavra)
        if pontos > max_pontos:
            melhor = palavra
            max_pontos = pontos

    return melhor



def clean_number(phone_number):
    phone_number = phone_number.replace("(", "")
    phone_number = phone_number.replace(")", "")
    phone_number = phone_number.replace("-", "")
    phone_number = phone_number.replace(" ", "")
    return phone_number

