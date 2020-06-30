kor,eng,math,sci=map(int,input().split())

avg= (kor+eng+math+sci)/4

if kor >100 or eng>100 or math>100 or sci > 100:
    print('잘못된 점수')
else:
    if avg>=80:
        print('합격')
    else:
        print('불합격')
    
