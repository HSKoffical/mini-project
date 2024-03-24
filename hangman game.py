import random

class random_class:
    def __init__(self,list_of_fruit):
        self.list_of_fruit=list_of_fruit
    def random_choice(self):
        x=random.choice(self.list_of_fruit)
        list_of_fruit=[i for i in x]
        return list_of_fruit
fruits=random_class(["banana","apple","mango","orange"])
fruit=fruits.random_choice()
x=len(fruit)
class dict:
    def dict_of_fruit(self):
        d1={}
        for i,j in enumerate(fruit):
            d1[i]=j
        return d1
dict_of_word=dict()
dicts=dict_of_word.dict_of_fruit()

class user_input:
    def input_fun(self):
        inputs="1"
        while True:
            if inputs.isalpha()==True:
                break
            else:
                inputs = input("Enter a letter to guess: ")
        return inputs
word=user_input()
w=word.input_fun()

class game:

    def __init__(self):
        self.s1=" - "*len(fruit)
        self.l1=self.s1.split()
    def w_in_fruit(self):
        if w in fruit:

            for i,j in dicts.items():

                if j==w:
                    w_index=i
            print(w_index)
            self.l1[w_index]=w
            print(" ".join(self.l1))
            fruit.remove(w)
            del[dicts[w_index]]

        else:
            print("No match")
game_on=game()

game_on.w_in_fruit()
flag=0
while flag<x+2:
    if fruit==[]:
        break
    else:
        w=word.input_fun()
        game_on.w_in_fruit()
        flag=flag+1
if fruit==[]:
    print("Congrulation YOU WON")
elif fruit!=[]:
    print("YOU LOSE")