#  Método de Bisección para Enfriamiento de una Bebida

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

##  Descripción

Este proyecto aplica el **método de bisección** para calcular el tiempo de enfriamiento de una bebida caliente utilizando un **modelo cuadrático** ajustado a datos experimentales. El proyecto incluye:

-  Ajuste de modelo cuadrático por mínimos cuadrados
-  Implementación del método de bisección
-  Análisis de sensibilidad con diferentes tolerancias
-  Comparación con el modelo exponencial (Ley de Newton)
-  Visualizaciones profesionales con Matplotlib

##  Objetivo

Determinar el tiempo necesario para que una bebida caliente alcance una temperatura de **40°C** a partir de datos experimentales de temperatura vs tiempo.

##  Resultados Principales

| Métrica | Valor |
|---------|-------|
| **Tiempo encontrado** | 32.474007 minutos (32 min 28 seg) |
| **Modelo** | T(t) = 0.036429t² - 2.882143t + 95.178571 |
| **R²** | 0.999897 |
| **Iteraciones** | 16 |
| **Error verdadero** | 0.000001% |

##  Tecnologías Utilizadas

- **Python 3.13** - Lenguaje de programación
- **Jupyter Notebook** - Entorno interactivo
- **NumPy** - Cálculos numéricos
- **Pandas** - Manipulación de datos
- **Matplotlib** - Visualización de datos
- **SciPy** - Ajuste de curvas (curve_fit)

## 📁 Estructura del Proyecto
metodos-numericos-biseccion-enfriamiento/\
│
├── README.md # Descripción del proyecto\
├── requirements.txt # Dependencias\
├── 📁 notebooks/ # Cuadernos Jupyter\
├── 📁 src/ # Código fuente\
├── 📁 data/ # Datos experimentales\
├── 📁 results/ # Resultados generados\
└── 📁 docs/ # Documentación\

