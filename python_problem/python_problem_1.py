num = 0
while True:
    while True:
        try:
            cnt = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
            if cnt<1 or cnt>3:
                print('1,2,3 중 하나를 입력하세요')
                continue
            break
        except ValueError:
            print('정수를 입력하세요')
    for i in range(cnt):
        num+=1
        print('playerA :', num)
        if num == 31: #게임 종료
            exit()

    while True:
        try:
            cnt = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
            if cnt<1 or cnt>3:
                print('1,2,3 중 하나를 입력하세요')
                continue
            break
        except ValueError:
            print('정수를 입력하세요')
    for i in range(cnt):
        num+=1
        print('playerB :', num)
        if num == 31: #게임 종료
            exit()