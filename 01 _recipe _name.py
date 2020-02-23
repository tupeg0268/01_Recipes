# Get's recipe name and check it is not blank


# Not Blank Function goes here
def not_blank(question) :
    error = "Your recipe name has numbers in it."

    valid = False
    while not valid:
        response = input(question)
        has_errors =""
        if response == "":
            continue
        else:
            return response

# Main Routine goes her

recipe_name = not_blank("what is the name? ")

print("you are making {}".format(recipe_name))

