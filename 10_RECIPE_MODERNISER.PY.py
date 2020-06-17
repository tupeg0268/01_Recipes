# modules to be used
import csv
import re

# *****Functions *****

def not_blank(question ,error_msg ,num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes"
            # look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit() == True:
                    has_errors =" yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response

 def num_check(question)

        error = "Please enter a number that is more than zero"

        valid = False
        while not valid:
            try:
                response = float(input(question))

                if response <= 0:
                  print(error)
                else:
                    return response

            except ValueError:
                 print(error)

def get_sf():
    serving_size = num_check("what is the recipe serving size? ")

    # Main Routine goes here
    doggy_sf = "yes"
    while doggy_sf == "yes":

            desired_size = num_check("how many serving are needed?")

            scale_factor = desired_size / serving_size

            if scale_factor > 0.25:
                doggy_sf = input("warning: this scale factor is very small  and you"
                                 " might struggle to accurately weigh the ingredient. \n "
                                 "Do you want to fix this and make more servings ").lower()
            elif scale_factor > 4:
                doggy_sf = input("warning: this scale factor is quite large - you might  "
                                 "have issues with mixing bowl space / oven space. "
                                 "\nDo you want to fix this and make a smaller"
                                 "bath? ").lower()

            else:
                doggy_sf = "no"

     return scale_factor

# ***** Main Routine*****

# set up Dictionaries

# set up list to hold 'modernised' ingredients

# Ask user for recipe name and check its not blank
recipe_name = not_blank("What is the recipe name? ",
                        "The recipe name can't be blank and can't contains numbers ",
                        "no")
# Ask user where the recipe is originlly from (num_ok)
source = not_blank("where is the recipe from ",
                   "The recipe source can't be blank ,",
                   "yes")

# Get serving sizes and scale factor


# Loop for eachingredients

# Get ingredients amount
# Get ingredients name
# Get unit
# Convert unit to ml
# Convert from to g