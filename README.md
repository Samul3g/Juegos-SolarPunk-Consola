# Juegos solarpunk de consola

Dos juegos de terminal en Python con temática solarpunk.

## Biblioteca solarpunk (`biblioteca_solarpunk_quiz.py`)

Juego de recorrido por los pisos de una biblioteca. En cada piso el jugador avanza por celdas y responde preguntas de selección única sobre energía renovable, ciudades sostenibles y otros temas solarpunk. Las preguntas cambian según el piso.

```
python biblioteca_solarpunk_quiz.py
```

La variable `cheats` al inicio del archivo está en `False`. Si se pone en `True`, el juego deja de revisar las respuestas del quiz, lo que sirve para probarlo rápido.

## Batalla naval contra los urbanitas (`batalla_naval_urbanitas.py`)

Versión de batalla naval con dos modos:

1. Barcos balleneros: el clásico, hundir los barcos en el tablero.
2. Solarpunk en lucha: turnos entre la guerrilla solarpunk, los urbanitas y la municipalidad, con construcción de edificios y puntos para cada bando.

Al iniciar se elige el modo y la proporción del tablero (16x9, 9x16, 4x3, 3x4 o 1x1).

```
python batalla_naval_urbanitas.py
```

## Requisitos

Python 3. No usa librerías externas.

## Contexto

Proyecto de un curso del TEC (Instituto Tecnológico de Costa Rica).

Autores: Samuel Ureña y Paula Monge

## Licencia

MIT
