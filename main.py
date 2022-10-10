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
        return self.rating < other.rating

    def __eq__(self, other):
        return self.rating == other.rating

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

#dictTest = create_dict_of_dramamovie_objects()
#print(dictTest["The Heirs"])
#print(dictTest["banan"])


# Del 2 --------------------------------------------------------------------------------------------------------
# Noder till klassen Hashtable
class HashNode:
    # key är nyckeln som anvands vid hashningen, data är det objekt som ska hashas in
    def __init__(self, key = "", data = None):

        self.key = key
        self.data = data
        self.next = None
        #Fyll i kod här för att initiera hashtabellen


class Hashtable:
    def __init__(self, size):
        self.size = size
        self.hashslots = [None] * size

    #key är nyckeln data är objektet som ska lagras Stoppar in "data" med nyckeln "key" i tabellen.
    def store(self, key, data):
        hashnode = HashNode(key, data)
        hashvalue = self.hashfunction(hashnode.key)
        if self.hashslots[hashvalue] == None:
            self.hashslots[hashvalue] = hashnode
            print("Stored new value for slot")
        else:
            self.next_element = self.hashslots[hashvalue]
            while self.next_element != None:
                if self.next_element.key == key:
                    self.next_element.data = data        # Ersätter data med den senaste så att varje key bara finns en gång.
                    print("Replaced data for key " + str(key))
                    return
                self.previous_element = self.next_element
                self.next_element = self.next_element.next
            self.previous_element.next = hashnode                # Kommer antingen att ersätta None eller en identisk.
            print("Inserted new value in linked list at " + str(self.hashfunction(key)))


    # key är nyckeln
#          Hämtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
#          Om "key" inte finns ska det bli KeyError
    def search(self, key):
        hashvalue = self.hashfunction(key)
        if self.hashslots[hashvalue] == None:
            raise KeyError
        else:
            self.next_element = self.hashslots[hashvalue]
            while self.next_element != None:
                if self.next_element.key == key:
                    return self.next_element.data
                self.next_element = self.next_element.next
            raise KeyError

    # key är nyckeln Beräknar hashfunktionen för key
    def hashfunction(self, key):
        key = str(key)
        hashable_number = 0
        multiplier = 0
        for character in key:
            multiplier += 1
            hashable_number += ord(character)
        print(hashable_number)
        print(hashable_number % self.size)
        return hashable_number % self.size

table = Hashtable(11)
table.store("tits", 13)
table.store(16, "balla")
table.store(23, 16)
#x = table.search(23)
#print(x)
