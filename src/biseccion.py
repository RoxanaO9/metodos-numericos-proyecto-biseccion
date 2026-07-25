# src/biseccion.py
"""
Implementación del método de bisección para encontrar raíces.
"""

import numpy as np
import pandas as pd

def encontrar_intervalo(funcion, t_min=0, t_max=50, paso=0.5):
    """
    Busca un intervalo [a, b] donde la función cambie de signo.
    
    Parámetros:
    - funcion: función a evaluar
    - t_min: tiempo mínimo de búsqueda
    - t_max: tiempo máximo de búsqueda
    - paso: tamaño del paso de búsqueda
    
    Retorna:
    - (a, b): intervalo donde hay cambio de signo, o (None, None) si no se encuentra
    """
    for i in np.arange(t_min, t_max, paso):
        if funcion(i) * funcion(i + paso) < 0:
            return i, i + paso
    
    return None, None


def biseccion(funcion, a, b, tolerancia=1e-6, max_iter=100, verbose=False):
    """
    Implementación del método de bisección para encontrar raíces.
    
    Parámetros:
    - funcion: función a evaluar
    - a: extremo izquierdo del intervalo
    - b: extremo derecho del intervalo
    - tolerancia: precisión deseada
    - max_iter: número máximo de iteraciones
    - verbose: si es True, imprime información durante la ejecución
    
    Retorna:
    - raiz: valor aproximado de la raíz
    - tabla: DataFrame con los datos de cada iteración
    - iteraciones: número de iteraciones realizadas
    - mensaje: mensaje de estado de la convergencia
    """
    # Verificar que el intervalo cumpla el Teorema de Bolzano
    if funcion(a) * funcion(b) >= 0:
        raise ValueError("El intervalo no cumple la condición del Teorema de Bolzano")
    
    # Inicializar variables
    tabla = []
    c_anterior = None
    iteracion = 0
    mensaje = ""
    
    if verbose:
        print("Ejecutando método de bisección...")
        print(f"Intervalo inicial: [{a:.4f}, {b:.4f}]")
        print(f"Tolerancia: {tolerancia}")
    
    while iteracion < max_iter:
        # Calcular punto medio
        c = (a + b) / 2
        fc = funcion(c)
        
        # Calcular error aproximado
        if c_anterior is None:
            error_aprox = 100.0
        else:
            error_aprox = abs((c - c_anterior) / c) * 100
        
        # Guardar datos de la iteración
        tabla.append({
            'Iteración': iteracion + 1,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': fc,
            'Error %': error_aprox
        })
        
        # Verificar condición de parada
        if abs(fc) < tolerancia or (b - a) / 2 < tolerancia:
            mensaje = f"Convergencia alcanzada en {iteracion + 1} iteraciones"
            if verbose:
                print(mensaje)
            break
        
        # Actualizar intervalo
        if funcion(a) * fc < 0:
            b = c
        else:
            a = c
        
        c_anterior = c
        iteracion += 1
    
    # Si no se alcanzó la convergencia
    if iteracion >= max_iter and abs(fc) >= tolerancia and (b - a) / 2 >= tolerancia:
        mensaje = f"Se alcanzó el máximo de iteraciones ({max_iter})"
        if verbose:
            print(mensaje)
    
    # Calcular la raíz aproximada
    raiz = (a + b) / 2
    
    # Crear DataFrame con los resultados
    df_iter = pd.DataFrame(tabla)
    
    return raiz, df_iter, len(tabla), mensaje