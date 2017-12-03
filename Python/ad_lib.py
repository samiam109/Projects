#Ad Lib. Program takes user in put and makes a story out of it!

user_input = {
    "Name": input("Enter your Name: "),
    "Gender": input("Enter your Gender: "),
    "Favourite Colour": input("Enter your Favourite Colour: "),
    "Favourite Activity": input("Enter your Favourite Activity: "),
    "Favourite Place": input("Enter your Favourite Place: "),
    "Age": input("Enter your Age: ")
}

#Func validates input strings and returns the necessary errors
def validateInputStrs(string, type_input):
    errors = ""

    #If the information passed is for an int-type use the integer validator Func
    if type_input == "Age":
        if not all(char.isdigit() for char in string):
            return validateInputInts(string, type_input)
        else:
            return "No errors"

    if any(char.isdigit() for char in string):
        errors += "You are not allowed to use numbers in " + type_input + ". "
    if any(char.isspace() for char in string):
        errors += "Did you accidentilly add a space to your " + type_input + ". "

    if errors == "":
        return "No errors"
    else:
        return errors

#Func validates input integers
def validateInputInts(integer, type_input):
    errors = ""
    if not all(char.isdigit() for char in integer):
        errors += "Did you enter the correct numbers?"
        return errors
    return "No errors"

#loop through entries in the dictionary, calling for validation
for entry in user_input:
    if not validateInputStrs(user_input[entry], entry) == "No errors":
        print(validateInputStrs(user_input[entry], entry))
        user_input[entry] = input("Enter your %s: " %(entry))

print("Once apon a time, a %s named %s was feeling down and %s so he went to %s to do some %s." % (user_input["Gender"], user_input["Name"], user_input["Favourite Colour"], user_input["Favourite Place"], user_input["Favourite Activity"]))
print("%s was only %d" % (user_input["Name"], int(user_input["Age"])))
