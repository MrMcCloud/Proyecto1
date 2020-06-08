from funciones import process_archivo, create_pelicula, show_peliculas, search_genero, search_actores

if __name__ == "__main__":
    data = process_archivo()
    clear_data = data.filter(["original_title", "genre", "actors", "avg_vote"])
    films = create_pelicula(clear_data)

    search_genero(films, "Drama")
    search_actores(films, "Leonardo dicaprio")
    show_peliculas(films)
