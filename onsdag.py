#!/usr/bin/env python3

import random # Det här importerar modulen random

foo = "Det här är en string"
bar = 98 # Det här är en integer
foobar = 0.2 # Det här är en float

print(foo, bar) # Printar ut värdet av variablern foo och bar

foo_bar = str(bar) # Det här konverterar bar/98 till en string

print(foo_bar)

print(chr(98)) # Det här konverterar integer till en unicode karaktär
print(ord("a")) # Det här konverterar en unicode karaktär till en integer

example_list = ["apples", "bananas", "cloudberry"]

for item in example_list:
    if item == "apples":
        print("This is an apple")
    elif item == "bananas":
        random_number = random.randint(0, 4) # slumpar en siffra mellan 0 - 4 
        print(random_number)
    else:
        print("Cloudberry is not a fruit")
