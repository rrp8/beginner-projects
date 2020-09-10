import random
import pyperclip
import time

phrase = input("Write your phrase: ")
ready = ""
num = random.randint(0, 1)

for letter in phrase:
    if letter == " ":
        ready += letter
    elif (num % 2) != 0:
        ready += letter.lower()
        num += 1
    elif (num % 2) == 0:
        ready += letter.upper()
        num += 1

pyperclip.copy(ready)
print("\"" + ready + "\" has been pasted to your clipboard.")
time.sleep(7)  # this is only so the user can see what the phrase looks like

# I just want to say that I hate my life, it took me more than one hour to finish this piece of shit script...
