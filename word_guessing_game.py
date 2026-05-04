from random import choice


words = [
    'four', 'word', 'fire', 'road', 'wash', 'love', 'team', 'code', 'wire', 'rain', 'bread', 'fifth', 
    'again', 'apple', 'chore', 'fixed', 'kudos', 'space', 'chose', 'power', 'intern', 'praise', 'python', 
    'friend', 'charge', 'bought', 'silent', 'xiaomi', 'hotdog', 'online'
    ]


def check_guess(guess, word):
    chances = len(word)+1
    while chances > 0:
        if guess == word:
            chances = 1
        else:
            in_word = []
            for ch in range(len(guess)):
                if guess[ch] in word:
                    in_word.append(guess[ch])
            if len(in_word) == 0:
                print(f"Not quite, bud!")
                guess = input("  guess again: ")
            elif len(in_word) == 1:
                print(f"Not quite the word, but '{in_word[0]}' is in the word.")
                guess = input("  guess again: ")
            else:
                print(f"Not quite the word, but {in_word} are in the word.")
                guess = input("  guess again: ")
        chances -= 1
    if guess == word:
        print("Attaboy! You got it.")
    else:
        print(f"Awww, man! The word was {word}, better luck next time!")


word = choice(words)

print("Guess a word,")
guess = (input(f"  any word! (that has {len(word)}-letters), you have {len(word)+1} chances: "))

check_guess(guess, word)