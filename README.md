# Pasos para el proyecto final
-** DSL**:  Lenguje de dominio especifico para un lenguaje de aprendizaje de máquina.

-Cosas que debe poder hacer el proyecto.

1. Operaciones aritméticas.
2. Operaciones de matrices.
3. Condicionales y ciclos for y while.
5. Gráficas de datos
6. Lectura, y escritura de archivos de texto.
7. Regresión Lineal.
8. Clasificador por medio de perceptron multicapa.
9. Algoritmos de agrupamiento (que es eso).

## Requisitos
- Instalar ANTLR4 y ANTLR4-python-runtime.

## Estructura
- La que tenemos sirve que sería:
	1. Main //Principal
	2. Parser //análisis léxico y sintactico
	3. Visitor //Operaciones
- Buscar como hacer esa gramática, e implementarle el numpy.

###Funciones para Machine Learning (ML)
- Visitor.py -> Operaciones con matrices
- Visit condicion -> Ciclos if/else, for, while
- Visit graficar -> Implmentar Matplotlib pyplot (buscar la gramática)
- Visit red neuronal -> Scikit-learn


### Crear el árbol principal
-Crear todos los objetos y crear la estructura para crear la consola.
- 
proyecto_dsl/
                ├── grammar/                   # Definir gramática

            │   └── MiLenguaje.g4          # Definición de gramática ANTLR4

            ├── src/                       # Código fuente

            │   ├── main.py                # Punto de entrada principal

            │   ├── parser.py              # Parsing del código fuente con ANTLR4

            │   ├── visitor.py             # Implementación del Visitor Pattern

            │   └── operations/            # Implementación de operaciones específicas

            │       ├── matrix.py          # Operaciones de matrices

            │       ├── arithmetic.py      # Operaciones aritméticas

            │       ├── regression.py      # Regresión lineal

            │       ├── classifier.py      # Clasificador multicapa

            │       └── clustering.py      # Algoritmo de agrupamiento

            └── README.md                  # Documentación del proyecto

**Mapeado extra a seguir** 
proyecto_lenguaje/
│
├── src/
│   ├── parser/
│   │   ├── grammar.g4           # Definición de la gramática ANTLR
│   │   ├── visitor.py            # Implementación del patrón Visitor
│   │   └── lexer.py              # Analizador léxico
│   │
│   ├── core/
│   │   ├── arithmetic.py         # Operaciones aritméticas
│   │   ├── matrix_operations.py  # Operaciones de matrices
│   │   └── file_handler.py       # Manejo de archivos
│   │
│   ├── ml/
│   │   ├── multilayer_perceptron.py  # Clasificador de perceptrón multicapa
│   │   └── clustering.py             # Algoritmos de agrupamiento
│   │
│   └── visualization/
│       └── data_plotter.py       # Graficación de datos
│
├── tests/
│   ├── test_arithmetic.py
│   ├── test_matrix.py
│   └── test_ml.py
│
├── requirements.txt
└── README.md

### Repo para guiarnos
[Natej](https://github.com/natej/dsl "Natej")
[DeepDSL](https://github.com/deepdsl/deepdsl "DeepDSL")

