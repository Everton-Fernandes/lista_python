def soma_pares(lista):
    soma = sum(i for i in lista if i % 2 == 0)
    return soma
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print( "A soma dos pares é: ", soma_pares(lista))