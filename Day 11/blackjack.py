from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21:
        return 1

def scores(hands):
    if sum(hands) > 21:
        if 11 in hands:
            hands.remove(11)
            hands.append(1)
    return sum(hands)

print("Game of blackjack")

while True:  # Main game loop for starting a new game
    dealer = []
    player = []
    round = 1
    dealer.append(deal_card())
    dealer.append(deal_card())
    player.append(deal_card())
    player.append(deal_card())

    while round:
        print(f"Round {round}")
        print(f"Dealer's cards: {dealer[0]}")
        print(f"Player's cards: {player}")

        scoreD = scores(dealer)
        scoreP = scores(player)

        if scoreD == 21:
            print("Dealer wins")
            break
        if scoreP == 21:
            print("Player wins")
            break
        if scoreD == scoreP:
            print("Draw")
            break
        if scoreD > 21:
            print("Dealer busts")
            break
        if scoreP > 21:
            print("Player busts")
            break

        if scoreD < 21 and scoreP < 21:
            choice = input("Do you want to hit or stand? ").lower()
            if choice == "hit":
                player.append(deal_card())
            elif choice == "stand":
                while scoreD < 17:
                    dealer.append(deal_card())
                    scoreD = scores(dealer)
                if scoreD > 21:
                    print("Dealer busts")
                    print(dealer)
                    break
                if scoreD >= 17:
                    if scoreD > scoreP:
                        print("Dealer wins")
                        print(dealer)
                        break
                    elif scoreD < scoreP:
                        print("Player wins")
                        print(player)
                        break
                    else:
                        print("Draw")
                        break
        round += 1

    
    cont = input("New game? (yes/no): ").lower()
    if cont == "yes":
        clear()  
        continue
    elif cont == "no":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Exiting game.")
        break
