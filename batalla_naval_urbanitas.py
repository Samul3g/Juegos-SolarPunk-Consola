
import random
from time import sleep

vidas = 20
turnos = 5
puntos_solarpunk = 0
puntos_urbanitas = 0

barcos_sprites = [
[
    "   .Y-\\       ",
    "  |.,'        ",
    "Y---'`..Y-''''",
    "  _           ",
    " /'`\\   __    ",
    " \\_,/ ,'''\\   ",
    "''''-''   ''--",
    "              ",
]
,
[
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ "
]
,
[
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║══════════║ ",
    "              "
]
,
[
    "              ",
    " ║══════════║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ "
]
,   
[
    "              ",
    "══════════════",
    "              ",
    "              ",
    "              ",
    "              ",
    "══════════════",
    "              "
]
,    
[
    "              ",
    "════════════║ ",
    "            ║ ",
    "            ║ ",
    "            ║ ",
    "            ║ ",
    "════════════║ ",
    "                "
]
,    
[
    "              ",
    " ║════════════",
    " ║            ",
    " ║            ",
    " ║            ",
    " ║            ",
    " ║════════════",
    "              "
]
,
[
    "              ",
    " ║══════════║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║          ║ ",
    " ║══════════║ ",
    "              "
]
,
[
    "    \\      /  ",
    "     \\    /   ",
    "      \\  /    ",
    "       \\/     ",
    "       /\\     ",
    "      /  \\    ",
    "     /    \\   ",
    "    /      \\  "
]
]

edificios = [
[
    '',
    '┌───────┐',
    '│       │',
    '│       │',
    '│       │',
    '│       │',
    '│       │',
    '│       │',
    '│       │',
    '│       │',
    '│       │',
    '│       │',
    '│       │',
    '│       │',
    '│       │',
    '└───────┘',
    '',     
]
,
[
    '',
    '│   │   │',
    '│       │',
    '│   │   │',
    '│   │   │',
    '│       │',
    '│   │   │',
    '│   │   │',
    '│       │',
    '│   │   │',
    '│   │   │',
    '│       │',
    '│   │   │',
    '│   │   │',
    '│       │',
    '│   │   │',
    '',
]
,
[
    '',
    '┌───────┐',
    '│─ ─ ─ ─│',
    '│       │',
    '│ CLUB  │',
    '│PRIVADO│',
    '│       │',
    '│       │',
    '│ (...) │',
    '│  |||  │',
    '│  |||  │',
    '│  |||  │',
    '│  |||  │',
    '│ (___) │',
    '│       │',
    '└───────┘',
    '',
]
,
[
    '',
    '┌───────┐',
    '│   .-,.│',
    "│   |.,'│",
    "│   /'| │",
    '│   | | │',
    '│Fábrica│',
    '│  ,>Y| │',
    '│ ,).\\| │',
    '│ >,|  |│',
    "│ |Y .')│",
    '│/\\/    │',
    '│|||||||│',
    '│| | | |│',
    '│| | | |│',
    '└───────┘',
    '',
]
,
[
    '',
    ' │  │  │ ',
    '         ',
    ' │  │  │ ',
    '         ',
    ' │  │  │ ',
    '         ',
    ' │  │  │ ',
    '         ',
    ' │  │  │ ',
    '         ',
    ' │  │  │ ',
    '         ',
    ' │  │  │ ',
    '         ',
    ' │  │  │ ',
    '',
]
,   
[
    '',
    '┌─────(  ',
    '│    ( ` ',
    '│   (_(_.',
    '│Granjas│',
    '│Comuni-│',
    '│tarias │',
    '│       │',
    '│       │',
    '│       │',
    '(__)  //│',
    '(oo) //\\ ',
    '-\\ ////\\ ',
    '||   ][ │',
    "\\\\  _('<│",
    ' \\ ___)─┘',
    '',
]
,    
[
    '',
    '┌───────┐',
    '│ \\./   │',
    '│─(+)-- │',
    "│ /'\\   │",
    '│/   \\  │',
    '│ Parque│',
    '│  ,-.  │',
    '\\ (   ) │',
    "\\  `-'  │",
    '/\\    /\\ ',
    '/\\   //\\ ',
    '/\\ \\ //\\ ',
    '/\\ \\ //\\ ',
    '/\\\\  //\\ ',
    '][───  ][',
    '',
]
,    
[
    '',
    '│   │   │',
    '│       │',
    '│   │    ',
    '│   │   │',
    '│       │',
    '│   │    ',
    '│   │   │',
    '│       │',
    '│   │    ',
    '│   │   │',
    '│       │',
    '│   │    ',
    '│   │   │',
    '│       │',
    '│   │    ',
    '',
]
,
[
    '',
    '┌───────┐',
    '│ Verde-│',
    '│ Soste-│',
    '│ nible │',
    '│       │',
    '│       │',
    ' /\\   //│',
    '//\\ \\ ///',
    '//\\ \\ ///',
    '│][─  ][ ',
    '│║┌|.|┐║│',
    "│║└/.'|║│",
    "│║┌|'|`║│",
    "│║└' '┘║│",
    '│║┌┐ ┌┐║│',
    '',
]
,
[
    '',
    '┌───────┐',
    '│Terceros',
    '│Espacios',
    '│      ,~',
    '│     (  ',
    "│    ( ` ",
    '│  (_(_.~',
    '\\ |/    │',
    '/|\\     │',
    ' | \\    │',
    '/ \\ _\\  │',
    '│   __o │',
    '│ _ \\ <_│',
    '│(_)/(_)│',
    '└───────┘',
    '',
]
]

