from functions import *

movie = dict()
movie[0] = {'Name': '', 'Director': '', 'Year': '', 'Actors': ''}
movie[1] = {'Name': 'starwars dlfjasldfja;sdljf', 'Director': '1', 'Year': '2021', 'Actors': 'tom'}
movie[2] = {'Name': 'starwars fg', 'Director': '2021', 'Year': '2020', 'Actors': 'Hulk'}
movie[3] = {'Name': '2', 'Director': '3-Director', 'Year': '2dfsgdg', 'Actors': '3sdfgsfg'}
movie[4] = {'Name': '4', 'Director': '1', 'Year': '2018', 'Actors': '2021'}

if __name__ == '__main__':
    print("1 - Show all movies")
    print("2 - Search Movie Database")
    seleccionUsuario = input("Select an option")
    if seleccionUsuario == '1':
        movie_read(movie)
    elif seleccionUsuario == '2':
        search = str(input('Search Parameter: '))
        for keys in dict_keys(movie[0]):
            advance_search(movie, keys, search)
    else:
        print('Select a valid option')
