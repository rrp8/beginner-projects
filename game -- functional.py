import random
x_score = 0
o_score = 0
end = False


def winning_condition():
    global end
    global o_score
    global x_score
    if grid[1][0] == "  X  |" and grid[4][0] == "  X  |" and grid[7][0] == "  X  |":
        print(x_player + " Wins!")
        x_score += 1
        end = True
        return end
    elif grid[1][1] == "  X  |" and grid[4][1] == "  X  |" and grid[7][1] == "  X  |":
        print(x_player + " Wins!")
        x_score += 1
        end = True
        return end
    elif grid[1][2] == "  X  " and grid[4][2] == "  X  " and grid[7][2] == "  X  ":
        print(x_player + " Wins!")
        x_score += 1
        end = True
        return end
    elif grid[1][0] == "  X  |" and grid[1][1] == "  X  |" and grid[1][2] == "  X  ":
        print(x_player + " Wins!")
        x_score += 1
        end = True
        return end
    elif grid[4][0] == "  X  |" and grid[4][1] == "  X  |" and grid[4][2] == "  X  ":
        print(x_player + " Wins!")
        x_score += 1
        end = True
        return end
    elif grid[7][0] == "  X  |" and grid[7][1] == "  X  |" and grid[7][2] == "  X  ":
        print(x_player + " Wins!")
        x_score += 1
        end = True
        return end
    elif grid[1][0] == "  X  |" and grid[4][1] == "  X  |" and grid[7][2] == "  X  ":
        print(x_player + " Wins!")
        x_score += 1
        end = True
        return end
    elif grid[1][2] == "  X  " and grid[4][1] == "  X  |" and grid[7][0] == "  X  |":
        print(x_player + " Wins!")
        x_score += 1
        end = True
        return end
    elif grid[1][0] == "  O  |" and grid[4][0] == "  O  |" and grid[7][0] == "  O  |":
        print(circle_player + " Wins!")
        o_score += 1
        end = True
        return end
    elif grid[1][1] == "  O  |" and grid[4][1] == "  O  |" and grid[7][1] == "  O  |":
        print(circle_player + " Wins!")
        o_score += 1
        end = True
        return end
    elif grid[1][2] == "  O  " and grid[4][2] == "  O  " and grid[7][2] == "  O  ":
        print(circle_player + " Wins!")
        o_score += 1
        end = True
        return end
    elif grid[1][0] == "  O  |" and grid[1][1] == "  O  |" and grid[1][2] == "  O  ":
        print(circle_player + " Wins!")
        o_score += 1
        end = True
        return end
    elif grid[4][0] == "  O  |" and grid[4][1] == "  O  |" and grid[4][2] == "  O  ":
        print(circle_player + " Wins!")
        o_score += 1
        end = True
        return end
    elif grid[7][0] == "  O  |" and grid[7][1] == "  O  |" and grid[7][2] == "  O  ":
        print(circle_player + " Wins!")
        o_score += 1
        end = True
        return end
    elif grid[1][0] == "  O  |" and grid[4][1] == "  O  |" and grid[7][2] == "  O  ":
        print(circle_player + " Wins!")
        o_score += 1
        end = True
        return end
    elif grid[1][2] == "  O  " and grid[4][1] == "  O  |" and grid[7][0] == "  O  |":
        print(circle_player + " Wins!")
        o_score += 1
        end = True
        return end
    elif grid[1][0] != "     |" and grid[1][1] != "     |" and grid[1][2] != "     " and grid[4][0] != "     |" and \
            grid[4][1] != "     |" and grid[4][2] != "     " and grid[7][0] != "     |" and grid[7][1] != "     |" and \
            grid[7][2] != "     ":
        print("It's a draw, nobody wins.")
        end = True
        return end


grid = [
    ["     |", "     |", "     "],
    ["     |", "     |", "     "],
    ["_____|", "_____|", "_____"],
    ["     |", "     |", "     "],
    ["     |", "     |", "     "],
    ["_____|", "_____|", "_____"],
    ["     |", "     |", "     "],
    ["     |", "     |", "     "],
    ["     |", "     |", "     "],
]


