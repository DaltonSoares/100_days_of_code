#!/usr/bin/env python3

"""Everyone loves a good story!

Well, you're going to create your own adventure story that places your user in
the role of the main character and we'll even customize the story to suit their
interests.

Welcome to your adventure simulator. I am going to ask you a bunch of questions
and then create an epic story with you as the star!

What is your name?
What is your worst enemy’s name?
What is your superpower?
Where do you live?
What is your favorite food?

Hello {name}! Your ability to {superpower} will make sure you never have to look at {worst enemy’s name} again. Go eat {your favorite food} as you walk down the streets of {where you live} and use {superpower} for good and not evil!
"""

name = input("What is your name?")
enemy = input("What is your worst enemy's name?")
superpower = input("What is your superpower?")
place = input("Where do you live?")
favorite_food = input("What is your favorite food?")

print("Hello", name,"!", "Your hability to", '\033[31m',superpower,'\033[0m', "will make sure you" 
" never have to look at", enemy, "again. Go eat you favorite food", 
favorite_food, "as you walk down the streets of", place, "and use", superpower,
"for good and not evil!")