def generar_tablero(proporción):
    '''Función que genera un tablero con diferentes márgenes
    E: Int entre 1 y 5
    S: Un tablero vacio 
    R: Int entre 1 y 5'''
    
    if type(proporción) != int:
        return "Error01"
    if proporción < 1 or proporción > 5:
        return "Error02"

    tablero = []
    if proporción == 1:
        tablero = generar_tablero_aux(16,9)
    if proporción == 2:
        tablero = generar_tablero_aux(9,16)
    if proporción == 3:
        tablero = generar_tablero_aux(4*2,3*2)
    if proporción == 4:
        tablero = generar_tablero_aux(3*2,4*2)
    if proporción == 5:
        tablero = generar_tablero_aux(1*5,1*5)
    return tablero

def generar_tablero_aux(proporción_filas, proporción_columnas):
    '''Auxiliar'''
    i = 0
    tablero = []
    
    while i < proporción_filas:
        tablero_columnas = []
        i2 = 0
        
        while i2 < proporción_columnas:
            tablero_columnas += [0]
            i2 += 1
        i += 1
        tablero += [tablero_columnas]
        
    return tablero

def es_num(num):
    """
    Función que comprueba que un valor sea entero
    E: valor str
    S: valida que ese valor sea numero
    R: que sea str
    """
    
    if type(num) != str:
        return "Error01"
        
    i = 0 
    
    while i < 10:
    
        if num == str(i):
            return True
            
        i += 1
        
    return False

def probar_mas(argumento):
    """Función que prueba argurmento
    E: argumento
    S: impresion"""
    
    if type(argumento) != list:
        print(argumento)
    else: 
        for fila in argumento:
            for mas in fila:
                print(mas)
        print("")

def probar(argumento):
    """Función que prueba argurmento
    E: argumento
    S: impresion"""

    if type(argumento) != list:
        print(argumento)
    else: 
        for fila in argumento:
            print(fila)
        print("")

def copiar_lista(lista_original):
    """
    Función que copia un lista
    E: lista
    S: lista copiada
    """
    copia_maestra = []
    i = 0
    
    while i < len(lista_original):
        sublista_original = lista_original[i]
        nueva_sublista = []
        j = 0
        
        while j < len(sublista_original):
            elemento = sublista_original[j]
            nueva_sublista += [elemento]
            j += 1
        copia_maestra += [nueva_sublista]
        i += 1
        
    return copia_maestra

def esta_lista(elem, lista):
    """Función que determina si un elemento está en una lista
    E: elem y lista
    S: true or false"""
    
    for elemntos in lista:
        if elemntos == elem:
            return True
    return False

def parsear_casilla(entrada):
    """Función que persea casilla
    E: entrada a parsear
    S: entrada parseada"""
    
    if type(entrada) != str:
        return "Error01"
    if es_num(entrada) != True:
        return "Error02"
    entrada = int(entrada)
    if entrada < 1:
        return "Error03"
    entrada -= 1 
    return entrada

#########################################################################
#                                                                       #
#                           LOGICA JUEGO 1                              #
#                                                                       #
#########################################################################