def grid_replacement(x_move, o_move):
    if x_move == "left up":
        if grid[1][0] == "     |":
            grid[1].pop(0)
            grid[1].insert(0, "  X  |")
        elif grid[1][0] != "     |":
            while x_move == "left up":
                x_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(x_move, 0)
    elif x_move == "left middle":
        if grid[4][0] == "     |":
            grid[4].pop(0)
            grid[4].insert(0, "  X  |")
        elif grid[4][0] != "     |":
            while x_move == "left middle":
                x_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(x_move, 0)
    elif x_move == "left down":
        if grid[7][0] == "     |":
            grid[7].pop(0)
            grid[7].insert(0, "  X  |")
        elif grid[7][0] != "     |":
            while x_move == "left down":
                x_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(x_move, 0)
    elif x_move == "center up":
        if grid[1][1] == "     |":
            grid[1].pop(1)
            grid[1].insert(1, "  X  |")
        elif grid[1][1] != "     |":
            while x_move == "center up":
                x_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(x_move, 0)
    elif x_move == "center middle":
        if grid[4][1] == "     |":
            grid[4].pop(1)
            grid[4].insert(1, "  X  |")
        elif grid[4][1] != "     |":
            while x_move == "center middle":
                x_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(x_move, 0)
    elif x_move == "center down":
        if grid[7][1] == "     |":
            grid[7].pop(1)
            grid[7].insert(1, "  X  |")
        elif grid[7][1] != "     |":
            while x_move == "center down":
                x_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(x_move, 0)
    elif x_move == "right up":
        if grid[1][2] == "     ":
            grid[1].pop(2)
            grid[1].insert(2, "  X  ")
        elif grid[1][2] != "     ":
            while x_move == "right up":
                x_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(x_move, 0)
    elif x_move == "right middle":
        if grid[4][2] == "     ":
            grid[4].pop(2)
            grid[4].insert(2, "  X  ")
        elif grid[4][2] != "     ":
            while x_move == "right middle":
                x_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(x_move, 0)
    elif x_move == "right down":
        if grid[7][2] == "     ":
            grid[7].pop(2)
            grid[7].insert(2, "  X  ")
        elif grid[7][2] != "     ":
            while x_move == "right down":
                x_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(x_move, 0)
    elif o_move == "left up":
        if grid[1][0] == "     |":
            grid[1].pop(0)
            grid[1].insert(0, "  O  |")
        elif grid[1][0] != "     |":
            while o_move == "left up":
                o_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(0, o_move)
    elif o_move == "left middle":
        if grid[4][0] == "     |":
            grid[4].pop(0)
            grid[4].insert(0, "  O  |")
        elif grid[4][0] != "     |":
            while o_move == "left middle":
                o_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(0, o_move)
    elif o_move == "left down":
        if grid[7][0] == "     |":
            grid[7].pop(0)
            grid[7].insert(0, "  O  |")
        elif grid[7][0] != "     |":
            while o_move == "left down":
                o_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(0, o_move)
    elif o_move == "center up":
        if grid[1][1] == "     |":
            grid[1].pop(1)
            grid[1].insert(1, "  O  |")
        elif grid[1][1] != "     |":
            while o_move == "center up":
                o_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(0, o_move)
    elif o_move == "center middle":
        if grid[4][1] == "     |":
            grid[4].pop(1)
            grid[4].insert(1, "  O  |")
        elif grid[4][1] != "     |":
            while o_move == "center middle":
                o_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(0, o_move)
    elif o_move == "center down":
        if grid[7][1] == "     |":
            grid[7].pop(1)
            grid[7].insert(1, "  O  |")
        elif grid[7][1] != "     |":
            while o_move == "  X  |":
                o_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(0, o_move)
    elif o_move == "right up":
        if grid[1][2] == "     ":
            grid[1].pop(2)
            grid[1].insert(2, "  O  ")
        elif grid[1][2] != "     ":
            while o_move == "right up":
                o_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(0, o_move)
    elif o_move == "right middle":
        if grid[4][2] == "     ":
            grid[4].pop(2)
            grid[4].insert(2, "  O  ")
        elif grid[4][2] != "     ":
            while o_move == "right middle":
                o_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(0, o_move)
    elif o_move == "right down":
        if grid[7][2] == "     ":
            grid[7].pop(2)
            grid[7].insert(2, "  O  ")
        elif grid[7][2] != "     ":
            while o_move == "right down":
                o_move = input("That spot is already occupied, choose another spot: ")
                grid_replacement(0, o_move)


def clean_grid():
    grid[1].pop(0)
    grid[1].insert(0, "     |")
    grid[1].pop(1)
    grid[1].insert(1, "     |")
    grid[1].pop(2)
    grid[1].insert(2, "     ")
    grid[4].pop(0)
    grid[4].insert(0, "     |")
    grid[4].pop(1)
    grid[4].insert(1, "     |")
    grid[4].pop(2)
    grid[4].insert(2, "     ")
    grid[7].pop(0)
    grid[7].insert(0, "     |")
    grid[7].pop(1)
    grid[7].insert(1, "     |")
    grid[7].pop(2)
    grid[7].insert(2, "     ")


