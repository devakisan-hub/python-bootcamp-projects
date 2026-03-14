import random
def deal_card():
    """Reaturn a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and calculates the score based on them."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    """Compares the user's score and the computer's score to determine the winner."""
    if u_score == c_score:
        print("It's a DRAW!")
    elif c_score == 0:
        print("Computer won with a balckjack:(")
    elif u_score == 0:
        print("You Win with a blackjack!")
    elif u_score > 21:
        print("You Lose :(")
    elif c_score > 21:
        print("You Win!")
    elif u_score > c_score:
        print("You Win!")
    else:
        print("You Lose :(")
    return u_score, c_score

def play_game():
    logo = r"""
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_is_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_is_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User cards: {user_cards}, User score: {user_score}")
        print("Computer's first card:", computer_cards[0])
        if user_score == 21 or computer_score == 21 or user_score > 21:
            print("GAME OVER!")
            game_is_over = True
        else:
            hit = input("Type 'y' if u want to hit or 'n' if u want to quit.")
            if hit == 'y':
                user_cards.append(deal_card())
            else:
                print("GAME OVER!")
                game_is_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final draw: {user_cards} , final score: {user_score}")
    print(f"Computer's final draw: {computer_cards} , final score: {computer_score}")
    print(compare(user_score, computer_score))

while  input("Do u want to play another game of blackjack? (y/n) ") == 'y':
    print("\n" * 20)
    play_game()




