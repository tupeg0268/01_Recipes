# To do

# Ask user for serving made by recipe (and check this is a number that is more than
# Ask user for serving desired (check this is a number )
# calculate the scale factor
# warn the user if the scale factor is less than 0.25 or more than 4

# Functions go here

# number checking function
def num_check(question):

    error = "please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input (question))


            if response <= 0:
                print(error)
            else:

                return response

        except ValueError:
            print(error)


# main routine goes here

serving_size = num_check("what is the reecipe serving size? ")
desired_size =num_check("how many serving are needed? ")

scale_factor = desired_size / serving_size

print("scale faactor :{}".format(scale_factor))
