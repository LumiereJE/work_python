# 산술연산자 : 사칙연산자(+, -, *, /)
#            // (몫)
#            ** (제곱연산자)
#             % (나머지 연산자)

# 값을 대입할 때, 데이터 형이 결정됨 → 파이썬은 데이터형이 없기 때문.
i = 10
j = 3
print(f"덧셈 : {i+j}")    # f를 넣으면, 변수를 집어 넣겠단 뜻임!!!
print(f"뺄셈 : {i-j}")
print(f"곱셈 : {i*j}")
print(f"나눗셈 : {i/j}")
print(f"몫 : {i//j}")
print(f"나머지 : {i%j}")
print(f"제곱 연산자 : {i**j}")  # 10 * 10 * 10

test = "Python!!!"

print(test + "Hello")
print(test + str(100))        # 문자열 + 숫자열
print(test * 3)               # test 문자열을 2번 반복하겠다는 의미

print(f"증감연산자 시험 : {++i}")  # 파이썬은 증감 연산자가 없어서 써도 계산이 안됨.
i += 1
print(f"증감연산자 시험 : {i}")    # 이렇게는 가능.

# 간단예제 ---------------------------------------------

TAX_RATE = 0.10         # 고정값 상수는 대문자로. 그렇지만 파이썬은 상수 개념이 없음... 걍 없대 이유 없대 ㅋ ㅋ ㅋ
income = int(input("당신의 수입이 얼마입니까? "))
print(f"당신이 내야 할 세금은 {income * TAX_RATE:.2f}원 입니다.")    # .2f 소수점 2자리 찍겠다.

# -----------------------------------------------------

# 관계 연산자 : AND(&&) → and
#             OR(||) → or
#             NOT(!) → not

x = 10
y = 20
z = 30

rst1 = x > 0 and x > y      # False
rst2 = x > 0 or x > y       # True
rst3 = not(x > 0 or x > y)  # False

print(rst1, rst2, rst3, sep="\t")

# 파이썬은 0만 False임. 그 외는 모두 True / 자바는 1넣으면 False로 인식함

# 다항(3항) 연산자    (조건식) and 참인경우 or 거짓인경우
num = int(input("정수 입력 : "))
rst = (num % 2 == 0) and "짝수" or "홀수"       # 리액트의 경우 e => (e % 2 == 0) and "짝수" or "홀수"
print(f"{num}은 {rst}입니다.")

# 2진수 입력 받기 (0b)
number = 0b101010101

# 8진수 입력 받기 (0o)
number = 0o1234567

#16진수 입력 받기 (0x)
number = 0xffffff





