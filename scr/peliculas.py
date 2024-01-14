from typing import NamedTuple, List, Tuple, Dict, Set
from datetime import datetime, date
import csv
from collections import defaultdict


Pelicula = NamedTuple(
    "Pelicula",
    [("fecha_estreno", date), 
    ("titulo", str), 
    ("director", str), 
    ("generos",List[str]),
    ("duracion", int),
    ("presupuesto", int), 
    ("recaudacion", int), 
    ("reparto", List[str])
    ]
)

def parsea_listas(lista):
    lista_parseada = [elemento.strip() for elemento in lista.split(',')]

    return lista_parseada

def lee_peliculas(ruta_csv: str) -> List[Tuple]: 
    '''Recibe una cadena de texto con la ruta de un fichero csv, y devuelve una lista
    de tuplas Pelicula con la información contenida en el fichero.
    Utilice datetime.strptime(cadena, "%d/%m/%Y").date() para parsear las fechas.''' 
    with open(ruta_csv, encoding='utf-8') as f:
        res = []
        lector = csv.reader(f, delimiter=';')
        next(lector)
        for fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto in lector:
            fecha_estreno = datetime.strptime(fecha_estreno, '%d/%m/%Y').date()
            generos = parsea_listas(generos)
            duracion = int(duracion)
            presupuesto = int(presupuesto)
            recaudacion = int(recaudacion)
            reparto = parsea_listas(reparto)
            tupla = Pelicula(fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto)
            res.append(tupla)
    return res

def pelicula_mas_ganancias(peliculas: List[Tuple], genero: str = None) -> Tuple[str, int]: 
    '''Recibe una lista de tuplas de tipo Pelicula y una cadena de texto genero,
    con valor por defecto None, y devuelve el título y las ganancias de la película
    con mayores ganancias, de entre aquellas películas que tienen entre sus géneros
    el genero indicado. Si el parámetro genero es None, se busca la película con
    mayores ganancias, sin importar sus géneros. Las ganancias de una película se
    calculan como la diferencia entre la recaudación y el presupuesto.'''
    filtrado = [p for p in peliculas if (genero==None) or (genero in p.generos)]
    titulo_ganancias = defaultdict(int)
    for p in filtrado:
        titulo_ganancias[p.titulo] = p.recaudacion - p.presupuesto
    mas_ganancias = max(titulo_ganancias.items(), key= lambda item:item[1])

    return mas_ganancias
        

def media_presupuesto_por_genero(peliculas: List[Tuple]) -> Dict[List[str],float]: 
    '''Recibe una lista de tuplas de tipo Pelicula y devuelve un diccionario en el que
    las claves son los distintos géneros y los valores son la media de presupuesto de
    las películas de cada género.'''
    genero_pres = defaultdict(list)
    genero_media_pres = defaultdict(float)

    for p in peliculas:
        for g in p.generos:
            genero_pres[g].append(p.presupuesto)

    for genero, presupuestos in genero_pres.items():
        media_pres = sum(presupuestos)/len(presupuestos)
        genero_media_pres[genero] = media_pres

    return dict(genero_media_pres)

def año_en_rango(año, año1, año2):
    return ((año1==None) or (año1 <= año)) and ((año2==None) or (año <= año2))

def peliculas_por_actor(peliculas: List[Tuple], año_inicial: int = None, año_final: int = None) -> Dict[str, int]: 
    '''Recibe una lista de tuplas de tipo Pelicula y dos enteros año_inicial y año_final,
    con valor por defecto None, y devuelve un diccionario en el que las claves son los
    nombres de los actores y actrices, y los valores son el número de películas,
    estrenadas entre año_inicial y año_final (ambos incluidos), en que ha participado
    cada actor o actriz. Si año_inicial o año_final son None, se contarán las películas
    sin filtrar por año inicial o final, respectivamente.'''
    filtrado = [p for p in peliculas if año_en_rango(p.fecha_estreno.year, año_inicial, año_final)]
    actor_pel = defaultdict(list)
    actor_num = defaultdict(int)
    for p in filtrado:
        for a in p.reparto:
            actor_pel[a].append(p)
    for actor, pels in actor_pel.items():
        actor_num[actor] = len(pels)

    return dict(actor_num)


def actores_mas_frecuentes(peliculas: List[Tuple], n: int, año_inicial: int = None, año_final: int = None) -> List[str]: 
    '''Recibe una lista de tuplas de tipo Pelicula, un entero n y dos enteros año_inicial
    y año_final, con valor por defecto None, y devuelve una lista con los n actores o
    actrices que han participado en más películas estrenadas entre año_inicial y año_final
    (ambos incluidos). La lista de actores o actrices debe estar ordenada alfabéticamente.
    Si año_inicial o año_final son None, se contarán las películas sin filtrar por año
    inicial o final, respectivamente. Haga uso de la función peliculas_por_actor para
    implementar esta función.'''
    actor_num = peliculas_por_actor(peliculas, año_inicial, año_final)
    actores_ord = sorted(actor_num.items(), key= lambda item:item[1], reverse= True)
    nombres = []
    for actor, num in actores_ord[:n]:
        nombres.append(actor)
    nombres.sort()

    return nombres


def recaudacion_total_por_año(peliculas: List[Tuple], generos: Set[str] = None) -> Dict[int,int]:
    '''Recibe una lista de tuplas de tipo Pelicula y un conjunto de cadenas de texto
    generos, con valor por defecto None, y devuelve un diccionario en el que las claves
    son los años en los que se han estrenado películas, y los valores son la recaudación
    total de las películas estrenadas en cada año que son de alguno de los géneros
    contenidos en el parámetro generos. Si generos es None, se calcularán las recaudaciones
    totales de todas las películas de cada año, independientemente de su género.
    NOTA: Puede usar operaciones entre conjuntos para ver si existe alguna coincidencia
    entre los géneros de cada película y los géneros especificados por el parámetro.'''
    
    año_recs = defaultdict(list)
    año_total_rec = defaultdict(int)
    filtrado = [p for p in peliculas if (generos==None) or (len(set(p.generos)&generos)>0)]
    
    for p in filtrado:
        año_recs[p.fecha_estreno.year].append(p.recaudacion)

    for año, recs in año_recs.items():
        año_total_rec[año] = sum(recs)

    return dict(año_total_rec)


def incrementos_recaudacion_por_año(peliculas: List[Tuple], generos: set[str] = None) -> List[int]: 
    '''Recibe una lista de tuplas de tipo Pelicula y un conjunto de cadenas de
    texto generos, con valor por defecto None, y devuelve una lista de enteros
    con las diferencias de recaudación total de cada año con respecto al anterior
    registrado, de películas de alguno de los géneros indicados por el parámetro generos.
    Si generos es None, se usarán para el cálculo las recaudaciones totales de
    todas las películas de cada año, independientemente de su género. Haga uso de la
    función recaudacion_total_por_año para implementar esta función.'''
    año_total_rec = recaudacion_total_por_año(peliculas, generos)
    año_total = sorted(año_total_rec.items())
    año_dif = defaultdict(int)
    diferencias = []

    for año_rec1, año_rec2 in zip(año_total, año_total[1:]):
        año_dif[año_rec2[0]] = año_rec2[1] - año_rec1[1]
    
    for año, dif in año_dif.items():
        diferencias.append(dif)

    return diferencias



