import re

# ingredients has mixed fraction followed by unit and ingrdients

full_recipe =[
    "1 1/2 ml flour "
    "3/4 cup milk",
    "1 cup flour"
    "2 tablespoon white sugar",
    "1.5 tsp baking powder",
    "pinch of cinnamon"
]

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()

    # Get amount...
    if re.match(mixed_regex, recipe_line):s

        # Get mixed number by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()

        # Replace space with a + sign...
        amount = mixed_num.replace(" ", "+")
        # Change the string into a decimal
        amount = eval(amount)
        print(amount)

        # Get unit and ingrdients...
        compile_regex = re.compile(mixed_regex)
        print(compile_regex)
        unit_ingredients = re.split(compile_regex,recipe_line)
        unit_ingredients = (unit_ingredients[1]).strip()   # remove extra white space from unit

    else:
        get_amount = recipe_line.split(" ", 1)  # split text at first space

        try:
            amount = eval(get_amount[0])   # Convert amount to float if possiple
        except NameError:
            amount = get_amount[0]
            convert = "no"

            unit_ingredients = get_amount[1]

    # Get unit and ingredients...
    get_unit =unit_ingredients.split(" ", 1)  # splits text at first space
    unit = get_unit[0]
    ingrdients = get_unit[1]

    print ("{} {} {}".format(amount, unit, ingrdients))
