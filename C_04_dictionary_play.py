my_dict = {
    "blue": "sky",
    "green": "grass",
    "yellow": "sun",
    "red": "apple"
}

to_find = input("What are you looking for?")

# check if it's a key...
if to_find in my_dict:

    # get the value...
    coloured_object = my_dict[to_find]

    print(f"The {coloured_object} is {to_find}")

elif to_find in my_dict.values():
    print(f"{to_find} is a value in the dictionary")

else:
    print("Sorry - item not found")
