'''(참고)
튜플의 불변 특성을 사용하여 내부 동작과 안전한 데이터 전달에 사용됨
다중 할당 x, y = 10, 20
값 교환 x,y=1,2 / x,y=y,x
그룹화
'''

# 튜플 표현
my_tuple_1 = ()
my_tuple_2 = (1,) 
'''(메모)
단일 요소 튜플을 만들때 후행쉼표를 사용해야함!
(1) => 소괄호가 벗겨지고 int=1이 됨
'''
my_tuple_3 = (1, 'a', 3, 'b', 5)

my_tuple = (1, 'a', 3, 'b', 5)

# 인덱싱
print(my_tuple[1])  # a

# 슬라이싱
print(my_tuple[2:4])  # (3, 'b')
print(my_tuple[:3])  # (1, 'a', 3)
print(my_tuple[3:])  # ('b', 5)
print(my_tuple[0:5:2])  # (1, 3, 5)
print(my_tuple[::-1])  # (5, 'b', 3, 'a', 1)

# 길이
print(len(my_tuple))  # 5

# 튜플은 불변
# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 'z'


# 다중 할당
x, y = 10, 20
print(x)  # 10
print(y)  # 20
# 실제 내부 동작
(x, y) = (10, 20)

# 값 교환
x, y = 1, 2
x, y = y, x
# 실제 내부 동작
temp = (y, x)  # 튜플 생성
x, y = temp  # 튜플 언패킹
print(x, y)  # 2 1

# 그룹화
student = ('Kim', 20, 'CS')
name, age, major = student  # 언패킹
print(name, age, major)  # Kim 20 CS
