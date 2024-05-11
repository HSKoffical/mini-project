class vcm:
    def __init__(self):
        self.dict={"sugar":1000,"milk":500,"water":500,"coffea":100}
        self.amount=0
    def tea(self):

        tea_dict = {"sugar": 100, "milk": 50, "water": 50}
        tea_ind = [j for i, j in self.dict.items() if i in tea_dict]
        if 0 in tea_ind:
            for i,j in self.dict.items():
                if j==0:
                    print(f"Sorry {i} is over now")
                    return

        quantity=int(input("How many tea do you want:: "))
        print("The tea is for 25 Rs")
        total_amount=quantity*25
        amount=int(input(f"Enter amount to pay {total_amount}:: "))
        if amount==total_amount:
                    for i,j in tea_dict.items():


                        if self.dict[i]<=0:



                            for i, j in self.dict.items():
                                    if j <= 0:
                                        print(f"Sorry {i} is limited")
                                        return False
                        self.dict[i] = self.dict[i] - (j * quantity)
                    self.amount=self.amount+amount


                    print("Pay sccessfull")
        if amount!=total_amount:
                    print("fail")
    def coffea(self):
        coffea_dict={"sugar":100,"milk":50,"water":50,"coffea":20}
        coffea_ind=[j for i,j in self.dict.items() if i in coffea_dict]
        if 0 in coffea_ind:
            for i,j in self.dict.items():
                if j==0:
                    print(f"Sorry {i} is over now")
                    return

        qunatity=int(input("How many coffea do you want:: "))
        print("The coffea is for 50 Rs")
        total_amount=qunatity*50
        amount=int(input(f"Enter amount to pay {total_amount}:: "))
        if amount==total_amount:
                    for i,j in coffea_dict.items():
                        if self.dict[i] <= 0:

                            for i, j in self.dict.items():
                                if j <= 0:
                                    print(f"Sorry {i} is limited")
                                    return False
                        self.dict[i]=self.dict[i]-(j*qunatity)

                    self.amount=self.amount+amount


                    print("Pay sccessfull")
        if amount!=total_amount:
                    print("fail")



    def milk_shake(self):
        milk_shake_dict = {"sugar": 100, "milk": 50}
        milk_shake_ind = [j for i, j in self.dict.items() if i in milk_shake_dict]
        if 0 in milk_shake_dict:
            for i, j in self.dict.items():
                if j == 0:
                    print(f"Sorry {i} is over now")
                    return

        qunatity = int(input("How many milk shake do you want:: "))
        print("The milk shake is for 40 Rs")
        total_amount = qunatity * 40
        amount = int(input(f"Enter amount to pay {total_amount}:: "))
        if amount == total_amount:
            for i, j in milk_shake_dict.items():
                if self.dict[i] <= 0:

                    for i, j in self.dict.items():
                        if j <= 0:
                            print(f"Sorry {i} is limited")
                            return False
                self.dict[i] = self.dict[i] - (j * qunatity)

            self.amount = self.amount + amount

            print("Pay sccessfull")
        if amount != total_amount:
            print("fail")

    def report(self):
        for i, j in self.dict.items():
            print(f"{i}::{j}")
        print(f"amount::{self.amount}")


x=vcm()
while True:
    Order = input("What you want to order(tea/milk shake/coffea):: ")
    if Order=="tea":
        x.tea()
    if Order=="report":
        x.report()
    if Order=="coffea":
        x.coffea()
    if Order=="milk shake":
        x.milk_shake()
    if Order=="off":
        break
