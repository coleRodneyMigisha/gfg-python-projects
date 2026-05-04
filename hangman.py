from random import choice


words = [
    'four', 'word', 'fire', 'road', 'wash', 'love', 'team', 'code', 'wire', 'rain', 'bread', 'fifth', 
    'again', 'apple', 'chore', 'fixed', 'kudos', 'space', 'chose', 'power', 'intern', 'praise', 'python', 
    'friend', 'charge', 'bought', 'silent', 'xiaomi', 'hotdog', 'online'
    ]


def make_hint(letter, word, hint):
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                hint[i] = word[i]
    


def check_guess(guess, word):
    chances = 6
    hint = []
    for j in range(len(word)):
        hint.append("_")
    hung_man = {
        7: """
            You freed him!
                O   
              | | |  
               | |  
            """,
        5: """
                 ___
                |   |
                O   |
                    |
                    |
            """,
        4: """
                 ___
                |   |
                O   |
                |   |
                    |
            """,
        3: """
                 ___
                |   |
                O   |
              | |   |
                    |
            """,
        2: """
                 ___
                |   |
                O   |
              | | | |
                    |
            """,
        1: """
                 ___
                |   |
                O   |
              | | | |
               |    |
            """,
        0: f"""
                 ___
                |   |
                O   |
              | | | |
               | |  |
               he's dead
               the word was {word}.
            """
    }
    while chances > 1 and chances < 7:
        if guess == word:
            chances = 8
        else:
            if len(guess) == 1:
                make_hint(guess, word, hint)
                print("".join(hint))
                chances -= 1
                print(hung_man[chances])
                guess = input("  guess again: ")
            else:
                for ch in guess:
                    make_hint(ch, word, hint)
                print("".join(hint))
                chances -= 1
                print(hung_man[chances])
                guess = input("  guess again: ")
    chances -= 1
    print(hung_man[chances])
            




print("___HANGMANNNN!___")
word = choice(words)
print(f"You have 6 chances before this dude is hung... Go!")
print("""
     ___
    |   |
        |
        |
        |
""")
print("_"*len(word))

guess = input("Guess a letter or the word: ")
check_guess(guess, word)