import random
list_of_fruit=words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
food=random.choice(list_of_fruit)
list_of_hangman= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
flag=0
list_of_show=[i for i in "".join([len(food)*"-"])]
def main():
    global flag
    user_input=input("Enter the word:: ")
    if user_input in food:
        for i,j in enumerate(food):
            if user_input==j:
                list_of_show[i]=j
        print(" ".join(list_of_show)+"\n")
        print("\n" + str(list_of_hangman[flag]))
    else:
            print(f"you guess a letter is {user_input} it is not in word")
            print("\n"+str(list_of_hangman[flag+1]))

            flag=flag+1
while True:
    if flag==len(list_of_hangman)-1:
        if food != "".join(list_of_show):
            print("you lose")
            break
    elif food=="".join(list_of_show):
        print("You win")
        break
    else:
        main()

