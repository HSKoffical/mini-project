import random
num=random.randint(100,10000)
num=str(num)

print("The num have",len(num)*" X"+" length")
outer_flag=1
def main_fun():
    n=input("Guess the number :: ")
    global outer_flag
    if n==num:
        print(f"Great! You guessed the number in just {outer_flag} try! You're a Mastermind!")
        return True

    else:
        sum=""
        inner_flag=0
        for i in range(len(num)):
            x="X"
            if num[i]==n[i]:
                x=num[i]
                sum=sum+" "+x
                inner_flag=inner_flag+1
            else:
                sum=sum+" "+x
        print(f"Not quite the number. But you did get {inner_flag} digit(s) correct! Also these numbers in your input were correct.\n {sum}")
    outer_flag = outer_flag + 1

s=main_fun()
while s!=True:
    choice=input("Do you want to guess number again (yes/no):: ")
    if choice=="yes":
        main_fun()
    else:
        break
