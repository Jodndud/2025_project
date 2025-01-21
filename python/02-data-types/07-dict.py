# 딕셔너리 표현
my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple': 12, 'list':[1, 2, 3]}
print(my_dict_1)  # 
print(my_dict_2)  # 
print(my_dict_3)  # 


# 딕셔너리는 키에 접근해 값을 얻어냄
my_dict = {'apple': 12, 'list': [1, 2, 3]}
print(my_dict['apple'])
print(my_dict['list'])
print(my_dict['list'][1])
'''(참고)키 값은 불변 : 데이터의 정보를 줘야하기 때문'''

'''(메모)**
apple은 몇 번째 키? : 순서가 존재하지 않는다.
'''


# 추가
my_dict['banana'] = 50
print(my_dict)  # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}

# 변경
my_dict['apple'] = 100
print(my_dict)  # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}