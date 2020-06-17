# modules to be used...
import csv
import re

# ***** Function *****

def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors =" "

        if num_ok != "yes":
            # Look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit()== True:
                    has_errors =("yes")
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response

# Number checking function (Number must be a float that is more than 0)
def num_check(question):

    error = "Please enter a number that is more than zero"

    valid =False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# function to get ( and check amount, unit and ingredients)
def get__all_ingredients():
    all_ingredients =[]

    stop =""
    print("Please enter ingredients one line at a time. Press 'xxx to when "
          "you are done ")
    while stop != "xxx"
        # Ask user for ingredients (via not blank function)
        get_recipe_line = not_blank("recipe Line:"
                                    "This can't be blank"
                                    "Yes")

        # stop loopin if exit code is typed and there are more
        # than 2 ingredients...
        if get_recipe_line.lower() == "xxx" and len(all_ingredients) >1:
            break

        elif get_recipe_line.lower() == "xxx" and len(all_ingredients) <2:
            print("You need at least two ingredients in the list."
                  "Please add more ingredients")

        # If exit code is not entred, add ingredients to list
        else:
            all_ingredients.append(get_recipe_line)

    return all_ingredients


# *****Main Routine*****

# set up Dictionaries

# set up list to hold  original and"modernised" recipes
modernised_recipe = []

# Ask user for recipe name and check its not blank
recipe_name = not_blank("What is the recipe name? ",
                        "The recipe name can't be blank and can't contain numbers",
                        "no"),
# Ask user where the recipe is originally from (numbers OK)
source = not_blank("Where is the recipe from?",
                   "The recipe source can't be blank, "
                   "yes")


# Get serving sizes and scale factor
scale_factor = get_sf()

# Get amounts, units and ingredients from user...
full_recipe = get_all_ingredients()

# Spilit each line of the recipe into amount, unit and ingredients...
mixed_reje



# Convert unit to ml
# Convert from to g
# Put updated ingrdients in list

# Output ingredients list



