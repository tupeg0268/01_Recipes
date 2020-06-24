# modules to be used
import csv

# *****Function*****

def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # Look at each character in string and if it's a number, complain
            for letter in response :
                if letter.isdigit():
                    has_errors = "yes"
                    break

        if response == "":
            # print(error)
            continue
        elif response != "":
            print (error)
            continue
        else:
            return response

# *****Main rountine*****

# set up dictionaries

# set up list to hold 'moderniser'ingredients

# Ask user for the recipe name and check its not blank
recipe_name = not_blank("What is the recipe name?",
                  "The recipe names can't be blank and can't contains numbers,",
                  "no")
# Ask user where the recipe is originally from(numbers OK)
source = not_blank("Where is the recipe from?",
                  "The recipe source can't be blank,",
                  "yes")
# Get serving sizes and scale factor

# Loop for each ingredieents...

# Get ingredients amount
# Get ingredients name
# Get unit
# Convert unit to ml
# Convert from ml to g
# Put updated ingredients in list

# Output ingredients list