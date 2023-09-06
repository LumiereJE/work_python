# 값을 할당하는 방법
a = b = c = 1
print(a, b, c)

# 여러개의 변수를 한번에 대입,
a, b, c = 1, False, "곰돌이사육사"
print(a, b, c)

# 타입 확인
# age = int(input("나이를 입력 하세요 : "))
# print(type(age))

value = 0o77        # 8진수
value = 0xffffff    # 16진수

print(value)

# boolean type : 참과 거짓의 값을 가짐.
print(bool(1))              # True
print(bool(0))              # False
print(bool(-1000))          # True
print(bool(""))             # False
print(bool(None))           # False, 값이 정해지지 않았음을 의미함.

# 문자열(str) 타입 :
str1 = "Hello Python!!"
print(str1)
print(str1[0])           # 인덱싱
print((str1[2:5]))       # 2 ~ 5 미만. → llo
print(str1[2:])          # 2 ~ 끝까지.
print(str1 * 5)          # 5번 출력됨
print(str1 + "TEST")

# 형변환 : 파이썬은 값이 할당되는 순간 형이 결정됨.
#         이후 데이터형을 변경하고자 할때 형 변환을 사용함.
print(10 + int("10"))
print("나이 : " + str(30))
aa = 10
print(1 + 3.141592 + float("4.44"))







