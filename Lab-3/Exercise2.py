

#       E X E R C I S E  : 02




# You have collected information about cities in your province. You decide to store each city’s
# name, population, and mayor in a file. Write a python program to accept the data for a number of
# cities from the keyboard and store the data in a file in the order in which they’re entered.



def SavingCityInfo():
    file = open("Cities.txt", "w")
    while True:
        city = input("Enter City Name (or type 'exit' to  or save the info of cities): ")
        if city.lower() == "exit":
            break
        population = input("Enter Population: ")
        mayor = input("Enter Mayor's Name: ")

        file.write(f"{city}, {population}, {mayor}\n")
        print("City Information Saved!\n")
    file.close()

SavingCityInfo()





# Write a python program to create a data file student.txt and append the message “Now we are
# AI students”s



file = open("Student.txt", "a")
file.write("Now we are AI students\n")
file.close()

