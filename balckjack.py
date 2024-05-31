import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def random_shuffle():
    random.shuffle(cards)
def hit_stand():
    user_choice=input("\nEnter h for hit and s for stand:: ")
    return user_choice
def hit():
    extra_card=random.choice(cards)
    player1.append(extra_card)
    print(f"\nPlayer card after hit::{player1},sum:: {sum(player1)}")
    extra_card_coumputer=random.choice(cards)
    player2.append(extra_card_coumputer)

def Ace():
    for i,j in enumerate(player1):
        if j==11:
            player1[i]=1
            break
def winner():
    player1_sum=sum(player1)
    player2_sum=sum(player2)
    print(f"Coumputer card::{player2}")
    print(f"Player card:: {player1}")
    print(f"\n\nCoumputer total sum {player2_sum}")
    print(f"player 1 total sum {player1_sum}\n\n")


    if player1_sum>21:

            print("Computer win\n\n")
            # print("Player lose\n\n")
    elif player2_sum>21:
        print("\n\n Player win")
    elif player1_sum<=21:
        if player1_sum<player2_sum:
            print("The winner is computer\n\n")
            # print("Player lose\n\n")
        if player2_sum<player1_sum:
            print("The winner is player\n\n")
            # print("coumputer lose\n\n")
        if player1_sum==player2_sum:
            print("Draw\n\n")
while True:
    print("Player 2 is Computer")
    user_choice = input("Do you want to play the 21 number game? (Yes / No)\n> ").lower()
    if user_choice=="yes":
        random_shuffle()
        player1 = random.choices(cards, k=2)
        player2 = random.choices(cards, k=2)
        print(f"Computer card:: [{player2[0]},?]")
        print(f"Player card:: {player1} sum::{sum(player1)}")
        x = hit_stand()
        if x=="h":
            hit()
        if 11 in player1:
            Ace_value = input("\nDo you want to change value of ace(yes/no):: ")
            if Ace_value == "yes":
                Ace()
        winner()
    else:
        print("Thank you")
        break