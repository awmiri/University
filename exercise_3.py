getUserNumber = int(input(" how many student do you have ? "))

student =[]

for i in range(getUserNumber):
    studentName = input(f" enter student {i +1} name :")
    countOfStudentCourse = int(input(f"student {i+1} how many study have ? "))
    corseScore=[]
    for j in range(countOfStudentCourse):
        score = int(input(f"enter score {j+1} for student {i+1} : "))
        corseScore.append(score)

    studentColection = {
        'userId': i +1 ,
        'name':studentName,
        'scores':corseScore
    }
    student.append(studentColection)

def studentGpa(user):
    total = sum(user['scores'])

    gpa = total / len(user['scores'])

    Result = None

    if gpa <=20 and gpa>=17 :
        Result = "excellent"
    elif  gpa < 17 and gpa>=15:
        Result = "not bad"
    else :
        Result = "awful"



    print(f"{user['name']} have the {gpa} GPA and thats {Result}")



for user in student :
    studentGpa(user)