def generar_barcos(tablero):
    '''S: Genera los barcos del tablero
    E: proporción del tablero
    R: Int entre 1 y 5'''
    
    if type(proporción) != int:
        return "Error01"
    if proporción < 1 or proporción > 5:
        return "Error02"

    i = 0
    while i < 5:
        barco_generar = random.randint(0,2)
        barco_generar = longitud_barco(barco_generar)
        direccion_barco = random.randint(0,1)

        if direccion_barco == 0:
            tablero_con_barco = generar_1_barco_eje_y(barco_generar, tablero)
        else:
            tablero_con_barco = generar_1_barco_eje_x(barco_generar, tablero)

        if tablero_con_barco != False:
            i += 1
            tablero = tablero_con_barco
    return tablero

def longitud_barco(barco_int):
    '''En base a un numero random devuelve la longitud de un barco
    E: Int entre 0 y cantidad de barcos
    S: Barco a generar
    R: Int entre 0 y 2]'''
    
    if type(barco_int) != int:
        return "Error01"
        
    if barco_int < 0 or barco_int > 2:
        return "Error02"
    if barco_int == 0:
        return 1
    if barco_int == 1:
        return 3
    if barco_int == 2:
        return 5

def generar_1_barco_eje_y(longitud, tablero):
    """Función que genera un barco en eje y
    E: largo y posicion en el tablero
    S: barco ubicado en el tablero"""
    
    posición_valida = False
    barco_abajo = False
    barco_arriba = False
    tablero_testeo = copiar_lista(tablero)
    largo_y = len(tablero) - 1
    largo_x = len(tablero[0]) - 1

    while posición_valida != True:
        posición_inicial_x = random.randint(0, largo_x)
        posición_inicial_y = random.randint(0, largo_y)
        if tablero[posición_inicial_y][posición_inicial_x] != 0:
            posición_valida = False
        else:
            posición_valida = True

    tablero_testeo[posición_inicial_y][posición_inicial_x] = 1 
    i = 1
    total_generado = 1

    while barco_abajo != True:
        if posición_inicial_y + i > largo_y or tablero[posición_inicial_y + i][posición_inicial_x] != 0: 
            tablero_testeo[posición_inicial_y + i - 1][posición_inicial_x] = 2
            barco_abajo = True
        elif total_generado == longitud:
            tablero_testeo[posición_inicial_y + i - 1][posición_inicial_x] = 2
            barco_abajo = True
        else:
            tablero_testeo[posición_inicial_y + i][posición_inicial_x] = 1
            total_generado += 1
        i += 1

    i = 1
    while barco_arriba != True:
        if posición_inicial_y - i < 0 or tablero[posición_inicial_y - i][posición_inicial_x] != 0: 
            tablero_testeo[posición_inicial_y - i + 1][posición_inicial_x] = 3
            barco_arriba = True
        elif total_generado == longitud:
            tablero_testeo[posición_inicial_y - i + 1][posición_inicial_x] = 3
            barco_arriba = True
        else:
            tablero_testeo[posición_inicial_y - i][posición_inicial_x] = 1
            total_generado += 1
        i += 1
        
    if total_generado == 1:
        tablero_testeo[posición_inicial_y][posición_inicial_x] = 7
        
    if total_generado < longitud:
        return False
    else:
        return tablero_testeo

def generar_1_barco_eje_x(longitud, tablero):
    """Función que genera un barco en eje x
    E: largo y posicion en el tablero
    S: barco ubicado en el tablero"""
    posición_valida = False
    barco_derecha = False
    barco_izquierda = False
    tablero_testeo = copiar_lista(tablero)
    largo_y = len(tablero) - 1
    largo_x = len(tablero[0]) - 1

    while posición_valida != True:
        posición_inicial_x = random.randint(0, largo_x)
        posición_inicial_y = random.randint(0, largo_y)
        if tablero[posición_inicial_y][posición_inicial_x] != 0:
            posición_valida = False
        else:
            posición_valida = True

    tablero_testeo[posición_inicial_y][posición_inicial_x] = 4 
    i = 1
    total_generado = 1

    while barco_derecha != True:
        if posición_inicial_x + i > largo_x or tablero[posición_inicial_y][posición_inicial_x + i] != 0: 
            tablero_testeo[posición_inicial_y][posición_inicial_x + i - 1] = 5
            barco_derecha = True
        elif total_generado == longitud:
            tablero_testeo[posición_inicial_y][posición_inicial_x  + i - 1] = 5
            barco_derecha = True
        else:
            tablero_testeo[posición_inicial_y][posición_inicial_x  + i] = 4
            total_generado += 1
        i += 1
        
    i = 1
    while barco_izquierda != True:
        if posición_inicial_x - i < 0 or tablero[posición_inicial_y][posición_inicial_x - i] != 0: 
            tablero_testeo[posición_inicial_y][posición_inicial_x  - i + 1] = 6
            barco_izquierda = True
        elif total_generado == longitud:
            tablero_testeo[posición_inicial_y][posición_inicial_x  - i + 1] = 6
            barco_izquierda = True
        else:
            tablero_testeo[posición_inicial_y][posición_inicial_x  - i] = 4
            total_generado += 1
        i += 1

    if total_generado == 1:
        tablero_testeo[posición_inicial_y][posición_inicial_x] = 7 
        
    if total_generado < longitud:
        return False
    else:
        return tablero_testeo
        
