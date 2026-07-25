# src/visualizacion.py
"""
Funciones de visualización para el proyecto.
"""

import numpy as np
import matplotlib.pyplot as plt
from .modelos import T_cuadratico, T_exponencial

def configurar_estilo_graficas():
    """
    Configura el estilo global de las gráficas.
    """
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 11
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3


def graficar_resultados(t, T, a, b, c, raiz, T_raiz, t_a, t_b, T_deseada, df_iter, tolerancia):
    """
    Genera las gráficas principales del proyecto.
    
    Parámetros:
    - t, T: datos experimentales
    - a, b, c: coeficientes del modelo cuadrático
    - raiz: raíz encontrada
    - T_raiz: temperatura en la raíz
    - t_a, t_b: intervalo inicial
    - T_deseada: temperatura objetivo
    - df_iter: DataFrame con las iteraciones
    - tolerancia: tolerancia utilizada
    
    Retorna:
    - Figura de matplotlib
    """
    configurar_estilo_graficas()
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    fig.suptitle('Análisis del Enfriamiento de la Bebida', fontsize=16, fontweight='bold')
    
    # Gráfica 1: Enfriamiento (Cuadrático)
    ax1 = axes[0, 0]
    t_suave = np.linspace(0, 50, 500)
    T_suave = T_cuadratico(t_suave, a, b, c)
    
    ax1.scatter(t, T, color='red', s=80, label='Datos experimentales', zorder=5)
    ax1.plot(t_suave, T_suave, 'b-', linewidth=2, label='Modelo cuadrático ajustado')
    ax1.axhline(y=T_deseada, color='green', linestyle='--', 
                linewidth=2, label=f'T_deseada = {T_deseada}°C')
    ax1.scatter(raiz, T_raiz, color='purple', s=200, 
                marker='*', label=f'Raíz: {raiz:.3f} min', zorder=10)
    
    ax1.set_xlabel('Tiempo (minutos)', fontsize=12)
    ax1.set_ylabel('Temperatura (°C)', fontsize=12)
    ax1.set_title('Enfriamiento de la Bebida (Modelo Cuadrático)', fontsize=13, fontweight='bold')
    ax1.legend(loc='best')
    ax1.set_xlim(-2, 50)
    ax1.set_ylim(20, 100)
    
    # Gráfica 2: Función f(t)
    ax2 = axes[0, 1]
    f_t = T_cuadratico(t_suave, a, b, c) - T_deseada
    
    ax2.plot(t_suave, f_t, 'r-', linewidth=2, label='f(t) = T(t) - 40')
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=1)
    ax2.axvline(x=raiz, color='purple', linestyle='--', 
                linewidth=2, label=f'Raíz: {raiz:.3f} min')
    ax2.fill_between([t_a, t_b], -20, 80, alpha=0.2, color='gray',
        label=f'Intervalo [{t_a:.1f}, {t_b:.1f}]')
    ax2.scatter(raiz, 0, color='purple', s=200, marker='*', zorder=10)
    
    ax2.set_xlabel('Tiempo (minutos)', fontsize=12)
    ax2.set_ylabel('f(t)', fontsize=12)
    ax2.set_title('Función a Resolver con Bisección', fontsize=13, fontweight='bold')
    ax2.legend(loc='best')
    ax2.set_xlim(-2, 50)
    ax2.set_ylim(-20, 60)
    
    # Gráfica 3: Convergencia del Error
    ax3 = axes[1, 0]
    iter_num = df_iter['Iteración'].values
    errores = df_iter['Error %'].values
    
    ax3.semilogy(iter_num, errores, 'bo-', linewidth=2, markersize=8)
    ax3.set_xlabel('Iteración', fontsize=12)
    ax3.set_ylabel('Error aproximado (%)', fontsize=12)
    ax3.set_title('Convergencia del Error', fontsize=13, fontweight='bold')
    ax3.axhline(y=tolerancia*100, color='red', linestyle='--', 
                linewidth=2, label=f'Tolerancia = {tolerancia*100:.4f}%')
    ax3.legend(loc='best')
    
    # Gráfica 4: Aproximación de la Raíz
    ax4 = axes[1, 1]
    valores_c = df_iter['c'].values
    
    ax4.plot(iter_num, valores_c, 'g-s', linewidth=2, markersize=8)
    ax4.axhline(y=raiz, color='red', linestyle='--', 
                linewidth=2, label=f'Raíz final: {raiz:.6f} min')
    ax4.set_xlabel('Iteración', fontsize=12)
    ax4.set_ylabel('Valor de c (tiempo en minutos)', fontsize=12)
    ax4.set_title('Aproximación de la Raíz', fontsize=13, fontweight='bold')
    ax4.legend(loc='best')
    
    plt.tight_layout()
    return fig


def graficar_comparacion(t, T, a, b, c, T0_exp, Ta_exp, k_exp, 
                        raiz, raiz_exp, T_raiz, T_raiz_exp, T_deseada):
    """
    Genera la gráfica comparativa entre modelos cuadrático y exponencial.
    
    Parámetros:
    - t, T: datos experimentales
    - a, b, c: coeficientes del modelo cuadrático
    - T0_exp, Ta_exp, k_exp: parámetros del modelo exponencial
    - raiz, raiz_exp: raíces de cada modelo
    - T_raiz, T_raiz_exp: temperaturas en las raíces
    - T_deseada: temperatura objetivo
    
    Retorna:
    - Figura de matplotlib
    """
    configurar_estilo_graficas()
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    
    t_suave = np.linspace(0, 60, 500)
    T_cuad = T_cuadratico(t_suave, a, b, c)
    T_exp = T_exponencial(t_suave, T0_exp, Ta_exp, k_exp)
    
    ax.scatter(t, T, color='red', s=80, label='Datos experimentales', zorder=5)
    ax.plot(t_suave, T_cuad, 'b-', linewidth=2, label='Modelo Cuadrático')
    ax.plot(t_suave, T_exp, 'orange', linewidth=2, label='Modelo Exponencial (Newton)')
    ax.axhline(y=T_deseada, color='green', linestyle='--', 
    linewidth=2, label=f'T_deseada = {T_deseada}°C')
    
    ax.scatter(raiz, T_raiz, color='blue', s=150, 
        marker='*', label=f'Cuadrático: {raiz:.2f} min', zorder=10)
    ax.scatter(raiz_exp, T_raiz_exp, color='orange', s=150, 
        marker='*', label=f'Exponencial: {raiz_exp:.2f} min', zorder=10)
    
    ax.set_xlabel('Tiempo (minutos)', fontsize=12)
    ax.set_ylabel('Temperatura (°C)', fontsize=12)
    ax.set_title('Comparación: Modelo Cuadrático vs Modelo Exponencial', 
                fontsize=14, fontweight='bold')
    ax.legend(loc='best')
    ax.set_xlim(-2, 60)
    ax.set_ylim(20, 100)
    
    plt.tight_layout()
    return fig