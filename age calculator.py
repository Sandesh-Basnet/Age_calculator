# getting age year input
age_input = int(input("In which year were you born: "))
# getting in which year input
in_which_year = input("In which date BS or AD: ").lower()
# using if and elif statement to find the result
if in_which_year == "ad":
    ad_year = 2021 - age_input
    print("You are",ad_year,"year old." )
elif in_which_year == "bs":
    bs_year = 2078 - age_input
    print("You are",bs_year,"year old." )
# if the value is not recognized the it will print your value is not reconized 
else:
    print("Not rercognized value or date")


