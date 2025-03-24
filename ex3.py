def contagem_frequencia(texto):
    palavras = texto.split()  # Divide a string em palavras
    frequencia = {}
    for item in palavras:
        frequencia[item] = frequencia.get(item, 0) + 1
    return frequencia

linguagem = "Java Java Ruby Javascript Ruby"
resultado = contagem_frequencia(linguagem)

print(resultado)
