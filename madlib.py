# list to store all the parts 
parts = [
'name',
'1st adjective',
'noun',
'2nd adjective',
'food (plural)',
'noun (plural)',
'verb ending in -ed',
'noun',
]
# dictionary to store user input
parts_of_paragraph ={}

# loop to prompt the user for input
for part in parts:
  word = input(f'Please enter {part}: ')
  parts_of_paragraph[part] = word
#jkgjk

# print madlib
print(f"Come on over to {parts_of_paragraph['name'].capitalize()}'s Pizza Parlor where you can enjoy your favorite {parts_of_paragraph['1st adjective']}-dish pizza's.You can try our famous {parts_of_paragraph['noun']}-lovers pizza,or select from our list of {parts_of_paragraph['2nd adjective']} toppings,including delicious {parts_of_paragraph['food (plural)']}, {parts_of_paragraph['noun (plural)']}, and many more.Our crusts are hand-{parts_of_paragraph['verb ending in -ed']} and basted in {parts_of_paragraph['noun']} to make them seem more Hand-made.")