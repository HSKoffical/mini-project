q1="\nwhich is the biggest continent in the world \n a.North America \t b.Asia \n c.Africa \t d.Austalia"
q2="\nWhich is the logest river in the world? \n a.Great Ganga \t b.Nile \n c.Amazon \t d.Niger"
q3="\nWhich is the lagest ocean in the world? \n a.Indian ocean \t b.Pacific Ocean \n c.Artic Ocean \t d.Atlantic Ocean"
q4="\nWhich is the india first super computer? \n a.Param8000 \t b.param800000 \n c.param800 \t d.param8"
question_ans_list=[q1,q2,q3,q4]
dict_list=["q1","q2","q3","q4"]
answer_dict={"q1":"b","q2":"b","q3":"b","q4":"a"}
answer_dict2={"q1":"Asia","q2":"Niger","q3":"Pacific ocean","q4":"Param8000"}
flag=0
price=0
question_price=500
for i in question_ans_list:
    print(f"\nThis question is for {question_price}",i)
    user_answer=input("ans::")

    if user_answer==answer_dict[dict_list[flag]]:
        print("\nCorrect Answer")
        price=price+question_price
        print("Total amount you won::",price)
        question_price+=1000
    else:
        print("\nWrong answer The corret answer is:",answer_dict2[dict_list[flag]])
        break
    flag+=1
print("Total amount you won::",price)