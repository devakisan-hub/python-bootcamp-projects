import random
logo = r"""
 ________  ___  ___  _______   ________   ________           _________  ___  ___  _______           ________   ___  ___  _____ ______   ________  _______   ________     
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\         |\___   ___\\  \|\  \|\  ___ \         |\   ___  \|\  \|\  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \    
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_        \|___ \  \_\ \  \\\  \ \   __/|        \ \  \\ \  \ \  \\\  \ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \   
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \            \ \  \ \ \   __  \ \  \_|/__       \ \  \\ \  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \            \ \  \ \ \  \ \  \ \  \_|\ \       \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \            \ \__\ \ \__\ \__\ \_______\       \ \__\\ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\ 
    \|_______|\|_______|\|_______|\_________\\_________\            \|__|  \|__|\|__|\|_______|        \|__| \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|
                                 \|_________\|_________|                                                                                                                 
                         
"""
print(logo)
print("Welcome to the Number guessing game!!")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
print("I'm thinking of a number between 1 and 100.")
num = random.randint(1, 100)
attempts = 0
game_over = False
def game():
    global attempts
    global game_over
    while not game_over:
        guess = int(input("Make a guess:"))
        print(f"You have {attempts-1} attempts remaining to guess the number.")
        if guess != num:
            attempts -= 1
        if attempts == 0:
            print("You've run out of guesses. You lose!")
            game_over = True
        else:
            if guess > num:
                print("Too High!\nGuess again.")
            elif guess < num:
                print("Too low!\nGuess again.")
            elif guess == num:
                print(f"You got it!. The answer was {num}.")
                game_over = True
            else:
                print("Enter a valid guess.")

if difficulty == "easy":
    print("You've got 10 attempts to guess the number.")
    attempts = 10
    game()
elif difficulty == "hard":
    print("You've got 5 attempts to guess the number.")
    attempts = 5
    game()
else:
    print("Enter a valid difficulty.")
