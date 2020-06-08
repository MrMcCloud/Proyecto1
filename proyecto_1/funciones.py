import pandas as pd
from pelicula import Pelicula


def process_archivo():
    data = pd.read_csv("IMDb_movies.csv")
    return data


def create_pelicula(data):
    films = []
    s = ", "
    for index, row in data.iterrows():
        try:
            votos = row["avg_vote"]
            votos = float(votos)
            if isinstance(votos, float):
                if votos >= 8.0:
                    if votos < 10.0:
                        objeto = Pelicula()
                        nombre = row["original_title"].capitalize()
                        objeto.set_nombre(nombre.capitalize())
                        genero = row["genre"].capitalize()
                        genero = genero.split(s)
                        for i in genero:
                            objeto.set_genero(i.capitalize())
                        actores = row["actors"].capitalize()
                        actores = actores.split(s)
                        for i in actores:
                            objeto.set_actores(i.capitalize())
                        objeto.set_votos(votos)
                        films.append(objeto)
        except Exception as e:
            str(e)
    return films


def search_genero(pelicula, busqueda):
    print("Peliculas del genero: ", busqueda)
    for obj in pelicula:
        for genero in obj.get_genero():
            if genero == busqueda:
                print("+", obj.get_nombre())


def search_actores(pelicula, busqueda):
    print("peliculas en las actua: ", busqueda)
    flag = False
    for obj in pelicula:
        for actor in obj.get_actores():
            if actor == busqueda:
                print("+", obj.get_nombre())
                flag = True
    if flag is False:
        print("no hay considencias")


def show_peliculas(pelicula):
    for obj in pelicula:
        print("\nPelicula: {}".format(obj.get_nombre()))
        for genero in obj.get_genero():
            print("Genero; {}".format(genero))
        for actor in obj.get_actores():
            print("Actor: {}".format(actor))
        print("Votes: {}".format(obj.get_votos()))