def armar_barcos_dibujo(dibujo, sprite):
    """Función que arma los barcos con su dibujo
    E: sprite de barco y dibujo
    S: barco armado
    """
    
    "Son listas del mismo len"
    global barcos_sprites
    i = 0
    cantidad = len(dibujo)
    while i < cantidad:
        dibujo[i] += barcos_sprites[sprite][i]
        i += 1
    return dibujo

def armar_tablero_dibujo(tablero):
    """Función que arma el tablero con su dibujo
    E: tablero
    S: tablero con dibujo
    """
    
    dibujo_final = []
    for filas in tablero:
        dibujo = ["","","","","","",""]
        for columnas in filas:
            dibujo = armar_barcos_dibujo(dibujo, columnas)
        dibujo_final += [dibujo]
    return dibujo_final        

def armar_edificio_dibujo(dibujo, sprite):
    """Función que arma el edificio con su dibujo
    E: dibujo y su sprite
    S: edificio con dibujo
    """

    "Son listas del mismo len"
    global edificios
    i = 0
    cantidad = len(dibujo)
    while i < cantidad:
        dibujo[i] += edificios[sprite][i]
        i += 1
    return dibujo

def armar_tablero_dibujo_edificios(tablero):
    """Función que arma el tablero  con los dibujos de edificios
    E: tablero
    S: tablero con edificios y dibujo
    """
    
    dibujo_final = []
    for filas in tablero:
        dibujo = []
        i = 0
        while i < len(edificios[0]):
            dibujo += [""]
            i += 1
        for columnas in filas:
            dibujo = armar_edificio_dibujo(dibujo, columnas)
        dibujo_final += [dibujo]
    return dibujo_final

def identificar_barcos(barcos):
    """Función que identifica los barcos
    E: barcos
    S: ubicacion barcos"""
    
    tablero_barcos = copiar_lista(barcos)
    i = -1
    i3 = 0
    
    while i3 < len(tablero_barcos):
        i2 = 0
        while i2 < len(tablero_barcos[0]):
            if tablero_barcos[i3][i2] == 2:
                tablero_barcos[i3][i2] = i
                tablero_barcos = identificar_vertical(tablero_barcos, i)
                i -= 1
            if tablero_barcos[i3][i2] == 5:
                tablero_barcos[i3][i2] = i
                tablero_barcos = identificar_horizontal(tablero_barcos, i)
                i -= 1
            if tablero_barcos[i3][i2] == 7:
                tablero_barcos[i3][i2] = i
                i -= 1
            i2 += 1
        i3 += 1
    return tablero_barcos

def identificar_vertical(tablero, indice):
    """Función que identifica de manera vertical en el tablero
    E: tablero e indice
    S: tablero identificado
    """
    
    i = 0
    continuar = True
    while continuar == True:
        i2 = 0
        while continuar == True and i2 < len(tablero[0]):
            if tablero[i][i2] == indice:
                continuar = False
            i2 += 1
        i += 1
    i = i - 1
    i2 = i2 - 1
    while True:
        if tablero[i][i2] == 3:
            tablero[i][i2] = indice
            break
        tablero[i][i2] = indice
        i -= 1
    return tablero

