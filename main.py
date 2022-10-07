# Lab 7 Vira Oetterli och Davide Attebrant
import csv

class DictHash():
    def __init__(self):
        self.dictionary = {}

    def store(self, nyckel, data):
        self.dictionary[nyckel] = data

    def search(self, nyckel):
        if nyckel in self.dictionary:
            return self.dictionary[nyckel]
        else:
            raise KeyError

    def __getitem__(self, nyckel):
        if nyckel in self.dictionary:
            return self.dictionary[nyckel]
        else:
            raise KeyError

    def __contains__(self, nyckel):
        if nyckel in self.dictionary:
            return True
        else:
            raise False


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

    def return_name(self):
        return self.Drama_Name




def create_dict_of_dramamovie_objects():
    with open('kdramaMini.csv') as kdrama:
        dict_of_drama_movies = DictHash()
        spamreader = csv.reader(kdrama)
        counter = 0
        for row in spamreader:
            if counter == 0:
                counter = 1
            else:
                tempdict = Drama(row)
                #print(tempdict.Drama_Name)
                dict_of_drama_movies.store(tempdict.Drama_Name, tempdict)
        return dict_of_drama_movies

dictTest = create_dict_of_dramamovie_objects()
print(dictTest["The Heirs"])
#print(dictTest["banan"])
exit()

# Del 2 --------------------------------------------------------------------------------------------------------
# Noder till klassen Hashtable
class HashNode:


    # key är nyckeln som anvands vid hashningen, data är det objekt som ska hashas in
    def __init__(self, key = "", data = None):

        self.key = key
        self.data = data
        #Fyll i kod här för att initiera hashtabellen

class Hashtable:
    # size: hashtabellens storlek
    def __init__(self, size):

        self.size = size

    #key är nyckeln data är objektet som ska lagras Stoppar in "data" med nyckeln "key" i tabellen.
    def store(self, key, data):
        pass
        #Fyll i kod här!

    # key är nyckeln
#          Hämtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
#          Om "key" inte finns ska det bli KeyError
    def search(self, key):
        #Fyll i kod här!
        #...
        '''else:
            raise KeyError'''

    # key är nyckeln Beräknar hashfunktionen för key
    def hashfunction(self, key):
        pass
        #Fyll i kod här!
