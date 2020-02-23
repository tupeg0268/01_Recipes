# Get's recipe name and check it is not blank



# Not Blank Function goes here
def not_blank(question,  ):

    has_errors = "yes"
    while has_errors != "no":
        response = input(question)

        # checks that the recipe is not blank
        if response == "":
            print("This can't be blank")
            continue

        # checks that recipe does not have numbers
        else:
            for letter in response:
                if letter.isdigit():
                    print("Your recipe title can't have numbers")
                    has_errors = "yes"
                    break
                else:
                    has_errors = "no"

        if has_errors == "no":

            return response

# Main Routine goes her

recipe_name = not_blank("what is the name? ")

print("you are making {}".format(recipe_name))

