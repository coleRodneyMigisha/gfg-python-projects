from random import choice, randint


def next_guess(prev_guesses, hint):
  next_guess = 0
  while next_guess in prev_guesses:
      guess = []
      for e in hint:
         if e.lower() == 'x':
            guess.append(str(randint(0, 9)))
         else:
            guess.append(str(e))
      next_guess = int("".join(guess))

  return next_guess

def make_hint(num, guess):
   hint = []
   for k in str(num):
      if k in guess:
         hint.append(k)
      else:
         hint.append('x')
   return "".join(hint)
    

print("""
      Welcome to the mastermind game...
      Let's see who the mastermind is;
        so, you're going to think of a  number between 1 and 10000, then I'm going to try and guess
        what number you're thinking of.
        - If i get it in one go, I'm the mastermind automatically
        - If not, you type out the number with 'x' representing the digits i haven't guessed and placing 
        the digits in what i guessed where they are in your number i.e. if your number is 4562 and I guess 
        26, you type xx62 and i will know that 6 and 2 are in you number and it's 4 digits long and we 
        continue like that til i guess your number right
        - once i guess your number, we switch roles and the rules continue as is but in reverse
        - whoever guesses the number in less tries at the end is declared the mastermind!
        - let's start! Think of a number between 1 and 10000
      """)

first_guess = randint(1, 10000)
print(f"Computer: {first_guess}")

comp_chances = 1
check = input("Is it right? (y or n): ")
prev_comp_guesses  = [0]
while check != 'y':
   print("Okayyy...")
   hint = input("A hint?: ")
   
   comp_guess = next_guess(prev_comp_guesses, hint)
   prev_comp_guesses.append(comp_guess)
   print(f"Next guess... computer: {comp_guess}")
   check = input("Is it right? (y or n): ")
   comp_chances += 1

if comp_chances == 1:
   print("Computer is mastermind!")
else:
   print(f"Well, computer guessed in {comp_chances} turns.")
   print("Now, we switch roles")
   comp_num = randint(1, 10000)
   player_guess = input("Your guess: ")
   player_chances = 1
   correct = 'n'
   while correct != 'y':
      print(f"Not correct, hint {make_hint(comp_num, player_guess)}")
      player_guess = input("Your guess: ")
      if player_guess == str(comp_num):
         correct = 'y'
      player_chances += 1
   if player_chances == 1:
      print("You're the mastermind, ooouuuououu!")
   else:
      print(f"Well, you guessed the right number in {player_chances} turns.")
      if player_chances < comp_chances:
         print("You guessed quicker, you're the mastermind! YOU WIN!")
      elif player_chances == comp_chances:
         print(f"You tied, you both used {comp_chances} turns... equally masterminds?")
      else: 
         print("You used more chances than the computer, so, it's the mastermind... you lose!")