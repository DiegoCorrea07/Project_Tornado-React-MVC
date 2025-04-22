
def calcular_promedio(notas):
    pesos = {1: 0.25, 2: 0.35, 3: 0.40}
    promedios_por_etapa = {}
    total_ponderado = 0.0

    notas_por_etapa = {}
    for nota in notas:
        etapa = nota['progress']
        if etapa not in notas_por_etapa:
            notas_por_etapa[etapa] = []
        notas_por_etapa[etapa].append(nota['grade'])

    for etapa, lista_notas in notas_por_etapa.items():
        if lista_notas:
            promedios_por_etapa[etapa] = sum(lista_notas) / len(lista_notas)
            if etapa in pesos:
                total_ponderado += promedios_por_etapa[etapa] * pesos[etapa]

    return round(total_ponderado, 2), promedios_por_etapa

def nota_necesaria_etapa3(promedio_etapa1, promedio_etapa2):
    nota_requerida = (6 - (promedio_etapa1 * 0.25 + promedio_etapa2 * 0.35)) / 0.4
    return round(nota_requerida, 2)