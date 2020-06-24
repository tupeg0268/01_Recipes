# ingredient list


# number checking Function
def num_check(question):

    error = "please enter a number that is more than zero"

    valid = False
    while not valid:
            response = (input(question))

            if response.lower() == "xxx":
                return "xxx"

            else:
                try:
                    if float(response) <= 0:
                        print(error)
                    else:
                        return response

                except ValueError:
                    print(error)

# Not blank function goes here
def not_blank(question,error_msg,num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # Look at each character in string and if it's a number,complain
            for letter in response:
                if letter.isdigit () == True:
                    has_errors ="yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


# Main routine...

# replace line below with components 3 in due course...
scale_factor = eval(input("scale factors:"))

# Set up empty ingredients list
ingredients =[]

# Loop to ask user to enter an ingredients
stop = ""
while stop != "xxx":

    amount = num_check("What is the amount for the ingredients? ")

    # stop looping if exit code is typed and there are more
    # than 2 ingredients...
    if amount.lower() == "xxx" and len(ingredients) > 1:
        break

    elif amount.lower() == "xxx" and len(ingredients) <2:
        print("You need at least two ingredients in the list. "
              "Please add more ingredients.")

    # if exit code is not entered, add ingredients to list
    else:
        # Ask user  for ingredients (via not blank function )
        get_ingredients = not_blank("please type in an ingredients name:" ,
                                    "this can't be blank",
                                    "yes")
        amount = float(amount) * scale_factor



        ingredients.append("{} units {}".format(amount, get_ingredients))


# output list
print(ingredients)

