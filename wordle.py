# List of animals
animals = ['Cat', 'Dog', 'Lion', 'Rat', 'Cow']

# pseudo code for getting user input

# 1 prompt user first word attempt into a  list
first_word_attempt = input("Enter your first word: ")
list1 = list(first_word_attempt)

# 2 prompt user for the results they got on the word into a list
print(list1)
# 3 results C if letter is correct in correct position
for animal in animals:
    if animal == list1:


#   results X if letter is correct but in incorrect position
#   results E if letter not in word
# combine the 2 prompts into a dictionary
# example first try SMART 
#         results   EECXX
#
# get user input
