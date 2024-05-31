import replit
game_dict={}
def inputs(name,bidding):
    game_dict[name]=bidding
def game():
    sortded_dict=sorted(game_dict,key=lambda x:x[1],reverse=True)
    print(f"The winner is {sortded_dict[-1]} with bidding {game_dict[sortded_dict[-1]]} ")
while True:
    inputs(input("Enter name:: "), int(input("Enter bidding:: $")))
    yes_no=input("do you want to add name(y/n):: ")
    if yes_no=="y":
        replit.clear()
    if yes_no=="n":
        game()
        break
