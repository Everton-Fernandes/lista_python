def ordenar_tupla(tupla):
    lista = list(tupla)
    lista.sort()
    return tuple(lista)

nomes = ["Samuel", "Karynne", "Carol", "Kleber", "Vinicius"]

resultado = ordenar_tupla(nomes)

print(resultado)