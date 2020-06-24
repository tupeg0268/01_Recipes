# ask user for amount
# ask user for unit
# check that unit is in dictionary

# if unit in dictionary, convert to ml

# if no unit given / unit is unknown, leave as is.


# ***** Function goes here*****
def unit_check() :

    unit_tocheck = input("unit? ")

    # Abbreviation lists
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]

    if unit_tocheck == "":
        print("you chose {}".format(unit_tocheck))
        return unit_tocheck

    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tbs"

# ***** Main Routine Goes here *****
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000
}

keep_going = ""
while keep_going =="":
    amount = eval(input("how much"))
    amount = float(amount)

    # Get unit and change it to match dictionary.
    unit=unit_check()

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("Amount in ml {}".format(amount))
    else:
        print("{} is unchanged" .format(amount))

    keep_going =input("<enter> or qss")