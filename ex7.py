from collections import Counter

def top_3_frequentes(lista):
    return [num for num, _ in Counter(lista).most_common(3)] # "_ é uma variavel descartavel"

numeros = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]
resultado = top_3_frequentes(numeros)

print(resultado)