def scores():
    if x_score > o_score:
        print(x_player + " wins, " + str(x_score) + " to " + str(o_score) + ". Congratulations, and thank you for "
                                                                            "playing.")
    elif o_score > x_score:
        print(circle_player + " wins, " + str(o_score) + " to " + str(x_score) + ". Congratulations, and thank you for "
                                                                                 "playing.")
    elif o_score == x_score:
        print("The final score is " + str(o_score) + " to " + str(x_score) + ". It's a tie.")


def grid_list():
    for line in grid:
        print("".join(map(str, line)))


def turns():
    global end
    starting_player = random.choice(players)
    print(starting_player + " will start the match.")
    if starting_player == circle_player:
        while True:
            move_o = input(circle_player + ", where would you like to place your \"O\"? ").lower()
            while True:
                if move_o == "left up" or move_o == "left middle" or move_o == "left down" or move_o == "center up"\
                        or move_o == "center middle" or move_o == "center down" or move_o == "right up" or\
                        move_o == "right middle" or move_o == "right down":
                    break
                else:
                    move_o = input("Invalid position, please try again: ")
            grid_replacement(0, move_o)
            grid_list()
            winning_condition()
            if end is True:
                end = False
                break
            move_x = input(x_player + ", where would you like to place your \"X\"? ").lower()
            while True:
                if move_x == "left up" or move_x == "left middle" or move_x == "left down" or move_x == "center up"\
                        or move_x == "center middle" or move_x == "center down" or move_x == "right up" or move_x \
                        == "right middle" or move_x == "right down":
                    break
                else:
                    move_x = input("Invalid position, please try again: ")
            grid_replacement(move_x, 0)
            grid_list()
            winning_condition()
            if end is True:
                end = False
                break
    elif starting_player == x_player:
        while True:
            move_x = input(x_player + ", where would you like to place your \"X\"? ").lower()
            while True:
                if move_x == "left up" or move_x == "left middle" or move_x == "left down" or move_x == "center up"\
                        or move_x == "center middle" or move_x == "center down" or move_x == "right up" or move_x \
                        == "right middle" or move_x == "right down":
                    break
                else:
                    move_x = input("Invalid position, please try again: ")
            grid_replacement(move_x, 0)
            grid_list()
            winning_condition()
            if end is True:
                end = False
                break
            move_o = input(circle_player + ", where would you like to place your \"O\"? ").lower()
            while True:
                if move_o == "left up" or move_o == "left middle" or move_o == "left down" or move_o == "center up"\
                        or move_o == "center middle" or move_o == "center down" or move_o == "right up" or move_o \
                        == "right middle" or move_o == "right down":
                    break
                else:
                    move_o = input("Invalid position, please try again: ")
            grid_replacement(0, move_o)
            grid_list()
            winning_condition()
            if end is True:
                end = False
                break


def playing():
    grid_list()
    turns()
    clean_grid()


def free_play():
    c = True
    playing()
    decision = input("Do you want to play again? ").lower()
    while c is True:
        if decision == "yes":
            while decision == "yes":
                playing()
                decision = input("Do you want to play again? ").lower()
                if decision == "no":
                    scores()
                    c = False
        elif decision == "no":
            scores()
            c = False
        else:
            while decision != "yes" or decision != "no":
                decision = input("Please answer with a simple \"yes\" or \"no\": ")


def best_of():
    try:
        of = int(input("Best of "))
        while True:
            if (of % 2) != 0:
                matches_of = 0
                while True:
                    playing()
                    matches_of += 1
                    if matches_of == of:
                        scores()
                        break
            elif (of % 2) == 0:
                of = int(input("Please enter an odd number: "))
    except ValueError:
        print("Invalid number, the game will shut down.")


def fist_to():
    try:
        to = int(input("To how many points do you want to play? "))
        while True:
            playing()
            if x_score == to or o_score == to:
                scores()
                break
    except ValueError:
        print("Invalid number, the game will shut down.")


circle_player = input("Insert name of Circle Player: ")
x_player = input("Insert name of X Player: ")
players = [circle_player, x_player]
match = input("What type of match would you like to play? The choices are: \"Free play\",\"Best of\", and \"First to\":"
              " ").lower()
while match == "free play" or "best of" or "first to":
    if match == "free play":
        free_play()
        break
    elif match == "best of":
        best_of()
        break
    elif match == "first to":
        fist_to()
        break
    else:
        match = input("Wrong command. What type of match would you like to play? ").lower()
