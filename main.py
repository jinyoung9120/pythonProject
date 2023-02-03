# print("Hello World!")
# print(1 + 5)
# print(1 * 5)
# print(5 / 2)
# print(5 % 2)
#
# professor = "Sungchul Choi"   #주석이에용~
# print(professor)
#
# a = 7  #변수할당 = 변수선언?
# b = 5
# print(a + b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a - b)
#
# print("a + b")
#
# # 주석주석주석 ctrl+/, #
#
# a = 1  #정수형
# b = 1
# print(a, b)
#
# a = 1.5 #실수형
# b = 3.5
# print(a, b)
#
# a = "ABC" #문자형
# b = "101010"
# print(a, b)
#
# a = True #불린형
# b = False
# print(a, b)
#
# print(2 ** 8) #2의 8승
# print(7 / 2)  #7나누기2
# print(7 // 2) #7나누기 2의 몫의 값만
#
# a = 1
# a = a + 1
# print(a)
#
# a += 1   #증가연산  +=을 띄면 안됌
# print(a)
#
# b = 1
# b = b - 1
# print(b)
#
# b -= 1  #감소연산  -=을 뜨면 안됌
# print(b)


# a = input()  #input은 기본적으로 문자취급
# print(a)
# print(type(a))

# a = input()
# b = input()
# print(a + b)
# # print(type(a))
# a = input()
# b = input()
# print(int(a) + int(b))  #a와 b 모두 숫자취급

# a = input()
# b = input()
# num1 = float(a)
# num2 = float(b)   # 여기도 a와 b 둘다 숫차쥐급해줌
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 % num2)
# print(num1 ** num2)
# print(num1 // num2)

# print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다.\n 변환하고 싶은 섭씨온도를 입력하세요")
# c = input()
# print("섭씨온도:",float(c))
# c = (float(c)*1.8+32)
# print ("화씨온도:", float(c))

#책
# celsius = input()
# fahrenheit = (float(celsius)*1.8)+32
# print("섭씨온도:",celsius)
# print("화씨온도:",fahrenheit)

#강사님이 알려준 또 다른 방법들
# print(f"사용자가 입력한 섭씨온도: {celisius} 입니다.")  비효율적
# print("섭씨온도" + celisius + "입니다")
# a = "섭씨온도는 {0},{1} 입니다.".format(selisius, fahrenhit)
#print(a)

# colors = ['red', 'blue', 'gree']
# print(colors[0])
# print(colors[2])
# print(len(colors))

# cities = ['서울','부산','인천','대구','대전','광주','울산','수원']
# print(cities[0:6])
# print(cities[5:])
# print(cities[-8:])

# color1 = ['red', 'blue', 'green']
# color2 = ['orenge', 'black', 'white']
# print(color1+color2)
#
# print(len(color1))  #리스트 길이
#
# total_color = color1+color2
# print(total_color)
#
# print('blue' in color1)  #존재여부확인
# print('blue' in color2)
#
# color1.append('purple')  #리스트에 추가하기
# print(color1)
#
# color2.extend(['black', 'white'])  #리스트에 추가하기
# print(color2)
#
# color = ['red', 'blue', 'green']
# color.insert(0,'orange')  #특정위치에 할당하기
# print(color)
#
# color.remove('red')  #지우기
# print(color)
#
# color = ['red', 'blue', 'green']
# color[0] = 'orange'   #0에 오렌지로 바꾸기(원래는 레드)
# print(color)
# del color[0]  #0번자리값지우기
# print(color)
#
# t = [1,2,3]
# a, b, c = t
# print(t, a, b, c)
#
# a_list = [1, 2, 3]
# b_list = [4, 5, 6]
# c_list = [a_list, b_list]
# print(c_list[0])
# print(c_list[1])

# kor_score = [49, 79, 20, 100, 80]
# math_score = [43, 59, 85, 30, 90]
# eng_score = [49, 79, 48, 60, 100]
# midterm_score = [kor_score, math_score, eng_score]
# print(midterm_score)
#
# print(midterm_score[0][2])
#
# math_score[0] = 1000
# print(math_score)
# print(midterm_score)

# print("I eat %d apples" % 3)  #정수넣기
# print("I eat %s apples" % "five") #문자열 넣기
# number = 3
# print("I eat %d apples" % number) #변수넣기
# print("I eat %0.2f apples" % 1.456456)  #소수점자리수 지정
# print("%10s" % "hi") #공백
# print("%-10sjane" % "hi")


print("다섯명의 파이썬 점수를 한명씩 입력해주세요")
phthon_score1 = input()
phthon_score2 = input()
phthon_score3 = input()
phthon_score4 = input()
phthon_score5 = input()

phthon_score = []
phthon_score.extend([phthon_score1, phthon_score2, phthon_score3, phthon_score4, phthon_score5])
p1, p2, p3, p4, p5 = phthon_score
kor_score = [85, 85, 85, 85, 85]
k1, k2, k3, k4 ,k5 = kor_score
eng_score = [80, 75, 90, 95, 85]
e1, e2, e3, e4 ,e5 = eng_score
math_score = [65, 95, 80, 75, 80]
m1, m2, m3, m4 ,m5 = math_score

print("%15s" % "성 적 표")
print("---------------------------------")
print("     국어 영어 수학 파이썬 평균")
print("장진영", k1,   e1,   m1,   p1) #"%0.2f" % ((k1+e1+m1+p1)/4)
print("최수연", k2,   e2,   m2,   p2) #"%0.2f" % ((k2+e2+m2+p2)/4)
print("김연화", k3,   e3,   m3,   p3) #"%0.2f" % ((k3+e3+m3+p3)/4)
print("장세원", k4,   e4,   m4,   p4) #"%0.2f" % ((k4+e4+m4+p4)/4)
print("한지훈", k5,   e5,   m5,   p5) #"%0.2f" % ((k5+e5+m5+p5)/4)
print("평균")


