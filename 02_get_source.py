# Get's source of recipe name and checks it is not blank

# To Do
# Allow user to specify a custom error message
# Allow users to specify whether numbers are allowed

# Not Blank functions goes here
def not_blank(question, error_msg,num_ok):
    error =error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors =""

        if'num_ok'!= "yes":
         # Look at each character in stringand if it's a number, complain
         for letter in response :
              if letter.isdigit() ==True:
                 has_errors = "yes"
                 break

        if response =="":
            # print(error)
                 continue
        elif response !="":
                print (error)
                continue
        else:
              return response

 # Main Routine goes here

source =not_blank("What is the recipe from?",
                       "The recipe source can not_blank,",
                      "yes")

print ("You are making {}".format(source))