def contagem_frequencia(lista):
    frequencia = {}
    for item in lista:
        frequencia[item] = frequencia.get(item, 0) + 1
    return frequencia

linguagem = ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby']
resultado = contagem_frequencia(linguagem)

print(resultado)
