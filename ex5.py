def calcular_medias(alunos):
    return [
        (nome, round(sum(notas) / len(notas), 2)) # round para arredondar a média para 2 casas decimais
        for nome, notas in alunos.items()
        ]

alunos = {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10], "Daniel": [10, 10, 10]}
resultado = calcular_medias(alunos)

print(resultado)
