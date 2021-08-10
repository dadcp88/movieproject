#
# for dict in movie.keys():
#     value = movie[dict]
#     # list(value)
#     # print(value)
#     print(movie.get(dict))
#     # print(movie.keys())

# movie.update({'name_movie': '2', 'director': '2', 'year_movie': '3'})
# movie.update({'name_movie': '3', 'director': '2', 'year_movie': '3'})
# movie.update({'name_movie': '4', 'director': '2', 'year_movie': '3'})
# print(movie)

def counter():
    counternumber = list(movie.keys())
    print(bool(counternumber))
    if not counternumber:  # Si el dictionario no tiene valores, es Falso y se inicializa counter a 0
        counternumber = 0
    else:
        counternumber = max(counternumber) + 1
    print(counternumber)
    return counternumber


def movie_add():
    name_movie = input('Name of the movie: ')
    director_movie = input('Director of the movie: ')
    year_movie = input('Year of the movie: ')
    Actor_movie = input('Actor of the movie: ')
    movie[name_movie] = {"name_movie": name_movie, "director": director_movie, "year_movie": year_movie,
                         "Actors": Actor_movie}
    # movie.update({'name_movie': name_movie, 'director': director_movie, 'year_movie': year_movie})
    print(movie)


def movie_read():
    for movies in movie:
        print(movies)


# def movie_search():
#
def test_dict(dict):
    keyslist = []
    itemsList = dict.items()
    print(itemsList)
    valueslist = dict.values()
    print(valueslist)
    getlist = dict.get('starwars0')
    getgetlist = getlist.get('Director')
    print(getgetlist)
    print(getlist)
    blalist = dict.keys()
    print(blalist)


def movie_search(dict):
    search = str(input('Ingrese nombre pelicula: '))

    for x in dict:
        if search == str(x):
            print(f"Nombre Pelicula: ", x)
            for keys in dict_keys(dict[x]):
                print(f'{keys}:', dict[x][keys])  # print every keys with the values
        else:
            continue
    print("pelicula no encontrada")
    return False


def dict_keys(dict):  # Return keys from a dictionary
    dict_keys = dict.keys()
    return dict_keys


def advance_search(dict, search_key, search):
    for x in dict:
        getvalues = dict.get(x)
        getvalues = getvalues[search_key]
        if search in str(getvalues):
            print('-------')

            for keys in dict_keys(dict[x]):
                print(f'{keys}:', dict[x][keys])  # print every keys with the values
            print('-------')
        else:
            continue
