def palindromo(palavra):
    return palavra == palavra[::-1]  # [::-1] inverte a string

entrada = "radar"
entrada1 = "reviver"
resultado = palindromo(entrada)
resultado1 = palindromo(entrada1)

print(resultado,"e", resultado1)
