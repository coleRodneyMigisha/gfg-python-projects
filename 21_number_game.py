from random import randint


def computers_turn(last_number):
    length = randint(1, 3)
    move = []
    if length == 1:
        move.append(str(int(last_number)+1))
    else:
        for k in range(int(last_number)+1, int(last_number)+length):
            move.append(str(k))
    return move

print("""
 21 NUMBER GAME
           
 RULES:
      - Player or computer enter 1, 2 or 3 numbers 
      - These numbers must follow each other in terms of counting 
      - No skipping any number
      - Who ever lands on the number 21 loses
      - Numbers must be separated by a space
      - As a demonstration, it will look something like this;
        - You: 1 2 3
        - Computer: 4
        - You: 5 
        - Computer: 6 7
        .
        .
        .
        -Computer: 20 21 22
        Winner: You
""")

players = {
    1: "You",
    2: "Computer"
}


print(" ")
print("You go first...")
turn = 1
move = ""
while '21' not in move:
    if turn == 1:
        move = input(f"{players[turn]}: ").split(" ")
        turn = 2
    else:
        if move[-1] == "":
            move = computers_turn(move[-2])
        else:
            move = computers_turn(move[-1])
        print(f"{players[turn]}: {" ".join(move)}")
        turn = 1
print(f"""
    Winner : {players[turn]}
""")