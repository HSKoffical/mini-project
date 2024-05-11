import os


class student:
    # \n1. Appecentance student
    # \n2. display student
    # \n3. search student
    # \n4. delete student
    # \n5. update student


    def __init__(self):
        self.list=[["A","1","10","90"],["B","2","10","91"],["C","3","10","77"]]
        self.info=["Name","Roll.No","Class","Marks"]

    def Appecentance(self):
            print("Appecentace")
            l1=[]
            name=input("enter the name:: ")
            l1.append(name)
            roll_no=input("enter the roll no:: ")
            l1.append(roll_no)
            classes=input("enter the class:: ")
            l1.append(classes)
            mark=input("enter the mark:: ")
            l1.append(mark)
            self.list.append(l1)
            print("Update sccessfull")
    def display(self):
            print("display")
            for i in self.list:
                for j,k in enumerate(i):
                    print(f" {self.info[j]}:::{k}")
                print("\n")
    def delete(self):
        print("deleting")
        deleting_info=int(input("enter roll no to delete that info:: "))-1
        self.list.pop(deleting_info)
    def search(self):
        print("searching")
        searching_info=int(input("enter roll no to search:: "))-1
        print(self.list[searching_info])
    def update(self):
        print("updating")
        updating_info=int(input("enter roll no to update"))-1
        list_1=self.list[updating_info]
        for i,j in enumerate(self.info):
            x=input(f"enter the {j}:: ")
            list_1[i]=x
        self.list[updating_info]=list_1
    def searching(self):
        print("Searching")
        roll_num=int(input("enter the roll no you want to search:: "))-1
        list_2=self.list[roll_num]
        for i,j in enumerate(list_2):
            print(f"{self.info[i]}::{j}")

main=student()
while True:
    print("What operation do you want\n1. Appecentance student\n2. search student \n3. delete student\n4. update student")
    opition=input("enter your opition:: ")

    if opition == "1":
        main.Appecentance()

        yes_no = input("enter yes for display ")
        if yes_no=="yes":
            main.display()
            again=input("Do you want to perform opretion again(yes/no):: ")
            if again=="yes":
                os.system('cls')

            else:
                break

    if opition == "3":
        main.delete()

        yes_no = input("enter yes for display ")
        if yes_no=="yes":
            main.display()
            again=input("Do you want to perform opretion again(yes/no):: ")
            if again=="yes":
                os.system('cls')

            else:
                break

    if opition == "2":
        main.searching()



    if opition == "4":
        main.update()

        yes_no = input("enter yes for display ")
        if yes_no=="yes":
            main.display()
            again=input("Do you want to perform opretion again(yes/no):: ")
            if again=="yes":
                os.system('cls')

            else:
                break