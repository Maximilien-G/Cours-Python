class animal:
    def_init_(self, name):
        self.name = name

    def_str_(self):
        return "Cet animal est un" + self.name

class Mammifère(animal):
    pass

    Humain = Omnivore,nb_pattes=2,Qt_nourriture=600,nb=2,

    Lion =  Carnivore,nb_pattes=4,Qt_nourriture=3,nb=1,

    Lapin = Végétarien,nb_pattes=4,Qt_nourriture=100,nb=7,

    Mouton = Vegetarien,nb_pattes=4,Qt_nourriture=500,nb=5,

    class Domestique(animal):
    pass

    Lapin = Mammifère,Vegetarien,nb_pattes=4,Qt_nourriture=100,nb=7,

    Mouton = Mammifère,Vegetarien,nb_pattes=4,Qt_nourriture=500,nb=5,

    chien = Mammifère,Omnivore,nb_pattes=4,Qt_nourriture=500,nb=2,

    Poule = Mammifère,Omnivore,nb_pattes=2,Qt_nourriture=200,nb=8,

    class Animal_Marin(animal):
    pass

    Pieuvre = Carnivore,Qt_nourriture=200,

    if __name__ == "__main__":

    animal_1 = animal("Lapin")
    animal_2 = animal("Mouton")
    animal_3 = animal("chien")
    animal_4 = animal("Poule")
    
    print(animal_1)
    print(animal_2)
    print(animal_3)
    print(animal_4)
  