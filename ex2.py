def ordenar_por_idade(lista):
    return sorted(lista, key=lambda pessoa: pessoa[1])

# Exemplo de uso
pessoas = [("Samuel", 25), ("Karynne", 22), ("Carol", 20), ("Kleber", 23), ("Vinicius", 27)]
resultado = ordenar_por_idade(pessoas)

print(resultado)
