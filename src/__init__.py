# src/__init__.py
"""
Módulo de métodos numéricos para el análisis de enfriamiento.
Contiene implementaciones de modelos, bisección, análisis y visualización.
"""

from .modelos import T_cuadratico, T_exponencial
from .biseccion import biseccion, encontrar_intervalo
from .analisis import analisis_sensibilidad, calcular_error_verdadero
from .visualizacion import graficar_resultados, graficar_comparacion

__all__ = [
    'T_cuadratico',
    'T_exponencial',
    'biseccion',
    'encontrar_intervalo',
    'analisis_sensibilidad',
    'calcular_error_verdadero',
    'graficar_resultados',
    'graficar_comparacion'
]