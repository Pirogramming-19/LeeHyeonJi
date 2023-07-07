##############  menu 1
def Menu1(name, mid, final) :
    students[name] = [mid, final]

##############  menu 2
def Menu2() :
    for scoreAr in students.values():
        if len(scoreAr) == 2:
            avg = sum(scoreAr) / 2
            if avg >= 90:
                scoreAr.append('A')
            elif avg >= 80:
                scoreAr.append('B')
            elif avg >= 70:
                scoreAr.append('C')
            else:
                scoreAr.append('D')

##############  menu 3
def Menu3() :
    print()
    print('----------------------------')
    print('name  mid  final  grade')
    print('----------------------------')
    for name, scoreAr in students.items():
        print('%s   %d   %d     %s' %(name, scoreAr[0], scoreAr[1], scoreAr[2]))

##############  menu 4
def Menu4(name):
    del students[name]

students = {} #학생 정보 저장
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")

    if choice == "1" :
        stuInfo = input('Enter name mid-score final-score : ').split()
        if len(stuInfo) != 3:
            print('Num of data is not 3!')
        elif stuInfo[0] in students:
            print('Already exist name!')
        elif (not stuInfo[1].isdigit()) or (int(stuInfo[1]) <= 0) or (not stuInfo[2].isdigit()) or (int(stuInfo[2]) <= 0):
            print('Score is not positive integer!')
        else:
            Menu1(stuInfo[0], int(stuInfo[1]), int(stuInfo[2]))

    elif choice == "2" :
        if len(students) == 0:
            print('No student data!')
            continue

        Menu2()
        print('Grading to all students.')

    elif choice == "3" :
        if len(students) == 0:
            print('No student data!')
            continue

        flag = True
        for scoreAr in students.values():
            if len(scoreAr) == 2:
                print("There is a student who didn't get grade.")
                flag = False
                break

        if flag == True:
            Menu3()

    elif choice == "4" :
        if len(students) == 0:
            print('No student data!')
            continue
        
        name = input('Enter the name to delete : ')
        if not name in students:
            print('Not exist name!')
        else:
            Menu4(name)
            print(name, 'student information is deleted.')

    elif choice == "5" :
        print('Exit Program!')
        break

    else :
        print('Wrong number. Choose again.')