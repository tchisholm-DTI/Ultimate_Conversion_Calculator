# Decorates statements
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Enter an amount then enter the units that you have and
the units that you need.

The program will convert your amount to the desired unit.  
    ''')


# checks user has entered a number that is more than zero
def num_check(question):
    error = "Please enter a number that is more than zero"

    while True:

        # Ask user for number / exit code
        response = input(question).lower()
        if response == "xxx":
            return "xxx"

        try:

            # ask user to enter a number
            response = float(response)

            # checks number is more than 0
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Main Routine goes here
# Display instructions if requested
want_instructions = input("Press <enter> to see the instructions or any key to continue. ")

if want_instructions == "":
    instructions()

# Domains
valid_type = {"mass", "distance", "time"}

while True:
    calc_type = input("calc_type: ").strip().lower()
    if calc_type == "xxx":
        print("Thank you using conversion calculator!!!^-^")
        break
    if calc_type not in valid_type:
        print("Please enter a valid calculation type.")
        continue

    if calc_type == "time":
        # get amount and units （assume they are valid）
        amount = float(num_check("how much? "))
        from_unit = input("From Unit? ")
        to_unit = input("To Unit? ")
        time_dict = {
          "ms": 3600*1000,
          "s": 3600,
          "min": 60,
          "h": 1,
          "d": 1/24,
          "month": 1/168,
          "y": 1 / (24 * 365 + 6 + 9/60)  # it accounts for leap years
        }

        # multiply to get to our standard value...
        multiply_by = time_dict[to_unit]
        standard = amount * multiply_by

        # Divide to get to our desired value
        divide_by = time_dict[from_unit]
        answer = standard / divide_by
        print(f"There are {answer} {to_unit} in {amount} {from_unit} ")

    if calc_type == "distance":
        # get amount and units （assume they are valid）
        amount = float(num_check("how much? "))
        from_unit = input("From Unit? ")
        to_unit = input("To Unit? ")
        distance_dict = {
            "mm": 1000,
            "cm": 100,
            "m": 1,
            "km": .001,
        }
        # multiply to get to our standard value...
        multiply_by = distance_dict[to_unit]
        standard = amount * multiply_by

        # Divide to get to our desired value
        divide_by = distance_dict[from_unit]
        answer = standard / divide_by
        print(f"There are {answer} {to_unit} in {amount} {from_unit}. ")

    if calc_type == "mass":
        # get amount and units （assume they are valid）
        amount = float(num_check("how much? "))
        from_unit = input("From Unit? ")
        to_unit = input("To Unit? ")
        mass_dict = {
                "mg": 1000,
                "g": 1,
                "kg": .001,
                "t": .000001,
        }
        # multiply to get to our standard value...
        multiply_by = mass_dict[to_unit]
        standard = amount * multiply_by

        # Divide to get to our desired value
        divide_by = mass_dict[from_unit]
        answer = standard / divide_by
        print(f"There are {answer} {to_unit} in {amount} {from_unit}. ")