def identificar_horizontal(tablero, indice):
    """Función que identifica de manera horizontal en el tablero
    E: tablero e indice
    S: tablero identificado
    """
    
    i = 0
    continuar = True
    while continuar == True:
        i2 = 0
        while continuar == True and i2 < len(tablero[0]):
            if tablero[i][i2] == indice:
                continuar = False
            i2 += 1
        i += 1
    i = i - 1
    i2 = i2 - 1
    while True:
        if tablero[i][i2] == 6:
            tablero[i][i2] = indice
            break
        tablero[i][i2] = indice
        i2 -= 1
    return tablero

def lista_barcos(barcos):
    """Función que tiene la lista de los barcos
    E: barcos
    S: lista de barcos
    """
    
    barco = -5
    lista_barcos = []
    while barco < 0:
        barco_lista = []
        i = 0
        while i < len(barcos):
            i2 = 0
            while i2 < len(barcos[0]):
                if barcos[i][i2] == barco:
                    barco_lista += [[i, i2]]
                i2 += 1
            i += 1
        lista_barcos += [barco_lista]
        barco += 1
    return lista_barcos

def juego_1(tablero_jugador, tablero_barcos, tablero_ganar, tablero_yanose):
    """
    Función que junta todas las funciones que dan funcionamiento al juego 1
    E: todos los valores y variables necesarias para el juego
    S: el juego en funcionamiento
    """
    global vidas
    while True:
        probar_mas(armar_tablero_dibujo(tablero_jugador))
        fila = parsear_casilla(input())
        columna = parsear_casilla(input())
        
        if type(fila) != int or type(columna) != int:
            return juego_1(tablero_jugador, tablero_barcos, tablero_ganar, tablero_yanose)
            
        if fila >= len(tablero_jugador) or columna >= len(tablero_jugador[0]):
            return juego_1(tablero_jugador, tablero_barcos, tablero_ganar, tablero_yanose)
            
        if fila < 0 or columna < 0:
            return juego_1(tablero_jugador, tablero_barcos, tablero_ganar, tablero_yanose)
            
        if tablero_barcos[fila][columna] != 0:
            tablero_jugador[fila][columna] = tablero_barcos[fila][columna]
            
            barco_hundido = True
            cual_barco = tablero_ganar[fila][columna]
            
            for posicion in tablero_yanose[cual_barco]:
                if tablero_jugador[posicion[0]][posicion[1]] == 0:
                    barco_hundido = False
                    break
            
            if barco_hundido == True:
                for posicion in tablero_yanose[cual_barco]:
                    probar_mas(armar_tablero_dibujo(tablero_jugador))
                    sleep(0.5)
                    tablero_jugador[posicion[0]][posicion[1]] = 8
                    tablero_barcos[posicion[0]][posicion[1]] = 8
                    tablero_ganar[posicion[0]][posicion[1]] = 0
                tablero_yanose[cual_barco] = 0
        else:
            tablero_jugador[fila][columna] = 8
            vidas = vidas - 1
            
        if vidas == 0:
            return "Perdiste"
            
        print('vida = ', vidas)
        
        todos_hundidos = True
        for barco in tablero_yanose:
            if barco != 0:
                todos_hundidos = False
                break
        
        if todos_hundidos:
            return "Todos los balleneros hundidos"

#########################################################################
#                                                                       #
#                           LOGICA JUEGO 2                              #
#                                                                       #
#########################################################################

def juego_2(tablero, cantidad_casillas):
    """
    Función que junta todas las funciones que dan funcionamiento al juego 2
    E: todos los valores y variables necesarias para el juego
    S: el juego en funcionamiento
    """
    global puntos_solarpunk, puntos_urbanitas, turnos

    urbanitas(tablero, cantidad_casillas)
    guerrillas(tablero, cantidad_casillas)
    diseniadores(tablero, cantidad_casillas)
    ganador = puntos(tablero, cantidad_casillas)
    
    if ganador != False:
        return "Ganaron los ", ganador

    municipalidad(tablero, cantidad_casillas)

    print("Solarpunk: ", puntos_solarpunk)

    print("Urbanitas: ", puntos_urbanitas)

    print("Turnos: ", turnos)
    return juego_2(tablero, cantidad_casillas)

def urbanitas(tablero, cantidad_casillas):
    """Función del turno de los urbanitas
    E: tablero, cantidad_casillas
    S: destruye, crea o expande algún edificio
    """
    
    eleccion = random.randint(0,2)
    
    if eleccion == 0:
        destruir([1,2,3,0], tablero, cantidad_casillas, 0)
    elif eleccion == 1:
        crear([1,2,3], tablero, cantidad_casillas)
    elif eleccion == 2:
        expandir([1,2,3], tablero, cantidad_casillas,0)
        
    input("Turno Urbanitas")
    probar_mas(armar_tablero_dibujo_edificios(tablero))

