import secrets, time
import pyperclip

letters = list("abcdefghijklmnopqrstuvwxyz")
letters_cap = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
spec_signs = list(".!@?-%/#$")

# this might be a very weird way to control the lenght of the password but so be it...
rand_num_pass_long = secrets.randbelow(11) + secrets.randbelow(11)
if rand_num_pass_long < 10:
    rand_num_pass_long = rand_num_pass_long + (10 - rand_num_pass_long )

current_pass_lett = []
div_inp = rand_num_pass_long / 4

a = 0
while div_inp >= a:
    l = secrets.choice(letters)
    current_pass_lett.append(l)

    cl = secrets.choice(letters_cap)
    current_pass_lett.append(cl)

    n = secrets.choice(numbers)
    current_pass_lett.append(n)

    s = secrets.choice(spec_signs)
    current_pass_lett.append(s)

    a += 1

password = []
while len(current_pass_lett) > 1:
    gen_pass = secrets.choice(current_pass_lett)
    current_pass_lett.remove(gen_pass)
    password.append(gen_pass)

comp_pass = ""
for let in password:
    comp_pass += let

pyperclip.copy(comp_pass)
print("Your password is " + comp_pass + ". The password has been saved in your clipboard.")

# I use this sleep function just in case the window shuts down before the user can see the password
time.sleep(5)
