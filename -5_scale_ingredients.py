# Ingredient list


# number checking function
def num_check(question):

    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response =float (input(question))
        has_errors = ""

        if num_check != "yes":
            # look at each character in string and if it's a number
            for letter in response:
                if letter.isdigit() == True:
                    has_error = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response
# Main Routine ...

# Set up empty ingredients list
ingredients = []

# Loop to ask user to enter an ingredients
stop = ""
while stop != "xxx":
    # Ask user for ingredient (via not blank function)
    get_ingredients = not_blank("Please type in an ingredient name: "
                                "This can't be blank",
                                "yes")

    # Stop loopin if exit code is typed and there are more
    # than 2 ingredients ...
    if get_ingredients.lower() == "xxx" and len(ingredients) > 1:
        break

    # If exit code is not entered,add ingredient to list
    else:
        ingredients.append(get_ingredients)

# output list
print(ingredients)
