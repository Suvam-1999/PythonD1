#question ask  correct q and a  check\


def user_ask(question,answer):

    ask = input(question + "")

    if(answer == ask):
        print ("Correct")
        return 1
    else:
        print ("Incorrect")
        return 0


quiz = [
    ("What is 2 - 2 : ", "0"),
    ("What is capital of Nepal : ", "Kathmandu")
]


score = 0


for q,a in quiz:
    score+= user_ask(q,a)
    
print ( f"Your score is : , {score}/{len(quiz)}")
