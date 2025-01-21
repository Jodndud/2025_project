# 단축 평가
'''
and : 모두 참이어야 함(하나라도 거짓이면 거짓)
or : 하나라도 참이면 참(모두 거짓이어야 거짓)
'''

vowels = 'aeiou'

print(('a' and 'b') in vowels)  # ('a' and 'b')=참이고 'b'출력, vowels안에 없으므로 false
print(('b' and 'a') in vowels)  # ('b' and 'a')=참이고 'a'출력, vowels안에 있으므로 true
# '' = false

print(3 and 5)  # 5
print(3 and 0)  # 0
print(0 and 3)  # 0
print(0 and 0)  # 0

print(5 or 3)  # 5
print(3 or 0)  # 3
print(0 or 3)  # 3
print(0 or 0)  # 0