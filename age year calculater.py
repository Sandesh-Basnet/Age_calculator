age_input = int(input("What is is your age: "))
age_year_type = input("In which date you want your age to be (AD or BS): ").lower()
if age_year_type == "ad":
    age = 2020 - age_input
    print("You were born on", age)
elif age_year_type == "bs":
    age_two = 2077 - age_input
    print("You were born on", age_two)
else:
    print("Error! Your date type is not recognized")
