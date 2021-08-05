pi = 3.1415926535897932
import turtle as t #turtle그래픽으로 원,부채꼴 그리기
import os

print('원의 넓이와 둘레, 부채꼴의 넓이와 호의 길이를 구하는 프로그램입니다.')
print('구하고자하는 원의 반지름을 입력해주세요.')
r = float(input())
if r == str:            #반지름 = r
    print('숫자가 아닙니다.')
else:
    print('구하고자 하는 것의 번호를 입력해주세요.')
    print('원=1, 부채꼴=2')
    number1 = int(input())    

    if number1 == 1: #원
        t.shape('classic')
        t.circle(r)
        circle_line = pi * r * 2
        circle_area = pi * r ** 2
        print('입력한 반지름을 가진 원의 둘레는', circle_line ,'이고, 넓이는', circle_area ,'입니다.')
        os.system("pause")
        

    elif number1 == 2:   #부채꼴
        print('값을 구하려 하는 부채꼴의 중심각을 입력해주세요.')
        midangle = float(input())
        pie_line = pi * r * 2 * ( midangle / 360 )
        pie_area = pi * r ** 2 * ( midangle / 360 )
        print('입력한 반지름을 가진 원의 부채꼴의 둘레는', pie_line ,'이고, 넓이는', pie_area ,'입니다.')
        

    else:
        print('nonono')