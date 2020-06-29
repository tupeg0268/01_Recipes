# to do

# ask user for sevings made by recipe (and check this is a number is more than
# ask user for serving desired (check this is a number)
# calculate the scale factor
# warn the user if the scale factor is less than 0.25 or more than 4

# functions go here

# number checking function.
def num_check(question):

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

print("scale factor:{}" .format(scale_factor))
