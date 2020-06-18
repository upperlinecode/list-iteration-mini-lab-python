# Here's a list of all of Alex's favorite foods.
favorite_foods = ["Sushi", "Pizza", "Salmon", "Tamales dulces", "Yuca fries", "Apple pie", "Katsu curry", "Shrimp and grits", "Waffles"]

# 1. For each food in the list, print out a statement that says "I really love _____" and then fill in the blank with each.



# 2. Let's expand the dialogue - For each food in the list, print out three lines.
#    "Have you ever tried ___?"
#    "I really recommend that you try _____."
#    "_____ is delicious."




# 3a. Now for each food in that list, let's be specific about how MUCH Alex likes them. We'll do this without iteration first.
# For example, print out "Alex's #1 favorite food is Sushi" and then "Alex's #2 favorite food is Pizza" and so on until you've made an ordered list.
# To start, you can copy-paste this line as many times as you need, and make small adjustments:
#
# print("Alex's #" + str(1) + " favorite food is " + favorite_foods[0])




# 3b. Now comment out the above code, and try doing the same thing with a loop - you will likely need fewer lines of code.
# This can be done a number of different ways, but the easiest is probably by iterating over each index in the favorite_foods list using a function called "range". Try to find it in the documentation.




# 4. Below is a massive list of numbers. Iterate over the list and print out only the numbers less than 100.
many_numbers = [109, 141, 44, 51, 133, 366, 339, 248, 226, 321, 97, 195, 245, 252, 238, 1, 366, 47, 189, 91, 148, 88, 194, 106, 5, 128, 165, 337, 380, 181, 143, 95]



# 5. Now iterate over the list but print out only the even ones.



# 6. Below is a list of 99 names. Iterate over them all and print out only the names that include the letter "a".
many_names = ["Alexa","Burke","Kasimir","Baxter","Carissa","Vielka","Derek","Jemima","Jackson","Keegan","Graham","Melissa","Jeanette","Grant","Kirsten","Naida","Brody","Ishmael","Kane","Seth","Rae","Eagan","Camille","Alana",
  "Vance","Melinda","Tarik","Risa","Jordan","Camilla","Karly","Baker","Adena","Calvin","Kendall","Nasim","Kellie","Dana","Rhoda","Linus","Tyler","Ahmed","Dante","Shay","Lael","Tana","Claudia","Chadwick","Tara",
  "Fulton","Justine","Malcolm","Rowan","Christopher","Ciaran","Ivan","Hiram","Blake","Colton","Nathaniel","Moses","Cynthia","George","Ignacia","Chanda","Wyatt","Amethyst","Vladimir","Adam","Boris","Joseph","Scarlett","Kieran","Curran",
  "Dalton","Paul","Phillip","Plato","Renee","Natalie","Barbara","Keiko","Oleg","Xerxes","Caesar","Kareem","Ahmed","Charles","Cyrus","Adria","Winifred","Pandora","Wynne","Simon","Wanda","Coby","Nolan","Marsden","Courtney"]



# 7. Now iterate over the list and print out only the names which have more than 6 letters in them.



# 8. Iterate over the list and find the longest name in the whole thing. Then print out "The longest name in the list is ______. It has ___ letters in it."



# 9. Take that same list and sort it into two lists: one list of long names, which have more than 6 characters, and one list of short names which have 6 or fewer characters. Then print out both lists.



# 10. Are there more long names or short names? Write code to figure that out.



# CHALLENGE: Iterate over the list of numbers to find the average of them all.
