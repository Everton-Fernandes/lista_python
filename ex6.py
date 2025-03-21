def combinar_dicionarios(d1, d2):
    resultado = d1.copy()  # Copia d1 para não modificar o original
    for chave, valor in d2.items():
        resultado[chave] = resultado.get(chave, 0) + valor
    return resultado

d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}
resultado = combinar_dicionarios(d1, d2)

print(resultado)