def guerrillas(tablero, cantidad_casillas):
    """Función del turno de los guerrillas
    E: tablero, cantidad_casillas
    S: destruye, crea o expande algún edificio
    """    
    
    eleccion = random.randint(0,2)
    
    if eleccion == 0:
        destruir([4,5,6,7,8,9,0], tablero, cantidad_casillas, 1)
    elif eleccion == 1:
        crear([4,5,6], tablero, cantidad_casillas)
    elif eleccion == 2:
        expandir([4,5,6,7,8,9], tablero, cantidad_casillas, 1)
    input("Turno Guerrillas")
    probar_mas(armar_tablero_dibujo_edificios(tablero))


def diseniadores(tablero, cantidad_casillas):
    """Función del turno del jugador
    E: tablero, cantidad_casillas
    S: destruye, crea o expande algún edificio
    """
    
    print('1. Destruir edificio rival')
    print('2. Crear edificio')
    print('3. Expandir edificio')
    
    eleccion = input('Seleccione que desea realizar: ')
    
    if es_num(eleccion) == False:
        print('Entrada inválida')
        return diseniadores(tablero,cantidad_casillas)

    eleccion = int(eleccion)
    
    if eleccion == 1:
        destruir_diseniadores(tablero,cantidad_casillas)
    elif eleccion == 2:
        crear_diseniadores(tablero,cantidad_casillas)
    elif eleccion == 3:
        expandir_diseniadores([4,5,6,7,8,9], tablero, cantidad_casillas)
    input("Tu turno")
    probar_mas(armar_tablero_dibujo_edificios(tablero))

def pedir_posicion(matriz):
    """
    Función que pide la posicion donde quiere hacer algo al
    usuario
    E: la matriz y se pide la posicion al usuario
    S: retorna la fila y columna si son válidas
    """
    filas = len(matriz)
    columnas = len(matriz[0])

    i = input('Ingrese la fila: ')
    if es_num(i) == False:
        print("Entrada inválida")
        return pedir_posicion(matriz)

    i = int(i)-1
    if i >= filas or i < 0:
        print("Fila fuera de rango")
        return pedir_posicion(matriz)
        
    j = input('Ingrese la columna: ')
    if es_num(j) == False:
        print("Entrada inválida")
        return pedir_posicion(matriz)

    j = int(j)-1
    if j >= columnas or j < 0:
        print("Columna fuera de rango")
        return pedir_posicion(matriz)
        
    return [i,j]

def destruir_diseniadores(tablero, cantidad_casillas):
    """
    Función que destruye edificios de urbanitas al ser opuestos
    edificios 1,2,3
    E: posicion a destruir con coordenadas i,j
    S: destruyo si allí habia un valor que entraba en los 
    parametro o no lo podia hacer porque estaba vacio o con un
    edificio aliado
    """
    casilla = pedir_posicion(tablero)
    
    if casilla != None:
        if esta_lista(tablero[casilla[0]][casilla[1]], [1,2,3]):
            tablero[casilla[0]][casilla[1]] = 0
            print("¡Edificio destruido con éxito!")
        else:
            print("No puedes destruir esa casilla")
            return diseniadores(tablero, cantidad_casillas)
            
def crear_diseniadores(tablero, cantidad_casillas):
    """
    Función que construye edificios propios de los diseñadores
    E: tablero, cantidad_casillas
    S: edificio creado en la posición deseada por el usuario
    """
    
    casilla = pedir_posicion(tablero)
    
    if casilla == None:
        return crear_diseniadores(tablero)
    if tablero[casilla[0]][casilla[1]] != 0:
        return crear_diseniadores(tablero, cantidad_casillas)

    print("Edificios a contruir:")
    print("1. Carretera mixta ")
    print("2. Edificio verde-sostenible ")
    print("3. Terceros espacios ")
    
    construir = input("Selecciona algún edificio a construir: ")

    if construir =="1":
        tablero[casilla[0]][casilla[1]] = 7
    elif construir == "2":
        tablero[casilla[0]][casilla[1]] = 8
    elif construir == "3":
        tablero[casilla[0]][casilla[1]] = 9
    else:
        return diseniadores(tablero, cantidad_casillas)         

