while True:
    a=int(input('몇번 별을 꺼낼까요?'))
            # 1번 별
    def star(a):   
        if a == 1 :
            for i in range(5):
                for j in range(5):
                    print('*',end='')
                print()
            # 2번 별
        elif a ==2 :
            for i in range(5):
                for j in range(5):
                    if j <= i:
                        print('*',end='')
                print()
                # 3번 별
        elif a == 3:
            for i in range(5):
                for j in range(5-i):
                    print(' ',end='')
                for j in range(i+1):
                    print('*',end='')
                print()    
            # 4번 별
        elif a == 4:
            for i in range(6):
                for j in range(5-i):
                    print(' ',end='')
                for j in range(2*i-1):
                    print('*',end='')
                print()            
            #5번별
        elif a == 5:
            for i in range(3):
                for j in range(3-i):
                    print(' ',end='')
                for j in range(2*i-1):
                    print('*',end='')
                print()
            for i in range(3):
                for j in range(i):
                    print(' ', end = '')
                for k in range(5 - (i * 2)):
                    print('*', end = '')
                print()
            # 6번별
        elif a == 6:
            print('미완성 입니다 ㅜㅜ')
    star(a)# 별꺼내는 함수 실행
    if a >=7 : # 없는 번호 입력시 종료하기
        print('┌────────────────┐')
        print('│없는 별 번호 입니다. 종료합니다.│') # 함수 정의 끝
        print('└────────────────┘')
        break

            
            
