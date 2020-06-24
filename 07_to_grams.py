import csv

# Open file
groceries = open('01_ingredients_ml_to_g.csv')

# Read data into a list
csv_groceries =csv.reader(groceries)

# create a dictionary to hold the data
food_dictionary ={}

# Add the data from the list into the dictionary
# (first item in row is the key,next is definition)

for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

print(food_dictionary)

keep_going = ""
while keep_going == "":
     amount =eval(input("how much"))
     amount = float(amount)

    # Get ingredients and change it to match dictionary.
    ingredients = input("Ingredients:")

    if ingredients in food_dictionary:
        mult_by = food_dictionary.get(ingredients)
        amount = amount * float(mult_by) /250
        print("Amount in g {}".format(amount))
    else:
        print("{} is unchanged".format(amount))