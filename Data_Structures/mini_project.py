#1.Create a dictionary that contains a list of people and one interesting fact about each of them.
  #Display each person and his or her interesting fact to the screen. Next, change a fact about one of the people. Also add an additional person and corresponding fact. Display the new list of people and facts. Run the program multiple times and notice if the order changes.

people_and_fact = {
   "Jeff": "Is afraid of Dogs.",
   "David": "Plays the piano.",
   "Jason": "Can fly an airplane"
}
for key , values in people_and_fact.items():
    print(key ,":", values)

print("\n")

people_and_fact["Jeff"] = "Loves cats"

people_and_fact["Jill"] = "Can hula dance"

for key , values in people_and_fact.items():
    print(key ,":", values)
