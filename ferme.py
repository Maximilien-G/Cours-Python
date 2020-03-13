import random

class Animal():
        def __init__(self,typeAnimal,age,):
            self.type = typeAnimal
            self.age = age
            self.sex =  random.choice(['Femelle', 'Male','Non Binaire'])
     
        def __str__(self):
            return "Type: {} age: {} sex: {}".format(self.type, self.age, self.sex)

class Farm:
        def __init__(self, nom):
            self.nom = nom
            self.Farm_Animal = []
    
        def __str__(self):
            out = ""
            for my_key in self.Farm_Animal:
                out += str(my_key) + "\n"

            return out   

if __name__ == "__main__":  
    Farm_list = []
    Farm_list.append(Farm("Farm"))
    Farm_list[0].Farm_Animal.append(Animal("vache", 1))
    Farm_list[0].Farm_Animal.append(Animal("poule", 1))
    Farm_list[0].Farm_Animal.append(Animal("mouton", 1))

    print(Farm_list[0])
     
  