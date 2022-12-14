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
    # Key ??r nyckeln som anv??nds vid hashningen, data ??r det objekt som ska hashas in
    def __init__(self, key = "", data = None):

        self.key = key
        self.data = data
        self.next = None
        #Fyll i kod h??r f??r att initiera hashtabellen

# En klass f??r Hashtable, den spar Hashnodes i en hashtabell och anv??nder l??nkade listor som krockhantering.
class Hashtable:

    def __init__(self, size):
        self.size = size
        self.hashslots = [None] * size

    # Input ??r key och data, d??r man kan s??ka p?? key f??r att f?? fram data. Anv??nder l??nkade listor som krockhantering.
    def store(self, key, data):
        hashnode = HashNode(key, data)
        hashvalue = self.hashfunction(hashnode.key)
        if self.hashslots[hashvalue] == None:
            self.hashslots[hashvalue] = hashnode
            #print("Stored new value for slot")
        else:
            self.next_element = self.hashslots[hashvalue]
            while self.next_element != None:
                if self.next_element.key == key:
                    self.next_element.data = data        # Ers??tter data med den senaste. Varje key finns bara en g??ng.
                    #print("Replaced data for key " + str(key))
                    return
                self.previous_element = self.next_element
                self.next_element = self.next_element.next
            self.previous_element.next = hashnode
            #print("Inserted new value in linked list at " + str(self.hashfunction(key)))

    # Input ??r en nyckel, output ??r antingen ett KeyError om den inte finns eller data v??rdet sparat under nyckeln.
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

    # Input nyckeln, output ??r ett Hashtal
    def hashfunction(self, key):
        key = str(key)
        hashable_number = 0
        multiplier = 0
        for character in key:
            multiplier += 1
            hashable_number += ord(character)
        return hashable_number % self.size

'''table = Hashtable(11)
table.store("tits", 13)
table.store(16, "balla")
table.store(23, 16)'''
#x = table.search(23)
#print(x)

# Testning del 1
# Vi stoppar in koreanska filen. Vi har ett lambda tal p?? 0.5.

# Funktion som skapar en Hashdictionary med kdrama
def create_dict_of_dramamovie_objects(size):
    with open('kdramaMini.csv') as kdrama:
        dict_of_drama_movies = Hashtable(size)
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


