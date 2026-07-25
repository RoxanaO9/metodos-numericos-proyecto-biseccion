# src/modelos.py
"""
Definición de los modelos matemáticos para el enfriamiento.
"""

import numpy as np

def T_cuadratico(t, a, b, c):
    """
    Función cuadrática para modelar el enfriamiento.
    
    Parámetros:
    - t: tiempo (minutos) o array de tiempos
    - a, b, c: coeficientes del polinomio
    
    Retorna:
    - Temperatura en el tiempo t
    """
    return a * t**2 + b * t + c


def T_exponencial(t, T0, Ta, k):
    """
    Modelo de enfriamiento exponencial (Ley de Newton)
    T(t) = Ta + (T0 - Ta) * exp(-k*t)
    
    Parámetros:
    - t: tiempo (minutos) o array de tiempos
    - T0: temperatura inicial
    - Ta: temperatura ambiente
    - k: constante de enfriamiento
    
    Retorna:
    - Temperatura en el tiempo t según la Ley de Newton
    """
    return Ta + (T0 - Ta) * np.exp(-k * t)


def f_cuadratico(t, a, b, c, T_deseada):
    """
    Función a resolver con el método de bisección para el modelo cuadrático.
    f(t) = T_cuadratico(t) - T_deseada = 0
    
    Parámetros:
    - t: tiempo (minutos)
    - a, b, c: coeficientes del polinomio
    - T_deseada: temperatura objetivo
    
    Retorna:
    - Diferencia entre la temperatura modelada y la deseada
    """
    return T_cuadratico(t, a, b, c) - T_deseada


def f_exponencial(t, T0, Ta, k, T_deseada):
    """
    Función a resolver con el método de bisección para el modelo exponencial.
    f(t) = T_exponencial(t) - T_deseada = 0
    
    Parámetros:
    - t: tiempo (minutos)
    - T0: temperatura inicial
    - Ta: temperatura ambiente
    - k: constante de enfriamiento
    - T_deseada: temperatura objetivo
    
    Retorna:
    - Diferencia entre la temperatura modelada y la deseada
    """
    return T_exponencial(t, T0, Ta, k) - T_deseada


def solucion_analitica_cuadratico(a, b, c, T_deseada, t_a=None, t_b=None):
    """
    Calcula la solución analítica de la ecuación cuadrática.
    f(t) = a*t² + b*t + (c - T_deseada) = 0
    
    Parámetros:
    - a, b, c: coeficientes del polinomio
    - T_deseada: temperatura objetivo
    - t_a, t_b: intervalo de búsqueda (opcional)
    
    Retorna:
    - Raíz positiva dentro del intervalo especificado, o None si no existe
    """
    discriminante = b**2 - 4 * a * (c - T_deseada)
    
    if discriminante < 0:
        return None
    
    raiz1 = (-b + np.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - np.sqrt(discriminante)) / (2 * a)
    
    if t_a is not None and t_b is not None:
        if t_a <= raiz1 <= t_b:
            return raiz1
        elif t_a <= raiz2 <= t_b:
            return raiz2
        return None
    
    # Si no se especifica intervalo, devolver la raíz positiva
    if raiz1 >= 0:
        return raiz1
    elif raiz2 >= 0:
        return raiz2
    return None