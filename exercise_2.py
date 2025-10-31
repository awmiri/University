# function for calculate the average
def multipleUserScore (userScore) :
    total = 0
    for score in userScore :
        total += score
    result = total / len(userScore) 
    return result

# get the study count
getTheUsername= input("whats your name?")
getTheUserStudy= int(input("how many study do you have?"))
# our score study list
theScoreList = []

# loop for the get number
for i in range(getTheUserStudy) :
    enterScore = int(input(f"please enter the {i+1} study score: "))
    theScoreList.append(enterScore)
# sort our study score
theScoreList.sort()
# call the func
getTheResult = multipleUserScore(theScoreList)
# show the study result
if getTheResult >= 17 :
    print(f"{getTheUsername} final avrage is equal {getTheResult} and sounds grate 👌")
elif getTheResult <17 and getTheResult >= 15 :
    print(f"{getTheUsername} final avrage is equal {getTheResult} and thats good ")
else :
    print(f"{getTheUsername} final avrage is equal {getTheResult} and you have to more practis")

