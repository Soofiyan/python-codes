colours = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

# You can check whether a colour is in the list

# print('Black' in colours)  # Prints True or False

# GO!

# You can add to the list with append

colours.append('Black')
colours.append('White')

# print('Black' in colours)  # Should this be different now?

# GO!

# You can add a list to a list with extend

more_colours = ['Gray', 'Navy', 'Pink']

colours.extend(more_colours)

# Try printing the list to see what's in it

# GO!

# 14. You can add two lists together in to a new list using +

primary_colours = ['Red', 'Blue', 'Yellow']
secondary_colours = ['Purple', 'Orange', 'Green']

main_colours = primary_colours + secondary_colours

# Try printing main_colours

# 15. You can find how many there are by using len(your_list). Try it below

# How many colours are there in main_colours?

# GO!

all_colours = colours + main_colours
print(all_colours)
