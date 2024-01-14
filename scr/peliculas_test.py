import peliculas

def test_lee_peliculas(fichero):
    peliculas2 = peliculas.lee_peliculas(fichero)
    print(f'Se han leído {len(peliculas2)} películas.')
    print('Tres primeros registros:')
    for p in peliculas2[:3]:
        print(p)

def test_pelicula_mas_ganancias(peliculas2):
    print('La película con más ganancias de genero=None:')
    print(peliculas.pelicula_mas_ganancias(peliculas2))
    print('La película con más ganancias de genero=Drama:')
    print(peliculas.pelicula_mas_ganancias(peliculas2, 'Drama'))

def test_media_presupuesto_por_genero(peliculas2):
    print(peliculas.media_presupuesto_por_genero(peliculas3))

def test_peliculas_por_actor(peliculas2):
    print('Test de peliculas_por_actor (año_inicial=None, año_final=None):')
    print(peliculas.peliculas_por_actor(peliculas2))
    print('Test de peliculas_por_actor (año_inicial=2010, año_final=2020)')
    print(peliculas.peliculas_por_actor(peliculas2, 2010, 2020))

def test_actores_mas_frecuentes(peliculas2):
    print('Test de actores_mas_frecuentes (n=3, año_inicial=2005, año_final=2015):')
    print(peliculas.actores_mas_frecuentes(peliculas2, 3, 2005, 2015))

def test_recaudacion_total_por_año(peliculas2):
    print('Test de recaudacion_total_por_año (generos=None):')
    print(peliculas.recaudacion_total_por_año(peliculas2))
    print("Test de recaudacion_total_por_año (generos={'Drama', 'Acción'}):")
    print(peliculas.recaudacion_total_por_año(peliculas2, {'Drama', 'Acción'}))

def test_incrementos_recaudacion_por_año(peliculas2):
    print('Test de incrementos_recaudacion_por_año (generos=None):')
    print(peliculas.incrementos_recaudacion_por_año(peliculas3))
    print("Test de incrementos_recaudacion_por_año (generos={'Drama', 'Acción'}):")
    print(peliculas.incrementos_recaudacion_por_año(peliculas3, {'Drama', 'Acción'}))


if __name__ == '__main__':
    #test_lee_peliculas('data\peliculas.csv')
    peliculas3 = peliculas.lee_peliculas('data\peliculas.csv')
    #test_pelicula_mas_ganancias(peliculas3)
    #test_media_presupuesto_por_genero(peliculas3)
    #test_peliculas_por_actor(peliculas3)
    #test_actores_mas_frecuentes(peliculas3)
    #test_recaudacion_total_por_año(peliculas3)
    test_incrementos_recaudacion_por_año(peliculas3)