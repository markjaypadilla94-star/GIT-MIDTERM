# PET ADOPTION
#student : Mark Jay Padilla
pets = []  # starts empty — the user adds pets as the program runs



def display_menu():
    print ("PET ADOPTION MENU")

    print ( "1 add_pet")

    print ( "2 view all pet")

    print ( "3 Count available vs adopted")

    print ( "4 Find a pet by name")

    print ( "5 Exit")


    print ("Choose from the MENU")
    display_menu = input ();
    return choice
    
     # print the menu, return the user's choice

def add_pet(pet_list):
 if input == '1':
   name = input("Enter the pets name: ")
   animal_type = input("Enter the animal type: ")
   status = input("Enter the status: " )


    

def view_pets(pet_list):
    if not pet_list:
        print("No pets available to view.")
        return
    
 
    print("--- Pet List ---")
    for index, pet in enumerate(pet_list, start=1):
        print(


def count_available_adopted(pet_list):
    # loop through, count Available vs Adopted, return both
    pass

def find_pet(pet_list):
    # ask for a name, search the list, print result or "not found"
    pass

# BONUS (optional)
def remove_pet(pet_list):
    pet_list.remove()
    pass

def main():
    running = True
    while running:
        choice = display_menu()
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit




main()