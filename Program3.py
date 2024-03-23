#Pseudocode

import pyfiglet

print()

#Prompt user to input name
name = input("What is your name? ")

#Prompt user to input dream job
dream_job = input("What is your dream job? ")

#Prompt user to input favorite food
favorite_food = input("What is your favorite food? ")

#Prompt user to input favorite color
favorite_color = input("What is your favorite color? ")

#Format inputted name in a fancy way
name_art1 = pyfiglet.figlet_format("Hello!", font="cybermedium")
name_art2 = pyfiglet.figlet_format(name, font="univers")

#Format inputted dream job in a fancy way
dream_job_art1 = pyfiglet.figlet_format("Your Dream Job is: ", font = "cybermedium")
dream_job_art2 = pyfiglet.figlet_format(dream_job, font = "univers")

#Format inputted favorite food in a fancy way
favorite_food_art1 = pyfiglet.figlet_format("Your Favorite Food is: ", font = "cybermedium")
favorite_food_art2 = pyfiglet.figlet_format(favorite_food, font = "univers")

#Format inputted favorite color in a fancy way
favorite_color_art1 = pyfiglet.figlet_format("Your Favorite Color is: ", font = "cybermedium")
favorite_color_art2 = pyfiglet.figlet_format(favorite_color, font = "univers")

#Display formatted name in a fancy way and in other color
print("\033[93m{}\033[00m".format(name_art1 + name_art2))

#Display formatted dream job in a fancy way and in other color
print("\033[93m{}\033[00m".format(dream_job_art1 + dream_job_art2))

#Display formatted favorite food in a fancy way and in other color
print("\033[93m{}\033[00m".format(favorite_food_art1 + favorite_food_art2))

#Display formatted favorite color in a fancy way and in other color
print("\033[93m{}\033[00m".format(favorite_color_art1 + favorite_color_art2))