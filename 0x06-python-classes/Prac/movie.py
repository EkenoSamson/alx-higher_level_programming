#!/usr/bin/python3
#By Ekeno

class Movie:
    '''This is a blueprint for movie'''
    def __init__(self, title, director, hero):
        self.title = title
        self.director = director
        self.hero = hero

    def info(self):
        print('Title of the movie is : ', self.title)
        print('The director is : ', self.director)
        print('The hero/heroine is : ', self.hero)

list_of_movies = []

while True:
    title = input("Enter the name of the movie: ")
    director = input("Who is the director: ")
    hero = input("Who is the hero/heroine of the movie: ")
    
    m = Movie(title, director, hero)
    list_of_movies.append(m)
    print("Movies addition success")

    option = input("Would you like to  continue [yes/no]: ")
    if option.lower() == 'no':
        break

print("All movies informatio:")
for movie in list_of_movies:
    movie.info()
    print()

print("Merry Christmas")