def expandir_diseniadores(lista, tablero, cantidad_casillas):
    """
    Función que expande edificios propios y de los guerrillas
    E: tablero, cantidad_casillas
    S: edificio seleccionado expandido
    """
    
    if hay_casilla_expandible(lista, tablero) != True:
        print("No hay edificios disponibles para expandir")
        return tablero

    casilla = pedir_posicion(tablero)
    elemento = tablero[casilla[0]][casilla[1]]
    
    if esta_lista(tablero[casilla[0]][casilla[1]], lista) != True: 
        return diseniadores(tablero, cantidad_casillas)
    else: 
        if casilla[0] < len(tablero)-1:
            if tablero[casilla[0]+1][casilla[1]] == 0:
                tablero[casilla[0]+1][casilla[1]] = elemento
                return(tablero)
        if casilla[0] > 0:         
            if tablero[casilla[0]-1][casilla[1]] == 0:
                tablero[casilla[0]-1][casilla[1]] = elemento
                return(tablero)
        if casilla[1] < len(tablero[0])-1:  
            if tablero[casilla[0]][casilla[1]+1] == 0:
                tablero[casilla[0]][casilla[1]+1] = elemento
                return(tablero)
        if casilla[1] > 0:    
            if tablero[casilla[0]][casilla[1]-1] == 0:
                tablero[casilla[0]][casilla[1]-1] = elemento
                return(tablero)
                        
        return diseniadores(tablero, cantidad_casillas)

def crear(lista, tablero, cantidad_casillas):
    """
    Función que construye edificios al azarmente
    E: tablero, cantidad_casillas, lista de edificios
    S: edificio creado
    """
    casilla = casilla_aleatoria(len(tablero[0]), cantidad_casillas)
    if tablero[casilla[0]][casilla[1]] != 0:
        return crear(lista, tablero, cantidad_casillas)
    else: 
        tablero[casilla[0]][casilla[1]] = lista[random.randint(0, len(lista)-1)]
            
def destruir(lista, tablero, cantidad_casillas, funcion):
    """
    Función que destruye edificios del opuesto
    E: lista, tablero, cantidad_casillas
    S: edificio destruido
    """

    hay_destruible = False
    for fila in tablero:
        for elem in fila:
            if esta_lista(elem, lista) != True:
                hay_destruible = True
                break
        if hay_destruible == True:
            break

    if hay_destruible == False:
        if funcion == 0:
            return urbanitas(tablero, cantidad_casillas)
        if funcion == 1:
            return guerrillas(tablero, cantidad_casillas) 
    
    casilla = casilla_aleatoria(len(tablero[0]), cantidad_casillas)
    
    if esta_lista(tablero[casilla[0]][casilla[1]], lista) != True: 
        tablero[casilla[0]][casilla[1]] = 0
    else: 
        return destruir(lista, tablero, cantidad_casillas, funcion) 

def hay_casilla_expandible(lista, tablero):
    """Función que determina si una casilla tiene espacio alrededor para
    expandirse
    E: lista y tablero
    S: true or false"""
    
    i = 0
    
    while i < len(tablero):
        j = 0
        
        while j < len(tablero[0]):
            if esta_lista(tablero[i][j], lista):
                if i < len(tablero)-1 and tablero[i+1][j] == 0:
                    return True
                if i > 0 and tablero[i-1][j] == 0:
                    return True
                if j < len(tablero[0])-1 and tablero[i][j+1] == 0:
                    return True
                if j > 0 and tablero[i][j-1] == 0:
                    return True
            j += 1
        i += 1
    return False

def expandir(lista, tablero, cantidad_casillas, funcion):
    """
    Función que expande edificios propios y de aliados solamente
    E: tablero, cantidad_casillas, lista
    S: edificio expandido
    """
    
    if hay_casilla_expandible(lista, tablero) != True:
        if funcion == 0:
            return urbanitas(tablero, cantidad_casillas)
        if funcion == 1:
            return guerrillas(tablero, cantidad_casillas)


    casilla = casilla_aleatoria(len(tablero[0]), cantidad_casillas)
    elemento = tablero[casilla[0]][casilla[1]]
    
    if esta_lista(tablero[casilla[0]][casilla[1]], lista) != True: 
        return expandir(lista, tablero, cantidad_casillas, funcion)
    else: 
        if casilla[0] < len(tablero)-1:
            if tablero[casilla[0]+1][casilla[1]] == 0:
                tablero[casilla[0]+1][casilla[1]] = elemento
                return(tablero)
        if casilla[0] > 0:         
            if tablero[casilla[0]-1][casilla[1]] == 0:
                tablero[casilla[0]-1][casilla[1]] = elemento
                return(tablero)
        if casilla[1] < len(tablero[0])-1:  
            if tablero[casilla[0]][casilla[1]+1] == 0:
                tablero[casilla[0]][casilla[1]+1] = elemento
                return(tablero)
        if casilla[1] > 0:    
            if tablero[casilla[0]][casilla[1]-1] == 0:
                tablero[casilla[0]][casilla[1]-1] = elemento
                return(tablero)
                        
        return expandir(lista, tablero, cantidad_casillas, funcion)

