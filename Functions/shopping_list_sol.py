"""
A program that prints a user's shopping list. The students should make a module called "shopping_list.py" and in it write a function that takes 4 parameters.
    The function should start by prompting the user to enter their name and then print "This is <name?'s shopping list!"
    The shopping list should then print out a need statement for each parameter (e.g. "I need <param>")
    Their function should have a docstring and a single line comment, and they should call their function from inside main.

Created by Emma Lubes, eml5244, for the Academic Success Center Supplemental Instruction Program.
"""

def shopping_list(param1, param2, param3, param4):
    """
	Function that prints the user a shopping list based on the input provided
	"""
    name = input("What is your name?")
    print("This is ", name, "'s shopping list!", sep="")
    print("I need", param1) # printing the first item on my grocery lsit
    print("I need", param2)
    print("I need", param3)
    print("I need", param4)

def main():
    # Note for SI Leader: You can pick some foods or you can go online, find a wheel to spin, put some foods on it, and pick them real time in session!
    shopping_list("carrot", "cupcakes", "bread", "cheese")

main()