import random, time
import pyperclip

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z"]
letters_cap = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
    "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
spec_signs = [".", "!", "@", "?", "-"]

try:
    long_inp = int(input("Choose one of these numbers: 8, 16, 24, 32 - "))
except ValueError:
    long_inp = int(input("Please enter a number: "))

current_pass_lett = []
div_inp = long_inp / 4

a = 0
while div_inp >= a:
    l = random.choice(letters)
    current_pass_lett.append(l)

    cl = random.choice(letters_cap)
    current_pass_lett.append(cl)

    n = random.choice(numbers)
    current_pass_lett.append(n)

    s = random.choice(spec_signs)
    current_pass_lett.append(s)

    a += 1

password = []
while len(current_pass_lett) > 1:
    gen_pass = random.choice(current_pass_lett)
    current_pass_lett.remove(gen_pass)
    password.append(gen_pass)

comp_pass = ""
for let in password:
    comp_pass = comp_pass + let

pyperclip.copy(comp_pass)
print("Your password is " + comp_pass + ". The password has been saved in your clipboard.")

time.sleep(5)
