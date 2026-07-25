# src/analisis.py
"""
Funciones de análisis para el proyecto.
"""

import numpy as np
import pandas as pd
from .biseccion import biseccion
from .modelos import f_cuadratico

def analisis_sensibilidad(funcion, a, b, tolerancias, max_iter=100):
    """
    Realiza un análisis de sensibilidad probando diferentes tolerancias.
    
    Parámetros:
    - funcion: función a resolver
    - a: extremo izquierdo del intervalo
    - b: extremo derecho del intervalo
    - tolerancias: lista de tolerancias a probar
    - max_iter: número máximo de iteraciones
    
    Retorna:
    - DataFrame con los resultados para cada tolerancia
    """
    resultados = []
    
    for tol in tolerancias:
        raiz, _, n_iter, _ = biseccion(funcion, a, b, tolerancia=tol, max_iter=max_iter)
        resultados.append({
            'Tolerancia': tol,
            'Tiempo (min)': raiz,
            'Iteraciones': n_iter
        })
    
    return pd.DataFrame(resultados)


def calcular_error_verdadero(numerico, exacto):
    """
    Calcula el error verdadero porcentual.
    
    Parámetros:
    - numerico: valor numérico aproximado
    - exacto: valor exacto de referencia
    
    Retorna:
    - Error verdadero en porcentaje
    """
    if exacto == 0:
        return np.nan
    return abs((numerico - exacto) / exacto) * 100


def calcular_error_aproximado(valor_actual, valor_anterior):
    """
    Calcula el error aproximado porcentual.
    
    Parámetros:
    - valor_actual: valor en la iteración actual
    - valor_anterior: valor en la iteración anterior
    
    Retorna:
    - Error aproximado en porcentaje
    """
    if valor_actual == 0:
        return 100.0
    return abs((valor_actual - valor_anterior) / valor_actual) * 100


def calcular_estadisticas_iteraciones(df_iter):
    """
    Calcula estadísticas básicas de las iteraciones.
    
    Parámetros:
    - df_iter: DataFrame con los datos de iteraciones
    
    Retorna:
    - Diccionario con estadísticas
    """
    return {
        'total_iteraciones': len(df_iter),
        'error_inicial': df_iter.iloc[0]['Error %'] if len(df_iter) > 0 else None,
        'error_final': df_iter.iloc[-1]['Error %'] if len(df_iter) > 0 else None,
        'valor_final_c': df_iter.iloc[-1]['c'] if len(df_iter) > 0 else None,
        'f_c_final': df_iter.iloc[-1]['f(c)'] if len(df_iter) > 0 else None,
        'intervalo_final': (df_iter.iloc[-1]['a'], df_iter.iloc[-1]['b']) if len(df_iter) > 0 else None
    }