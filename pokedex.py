import os

MAX = 30

def add():
    try:
        with open("Records.txt", "a") as fptr:
            id = get_new_id()
            name = input("Enter Pokemon name: ")
            height = input("Enter Pokemon height: ")
            weight = input("Enter Pokemon weight: ")
            location = input("Enter Pokemon location: ")
            shiny = input("Is the Pokemon shiny? (yes/no): ")

            fptr.write(f"{id}, {name}, {height}, {weight}, {location}, {shiny}\n")
            print("Record has been added.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_new_id():
    try:
        with open("Records.txt", "r") as fptr:
            lines = fptr.readlines()
            if lines:
                last_id = int(lines[-1].split(',')[0])
                return last_id + 1
            else:
                return 1
    except FileNotFoundError:
        return 1
def welcome():
    gender = ""
    choice = 0
    userName = input("\t\t\tPlease enter your name: ")

    print("\t\t\t--------------------------------------------------------")
    print("\t\t\tHello. Welcome to the PokeDex App.")
    print("\t\t\tThe professor needs your help in finding all the PokeMon across the world.")
    print("\t\t\tThis app is able to display, remove, search, and display entries made.")
    print("\t\t\tWhenever you encounter a pokemon, enter its name, height, weight, location, and whether it's shiny or not.")
    print("\t\t\t(For those who aren't familiar with PokeMon, you can come up with your own Pokemon name and region.)")
    print("\t\t\t(You can also come up with any weight and height number since all PokeMon come in different heights.)")
    print("\t\t\tWhen you are done, the data will be written in a text file and sent to the professor.")
    print("\t\t\tThis data is very important in understanding the mysterious world of PokeMon.")
    print("\t\t\t--------------------------------------------------------")
    
    while True:
        print("\t\t\t--------------------------------------------------------")
        gender = input(f"\t\t\t{userName} are you a boy or a girl? ")
        
        if gender in ["boy", "girl"]:
            break
        else:
            print("\t\t\tPlease enter a valid input!")
    
    print("\t\t\t--------------------------------------------------------")
    print(f"\t\t\tOk {userName}, it's been indicated that you are a {gender}.")
    
    while True:
        print("\t\t\t--------------------------------------------------------")
        choice = int(input("\t\t\tInput 1 for yes, or 2 for no: "))
        
        if choice == 1:
            print("\t\t\t--------------------------------------------------------")
            print("\t\t\tLet's begin. Welcome to the world of PokeMon.")
            break
        elif choice == 2:
            print("\t\t\tTERMINATING PROGRAM...")
            exit(1)
        else:
            print("\t\t\tPlease enter a valid input!")

def menu():
    while True:
        print("\t\t\t--------------------------------------------------------")
        print("\t\t\t\t\t   POKEDEX APPLICATION")
        print("\t\t\t1. INSERT POKEMON DATA")
        print("\t\t\t2. REMOVE POKEMON DATA")
        print("\t\t\t3. SEARCH FOR POKEMON DATA")
        print("\t\t\t4. DISPLAY POKEMON DATA")
        print("\t\t\t5. TERMINATE PROGRAM")
        
        menuSelection = int(input("\n\t\t\tMAKE A SELECTION BASED ON A CORRESPONDING NUMBER: "))
        
        if menuSelection == 1:
            insert()
        elif menuSelection == 2:
            delete()
        elif menuSelection == 3:
            search()
        elif menuSelection == 4:
            view()
        elif menuSelection == 5:
            exitProgram()
        else:
            print("\t\t\tPlease enter a valid input")

def insert():
    counter = 0
    mon = {}
    
    while True:
        print("\t\t\t--------------------------------------------------------")
        mon['pokeName'] = input("\t\t\tEnter PokeMon name: ")
        mon['location'] = input("\t\t\tEnter the Region: ")
        mon['weight'] = float(input("\t\t\tEnter the weight in pounds: "))
        mon['height'] = float(input("\t\t\tEnter the height in meters: "))
        mon['shiny'] = input("\t\t\tIs the pokemon shiny? Y/N: ")

        with open("Records.txt", "a") as fptr:
            fptr.write("--------------------------------------------------------\n")
            fptr.write(f"Pokemon name: {mon['pokeName']}\n")
            fptr.write(f"Region: {mon['location']}\n")
            fptr.write(f"Weight: {mon['weight']:.2f} lbs\n")
            fptr.write(f"Height: {mon['height']:.2f} m\n")
            fptr.write(f"Shiny: {mon['shiny']}\n")
            fptr.write("--------------------------------------------------------\n")
        
        print("\n\t\t\t--------------------------------------------------------")
        print("\t\t\tInformation was saved.")
        print("\t\t\t--------------------------------------------------------")
        
        while True:
            counter = int(input("\t\t\tWould you like to make another entry?\n\t\t\tEnter 1 for Yes, or 2 for No: "))
            if counter == 1:
                break
            elif counter == 2:
                print("\t\t\tYou will be returned to the main menu")
                return
            else:
                print("\t\t\tPlease enter a valid input.")

def view():
    try:
        with open("Records.txt", "r") as fptr:
            print("\t\t\tPOKEMON DATA")
            print("\t\t\t--------------------------------------------------------")
            for line in fptr:
                print(line.strip())
    except FileNotFoundError:
        print("\t\t\tERROR: Records file not found.")
    
    input("\t\t\tPress Enter to return to the main menu.")


def search():
    name = input("\t\t\tEnter the name of the PokeMon you would like to search for: ")
    
    try:
        with open("Records.txt", "r") as fptr:
            found = False
            for line in fptr:
                if name in line:
                    found = True
                    print(line.strip())
            if not found:
                print("\t\t\tRecord could not be found.")
    except FileNotFoundError:
        print("\t\t\tERROR: Records file not found.")
    
    input("\n\t\t\tPress Enter to return to the main menu.")
def delete():
    while True:
        print("\t\t\t--------------------------------------------------------")
        deloption = int(input("\t\t\tWould you like to delete a record? (Input 1 for yes, or 2 for no): "))
        
        if deloption == 1:
            delete_id = input("\t\t\tPlease enter the ID of the PokeMon you would like to delete: ")
            break
        elif deloption == 2:
            return
        else:
            print("\t\t\tPlease make a valid input!")
    
    try:
        with open("Records.txt", "r") as fptr, open("DeleteRecords.txt", "w") as delptr:
            found = False
            for line in fptr:
                if line.startswith(delete_id + ","):
                    found = True
                    print("\t\t\tThe record has been found and will now be deleted from the application.")
                else:
                    delptr.write(line)
        
        if not found:
            print("\t\t\tRecord does not exist.")
        
        os.remove("Records.txt")
        os.rename("DeleteRecords.txt", "Records.txt")
        print("\t\t\tYou will now be returned to the main menu.")
    except FileNotFoundError:
        print("\t\t\tERROR: Records file not found.")

def exitProgram():
    print("\t\t\t--------------------------------------------------------")
    print("\t\t\tThank you for participating in this research task.")
    print("\t\t\tThe professor and his research team would like to thank you for your help.")
    print("\t\t\tTake care.")
    print("\t\t\tPRINTING DATA...")
    print("\t\t\tSENDING DATA...")
    print("\t\t\tTERMINATING PROGRAM...\n")
    exit(1)

if __name__ == "__main__":
    welcome()
    while True:
        menu()


