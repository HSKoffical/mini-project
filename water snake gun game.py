print("\n\tWelcome to the water snake gun game")
print("\n\t Firstly enter your name")
user_name=input("NAME::")
with open("water", "a") as f:
    f.write("\n\t"+user_name)

def game(var):
    i=0
    j=0
    k=0
    for a in range(var,0,-1):
       try:
          print(f"************remaining time {a} ******************* ")
          print("\n\n\tYou have to choice 1 for water, 2 for snake, and 3 for gun")
          user_input=int(input("\n\n\tType Here:"))

          d1={1:'water',2:'snake',3:'gun'}
          l1=[1,2,3]
          print("\n\t You choice",d1[user_input])

          l1=["water","snake","gun"]
          import random
          x=random.choice(l1)
          print("\n\tcoumpter choice",x)



          if user_input==1 and x=="water":
              print("\n\tuff! same")
              i=i+1
          if user_input==1 and x=="gun":
              print("\n\tyou win")
              j=j+1
          if user_input==1 and x=="snake":
              print("\n\tyou lose")
              k=k+1
          if user_input==2 and x=="snake":
              print("\n\tuff! it is same")
              i=i+1
          if user_input==2 and x=="water":
              print('\n\tyou win')
              j=j+1
          if  user_input==2 and  x=="gun":
              print("\n\tyou lose")
              k=k+1
          if user_input==3 and x=="water":
              print("\n\tyou lose")
              k=k+1
          if user_input==3 and x=="snake":
              print("\n\tyou win")
              j=j+1
          if user_input==3 and x=="gun":
              print("\n\tuff! same")
              i=i+1
       except Exception as e:
          print("\n\tvalueerror please enter 1,2,3")
    with open("water", "a") as f:
        f.write(f"\n\t win {j} time and lose {k} time and equal {i} time\n")
    print("\n\tyou win ",j,"time and lose ",k," time and equal ",i," time")
game(10)


