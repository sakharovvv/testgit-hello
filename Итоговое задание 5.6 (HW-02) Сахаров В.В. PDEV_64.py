field = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]
victory_combinations = [[0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8],
                        [0, 3, 6],
                        [1, 4, 7],
                        [2, 5, 8],
                        [0, 4, 8],
                        [2, 4, 6]]
def show_field():
    print(field[0], end= " ")
    print(field[1], end= " ")
    print(field[2])
    print(field[3], end= " ")
    print(field[4], end= " ")
    print(field[5])
    print(field[6], end= " ")
    print(field[7], end= " ")
    print(field[8])
def choice(step, symbol):
    index = field.index(step)
    field[index] = symbol
def victory_conditions():
    victory = ""
    for i in victory_combinations:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            victory = "X"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            victory = "O"
    return victory
game_over = False
player = True
while game_over == False:
    show_field()
    if player == True:
        symbol = "X"
        step = int(input("Ход игрока 1: "))
    else:
        symbol = "O"
        step = int(input("Ход игрока 2: "))
    choice(step, symbol)
    victory = victory_conditions()
    if victory != "":
        game_over = True
    else:
        game_over = False

    player = not(player)
show_field()
print("Победил", victory)