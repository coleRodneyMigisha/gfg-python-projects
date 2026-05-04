from random import choice


def winner(play, comp):
    if play.lower() == "rock":
        if comp == "scissors":
            return [play, comp, "win"]
        else:
            return [play, comp, "loss"]
    elif play.lower() == "paper":
        if comp == "rock":
            return [play, comp, "win"]
        else:
            return [play, comp, "loss"]
    elif play.lower() == "scissors":
        if comp == "paper":
            return [play, comp, "win"]
        else:
            return [play, comp, "loss"]
    else:
        return [play, comp, "loss"]
    
def round(rounds):
    wins = 0
    losses = 0
    while rounds > 0:
        player = input("rock, paper, scissors... shoot: ")
        computer = choice([k for k in playable if k != player.lower()])
        if winner(player, computer)[-1] == "win":
            print(f"Computer played {winner(player, computer)[1]}, you won that round...")
            wins += 1
        else: 
            print(f"Computer played {winner(player, computer)[1]}, you lose that one...")
            losses += 1
        rounds -= 1
        if rounds==0 and wins==losses:
            print("You're tied so let's go again")
            rounds += 1
        print(" ")
    if wins > losses:
        print("You win!")
    elif wins < losses:
        print("You lose!")



playable = ["rock", "paper", "scissors"]

print("""
    ROCK, PAPER, SCISSORS
      The rules are simple:
      - Rock beats scissors
      - Paper beats rock
      - Scissors beats paper
      - Any input that's not rock, paper or scissors is recorded as a loss
      So... best out of?
""")
rounds = input("How many rounds do you want to play (2, 3, or ....)?: ")

round(int(rounds))