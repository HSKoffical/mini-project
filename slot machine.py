import random
deposite=int(input("Enter you dposite?:: "))
print(f"Your deposite is {deposite}")
slot_machine={1:"A",2:"B",3:"A",4:"B"}
win_amount=0
l1=[]
def play_or_not():
    play_or_not = input("Press yes to play or q for quit:: ")
    return play_or_not

def spin():

    for i in range(9):
        num=random.randint(1,4)
        l1.append(slot_machine[num])


def display():
    print(f"{l1[0]} | {l1[1]} | {l1[2]}")
    print(f"{l1[3]} | {l1[4]} | {l1[5]}")
    print(f"{l1[6]} | {l1[7]} | {l1[8]}")


def compare():
    flag=0
    for i in slot_machine.values():
        if l1[0]==l1[1]==l1[2]==i:
            flag+=1
            break
    for i in slot_machine.values():
        if l1[3]==l1[4]==l1[5]==i:
            flag+=1
            break
    for i in slot_machine.values():
        if l1[6]==l1[7]==l1[8]==i:
            flag+=1

            break
    return flag


def bets_on_line():
    while True:
        bet_on_lines = int(input("Enter the number of line you bet(1-3):: "))
        if int(bet_on_lines)<=3 and int(bet_on_lines)>=1:
            return bet_on_lines

def betting():
    global deposite
    while True:

            betting_amt = int(input("Enter the number of bet on each line:: "))
            if deposite > 0:
                if lines==0:
                    normal_amount=bets_line * betting_amt
                    deposite=deposite-normal_amount
                    return betting_amt
                return betting_amt
            else:
                print("Deposite is over")
                return betting_amt



def winlines():
    if same==bets_line:
        return same
    if same < bets_line:
        return same
    if same > bets_line:
        return bets_line



def amount_cal():
    global deposite
    if lines>0:
        win_amount=2*(lines*amount)
        deposite=deposite+win_amount
        print("You have win",win_amount)
        print("Total amount is ",deposite)
    if lines==0:
        print("You have lose",amount*bets_line)
        print("Total amount is",deposite)
while True:
    x=play_or_not()
    if x=="yes":
        spin()

        same = compare()
        bets_line = bets_on_line()
        lines = winlines()
        amount = betting()

        display()
        l1.clear()
        amount_cal()
    if x=="q":
        break