def casilla_aleatoria(columnas, cantidad_casillas):
    """Función que elige aleatoriamente una casilla
    E: columnas, cantidad_casillas
    S: fila y columna de la casilla"""
    
    casilla = random.randint(0,cantidad_casillas - 1)
    fila = casilla//columnas
    columna = casilla%columnas
    return [fila, columna]

def cantidad_casillas(tablero):
    """Función que da la cantidad de casillas de un tablero
    E: tablero
    S: numero de casillas"""
    
    i = 0
    
    for filas in tablero:
        for casillas in filas:
            i+=1
    return i

def puntos(tablero, cantidad_casillas):
    """Función que calcula los puntos acumulados por los jugadores
    E: tablero, cantidad de casillas
    S: puntos"""
    
    global puntos_solarpunk, puntos_urbanitas, turnos
    turnos -= 1
    edificio_urbanitas = 0
    edicios_solar_punk = 0

    for filas in tablero:
        for casillas in filas:
            if esta_lista(casillas,  [1,2,3]):
                edificio_urbanitas += 1
            elif casillas != 0:
                edicios_solar_punk += 1

    if edicios_solar_punk == cantidad_casillas:
        return "Solar Punk"
    if edificio_urbanitas == cantidad_casillas:
        return "Urbanitas"

    puntos_urbanitas +=edificio_urbanitas
    puntos_solarpunk += edicios_solar_punk

    if turnos == 0:
        if puntos_urbanitas > puntos_solarpunk:
            return "Urbanitas"
        if puntos_solarpunk > puntos_urbanitas:
            return "Solar Punk"
        else: 
            return "Empate"
    return False

def municipalidad(tablero, cantidad_casillas):
    """Función que hace la función de municipalidad que elimina edificios
    construidos ilegalmente
    E: tablero, cantidad_casillas
    S: tablero si la muni decide eliminar edificio ilegal"""
    
    cantidad_a_destruir = random.randint(0,2)
    
    while cantidad_a_destruir > 0:
        destruir([1,2,3,7,8,9], tablero, cantidad_casillas, 2)
        cantidad_a_destruir -= 1
    input("Turno Municipalidad")
    probar_mas(armar_tablero_dibujo_edificios(tablero))

#########################################################################
#                                                                       #
#                           MENU PRINCIPAL                              #
#                                                                       #
#########################################################################

def jugar():
    """
    Función que presenta el menú del juego
    """
    
    global proporción
    print("Escoge un juego:")
    print("1: Juego 1 (Barcos Balleneros)")
    print("2: Juego 2 (Solarpunk en lucha)")
    juego_seleccionado = input("Selección: ")

    print("Escoge una matriz:")
    print()
    print("")
    print("1: 16x9")
    print("")
    print("2: 9x16")
    print("")
    print("3: 4x3")
    print("")
    print("4: 3x4")
    print("")
    print("5: 1x1")
    print("")

    proporción = (input())
    if es_num(proporción) != True:
        return "Error01"
    proporción = int(proporción)
    if proporción > 5:
        return "Error02"
    
    tablero_jugador = generar_tablero(proporción)

    if juego_seleccionado == "1":
        tablero_barcos = generar_barcos(tablero_jugador)
        tablero_ganar = identificar_barcos(tablero_barcos)
        tablero_yanose = lista_barcos(tablero_ganar)
        
        probar(tablero_jugador)
        return (juego_1(tablero_jugador, tablero_barcos, tablero_ganar, tablero_yanose))
        
    elif juego_seleccionado == "2":
        return (juego_2(tablero_jugador, cantidad_casillas(tablero_jugador)))

    else: 
        return jugar()

print(jugar())
