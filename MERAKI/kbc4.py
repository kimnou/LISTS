questions=["how many continents are there?",
"what is the capital of India?",
"what course do they teach at NG?",]
options=[["four","nine","seven","eight"],
["chandigarh","bhopal","chennai","delhi"],
["software engineering","counselling","tourism","agriculture"]]
i=0
solutions=[3,4,1]
while i<len(questions):
    print("Q.",i+1,questions[i])
    j=0
    while j<len(options[i]):
        print("Ans:",j+1,options[i][j])
        j+=1
    lifeline=("without lifeline","with lifeline")
    print("choose if you want lifeline or not")
    print(" 1.without lifeline","\n","2.with lifeline")
    choice=int(input("enter choice:"))
    if choice==1:
        ans=int(input("choose your answer:"))
        if ans==solutions[i]:
            print(" congrats! your answer is correct","\n","move ahead")
        else:
            print(" -wrong answer-","\n","-restart the game-")
            break
    else:
        ans=int(input("choose your answer:"))
        if ans==solutions[i]:
            print(" congrats! your answer is correct","\n","move forward")
        else:
            print(" -wrong answer","\n","-you have a lifeline","\n","-choose answer again-")
            sec_chance=int(input("enter answer:"))
            if sec_chance==solutions[i]:
                print(" congrats! you got the right answer","\n","move ahead")
            else:
                print(" -wrong answer AGAIN-","\n","-lifeline is finished-","\n")
                break
    i+=1




   

