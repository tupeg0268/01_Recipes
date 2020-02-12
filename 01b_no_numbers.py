# Iterate through string...

# ask user for string
recipe_name = input ( "what is the recipe name? ")

error = "Your recipe name has numbers in it."
has_errors =""

# look at each character in string and if it's a number ,complain
for letter in recipe_name:
   if letter.isdigit() ==True:
       print(error)
       has_errors ="yes"
       break

 #give user feedback...
if has_errors != "yes":
  print ("you are OK")
