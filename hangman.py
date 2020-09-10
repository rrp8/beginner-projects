# apologies to myself for the shitty variable names...

print("You have 5 guesses to guess the correct word/phrase, good luck!")
secret_word = input("Enter the secret word: ").upper()
# this list contains the secret word/phrase as normal letters
secret_word_list = []
for letter_secret in secret_word:
    secret_word_list.append(letter_secret)

# this list contains the secret word/phrase as "_" where necessary
not_visible_word_list = []
for letter in secret_word:
    if letter == " " or letter == "!" or letter == "?":
        not_visible_word_list.append(letter)
    else:
        not_visible_word_list.append("_")

# print(not_visible_word_list) -- this was here for testing purposes
# print(secret_word_list)

invalid_guesses = 0  # when it reaches 5, the guesser loses

end_game = False

while end_game is False:
    if invalid_guesses <= 5:
        while True:
            # this should check if only one letter has been typed
            guess_letter = input("Guess a letter: ").upper()
            # this doesn't really work. If the user types more than one letter, 
            # and then types a correct letter it still counts as an error. But I don't care enough to fix it...
            while True:
                if len(guess_letter) == 1:
                    break
                else:
                    guess_letter = input("Guess only one letter: ")

            # this checks the whole list and finds the index of the letter, nevermind how many times the letter is repeated
            letter_index = []
            fake_index = 0
            for letter_search in secret_word_list:
                if letter_search == guess_letter:
                    letter_index.append(fake_index)
                fake_index += 1

            if len(letter_index) >= 1:  # this SHOULD mean that it is a correct guess
                print("Correct guess.")

                # this replaces the "_" with the guess_letter
                loops_num_for_index = 0
                while loops_num_for_index < len(letter_index):
                    not_visible_word_list[letter_index[loops_num_for_index]] = guess_letter
                    loops_num_for_index += 1

                # this changes the printed "_" to acutal letters in a string so it looks nice
                visible_word = ""
                for letter_final in not_visible_word_list:
                    visible_word += letter_final + " "

                print(visible_word)

                if not "_" in visible_word:  # this is achieved when player wins
                    print("Congratulations, you win!")
                    end_game = True

            else:
                print("Incorrect guess.")
                invalid_guesses += 1
            
            # here are all the lists and variables that are cleared before another guess
            letter_index.clear()
            fake_index = 0
            loops_num_for_index = 0

            break
    elif invalid_guesses > 5:
        print("Out of guesses, you lost.")
        end_game = True
        break
