#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

# this program takes an input (for example a name)
# and returns the capitalized version of that string
# it checks if the input has special characters or numbers, too
import re
import sys


# define a utility function that checks it the user input is a string
def is_string(s):
    """
    is_string takes one input `s' and returns `str(s)' if s is
    actually a string (silent `ValueError'); otherwise, it exits with status 1
    """
    for operation in [int, float]:
        try:
            _test = operation(s)  # test if s is an int
            print("invalid input: {}, please input a string".format(_test))
            return False
        except ValueError:
            # do nothing
            pass
    else:
        return str(s)


# ask the user for input
input_str = input("please enter your name: ")

# check if user input is a valid string
valid_str = is_string(input_str)
if not valid_str:
    sys.exit(1)

# check if the user input is at least two characters long (otherwise,
# it can hardly be a name and capitalization does not make sense)
if len(valid_str) < 2:
    print("you should enter a string composed of at least two characters!")
    sys.exit(1)

# check if the user input is anything else but a char a:zA:Z
pattern = re.compile("[A-Za-z]")
for c in valid_str:
    m = pattern.match(c)
    if not m:
        print("invalid input: {} is not a valid character".format(c))
        sys.exit(1)

# if no error occured during execution, output the capitalized input string
print("capitalized name: {}".format(valid_str.capitalize()))
