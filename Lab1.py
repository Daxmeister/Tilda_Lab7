# Tilda Lab 1 Davide Attebrant och Vira Oetterli Medieteknik

import csv
'''with open('koreadrama.csv') as kdrama:
    spamreader = csv.reader(kdrama)
    for row in spamreader:
        print(row)'''

class Drama:
    def __init__(self, list):
        self.Drama_Name = list[0]
        self.rating = float(list[1])
        self.actors = list[2]
        self.viewship_rate = float(list[3])
        self.genre = list[4]
        self.director = list[5]
        self.writer = list[6]
        self.year = int(list[7])
        self.no_of_episodes = int(list[8])
        self.network = list[9]

    def __str__(self):
        return self.Drama_Name

    def __lt__(self, other):
        if self.rating < other.rating:
            return True
        else:
            return False

    def return_genre(self):
        return self.genre

    def is_it_good(self):
        if self.rating > 5:
            print(str(self.Drama_Name) + " is good")
        else:
            print(str(self.Drama_Name) + " is bad")

# 3. Program som skapar två drama objekt
def program_class_tester():
    kmovie_list_1 = ['Tomorrow', 8.7, 'Kim, John', 3.4, 'Fantasy', 'Kim T', 'Park Ran', 2022, 16, 'MBC']
    kmovie_list_2 = ['Today', 8.6, 'Kim J, Mike', 6.4, 'Sci-Fi', 'Kim A', 'Park Ron', 2012, 11, 'NBC']
    kmovie_1 = Drama(kmovie_list_1)
    kmovie_2 = Drama(kmovie_list_2)
    print(kmovie_1)
    print(kmovie_2)
    if kmovie_1 > kmovie_2:
        print('You should watch: ' + str(kmovie_1))
    else:
        print('You should watch: ' + str(kmovie_2))

    kmovie_2.is_it_good()
    print(str(kmovie_1.return_genre()))

# program_class_tester()

# 4. Funktion som skapar lista med objekt för varje rad i filen utom första raden och returnerar listan
# Creates an object based on list information
#def create_dramaclass(list_of_row):


#Opens and iterates over the file and uses create_dramaclass to create classes and add to list
def create_list_of_dramamovie_objects():
    with open('koreadrama.csv') as kdrama:
        list_of_drama_movies = []
        spamreader = csv.reader(kdrama)
        counter = 0
        for row in spamreader:
            if counter == 0:
                counter = 1
            else:
                list_of_drama_movies.append(Drama(row))
        return list_of_drama_movies

# 5. Sök i listan
def search_rating_better_than(object_list, value):
    for object in object_list:
        if object.rating >= value:
            print(str(object))
        else:
            pass


def search_for_specific_rating(object_list, value):
    for object in object_list:
        if object.rating == value:
            print(str(object) + " has value " + str(value))
        else:
            pass

list = create_list_of_dramamovie_objects()
#search_rating_better_than(list, 9.1)
search_for_specific_rating(list, 8)

