def contagem_palavras(texto):
    palavras = texto.split()  # Divide a string em palavras
    frequencia = {}
    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1
    return frequencia

texto = "banana maçã banana laranja maçã maçã"
resultado = contagem_palavras(texto)

print(resultado)
