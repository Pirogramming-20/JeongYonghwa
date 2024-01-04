# solution 골자 설명(24.01.05 solved by YonghwaJeong)

# stdDict, stdGradeDict 두 개의 딕셔너리를 전역으로 선언 및 사용하여 구현
# stdDict에 있는 학생들은 Grading이 완료되면 stdGradeDict에 새롭게 등록되며, stdDict에서 삭제된다
# 양 딕셔너리의 상태 차이를 이용해 각종 예외를 처리한다
# 입력 예외 처리에 isdigit을 사용하여, 양의 정수 이외의 모든 score 입력을 reject함

def Menu1(stdDict : dict, name, mid, final):
    stdDict[name] = [mid, final]

def Menu2(stdDict : dict, stdGradeDict : dict):
    for key in stdDict:
        grade = ''
        scores = stdDict[key]
        average = sum(scores)/2
        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B'
        elif average >= 70:
            grade = 'C'
        else:
            grade = 'D'
        scores.append(grade)
        stdGradeDict[key] = scores
        # [mid, final, grade] 순으로 저장

    stdDict.clear()

def Menu3(stdGradeDict: dict):
    print('-'*25)
    print("Name     mid final Grade")
    print('-'*25)
    for key in stdGradeDict:
        info = stdGradeDict[key]
        print(f"{key.ljust(8)} {str(info[0]).ljust(4)} {str(info[1]).ljust(6)} {info[2]}")

def Menu4(name, stdDict, stdGradeDict):
    
    if name in stdDict:
        del stdDict[name]
    elif name in stdGradeDict:
        del stdGradeDict[name]

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

stdDict = {}
stdGradeDict = {}

while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        
        infoList = input("Enter name mid-score final-score : ").split()

        # input 값 양식 검사
        if len(infoList) != 3:
            print("Number of input is not proper")
            continue

        # 중복 검사
        if infoList[0] in stdDict or infoList[0] in stdGradeDict:
            print("Student info already exists")
            continue
        
        # 입력이 문자열로 들어오는 경우, 음의 정수 입력이 들어오는 경우, float로 들어오는 경우가 모두 해당
        if (not infoList[1].isdigit() or not infoList[2].isdigit()):
            print("There are invalid input values")
            continue
        
        mid = int(infoList[1])
        final = int(infoList[2])

        name = infoList[0]
        Menu1(stdDict, name, mid, final)

    elif choice == "2" :

        # grading이 안된 학생이 없는 상태
        if not len(stdDict):
            print("No student to grade")
            continue

        print("Grading to all students.")
        Menu2(stdDict, stdGradeDict)

    elif choice == "3" :

        # stdDict에 정보가 있음 => 모든 학생에 대한 grading이 되기 전임
        if len(stdDict):
            print("Some student did not receive the grades.")
            continue
        
        # stdGradeDict에 정보가 없음 => 어떤 학생도 아직 grading 되지 않음 / 혹은 삭제됨
        if not len(stdGradeDict):
            print("No student to print grade information")
            continue    

        Menu3(stdGradeDict)

    elif choice == "4" :

        # 양쪽 딕셔너리가 모두 빈 상태 => 등록된 학생이 없음
        if not len(stdGradeDict) and not len(stdDict):
            print("No student to Delete")  
            continue

        name = input("Enter student name to delete : ")

        # 둘중 하나에 있는 경우 => Grading 전/후와 상관없이 일단 학생 정보가 있음
        if name in stdDict or name in stdGradeDict:
            Menu4(name, stdDict, stdGradeDict)
            print(f"{name}'s information is deleted.")
        else:
            # 매칭되는 이름이 없음
            print("Not exist name!")

    elif choice == "5" :
        print("Exit Program")
        break

    else :
        print("Wrong number. Choose again.")