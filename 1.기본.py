print("Hello, world")
print('Hello, world')
print(100)
print(33.333)
print(100+23)

# 변수를 선언하고 값을 대입
num = 100   # 데이터형은 값이 대입되는 순간에 결정됨 -> 자료형을 자동 판단함 ( 파이썬의 장점이자 단점이 됨 )
print(num)
num = "100"

# 변수 활용
name = "곰돌이사육사"
email = "ks2024@gamail.com"
age = 25
addr = "서울시 강남구 역삼동 KH정보교육원"

# 주석 / 범위주석
"""
범위 주석 구간
2023. 09. 06
"""

'''
범위 주석 구간
2023. 09. 06
'''

print(f"""
이곳에 줄바꿈도 ok
이름 : {name}
이메일 : {email}
나이 : {age}
주소 : {addr}
""")

# 파이썬은 boolean값이 대문자로 시작함
is_adult = True

# 들여쓰기 사용
if is_adult :
    print("나는 성인 입니다.")
else :
    print("나는 성인이 아닙니다.")

# 리스트 출력
print([1, 2, 3]) 


