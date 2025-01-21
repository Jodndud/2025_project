# 암시적 형변환
'''정수와 실수의 연산에서 정수가 실수로 변환됨
Boolean과 Numeric Type에서만 가능'''
print(3+5.0)
print(True + 3)
print(True + False)

# 명시적 형변환
print(int(3.5)) # X
print(int(3.5)) # 3
print(float('3.5')) # 3.5