import datetime
import random
import json


class Animal:

    def __init__(self, my_type, my_sex, my_birthdate = None):
        self.my_type = my_type
        self.my_sex = my_sex
        self.my_birthdate = my_birthdate

     if my_birthdate == None :
		global current_farms_date
		self.my_birthdate = current_farms_date

    def __str__(self):

    return "Animal": + str(self.my_type) + " " + str(self.my_sex) + " " + str(self.my_birthdate)

    def want_reproduce(self):


        global future_farms_date

		if (self.my_sex == "Female") and ((future_farms_date - self.my_birthdate).days > 365) and ((future_farms_date - self.my_birthdate).days % 365 < 30):

			return True

		else :
			return False

class Fram:

    def __init__(self, farm_name=None):

        self.farm_name = farm_name
    	self.animal_list = []
    	self.current_date = datetime.datetime.now()


    def __str__(self):

        return_string = "Farm : " + str(self.farm_name) + "\n"

    	for current_animal in self.animal_list:

    			return_string += current_animal.__str__() + "\n"

    		return return_string

    def add_animal(self, my_type, my_sex, my_age=None):

        self.animal_list.append(Animal(my_type, my_sex, my_age))
		print("\t\t=>Farm.add_animal(" + str(my_type) + ", " + str(my_sex) + ", " + str(my_age) + ")")
        
    def pass_time(self, time_delta_to_advance):

        	global future_farms_date

		for current_animal in self.animal_list:

	
			if(current_animal.want_reproduce() == True):

				print("\t\tAnimal " + str(current_animal.my_type) + "  wants to reproduce (" + str(current_animal.my_sex) 
						+ " Mouton " + str((future_farms_date - current_animal.my_birthdate).days) + " days)")

				
				
				for searched_animal in self.animal_list:
					if (searched_animal.my_type == current_animal.my_type) and (searched_animal.my_sex == "Male") :

						print("\t\tPerfect match ! A baby was born !")

						self.add_animal(current_animal.my_type, random.choice(["Male", "Female"]), my_age=None)
						
						break


			if((future_farms_date - current_animal.my_birthdate).days > 3*365):
				self.animal_list.remove(current_animal)
				print("\t\tGoodby animal !!")

    

if __name__ == "__main__":=


	global current_farms_date
	current_farms_date = datetime.datetime.now()
	print("We are the : " + str(current_farms_date) + "\n")

	
	farm_list = []
	farm_list.append(Farm("My first farm"))
	farm_list.append(Farm("Another farm"))

	
	farm_list[0].animal_list.append(Animal("Poule", "Male"))
	farm_list[0].animal_list.append(Animal("Mouton", "Male"))
	farm_list[0].animal_list.append(Animal("Vache", "Female"))
	farm_list[0].animal_list.append(Animal("Cochon", "Female"))
	farm_list[1].animal_list.append(Animal("Lapin", "Male"))
	farm_list[1].animal_list.append(Animal("cheval", "Male"))
	farm_list[1].animal_list.append(Animal("chèvre", "Female"))
	farm_list[1].animal_list.append(Animal("Coq", "Female"))

	farm_list[0].add_animal("cow", "Female", datetime.datetime(year=2019, month = 5, day = 3))



	
	for current_farm in farm_list:
		print(current_farm)


	
	print("\nWe start the time...:\n")

	time_iteration = 0

	while time_iteration < 100:

		
		global future_farms_date
		future_farms_date = current_farms_date + datetime.timedelta(days = 28)

		print("\n\tAdvancing to : " + str(future_farms_date))

		time_iteration += 1

		for current_farm in farm_list:
			current_farm.pass_time(datetime.timedelta(weeks = 4))


		current_farms_date = future_farms_date

	
	for current_farm in farm_list:
		print(current_farm)

