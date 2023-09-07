# 반복문 : 조건이 참인 동안 계속 수행되는 구문

# n = int(input("정수를 입력 하세요 : "))
# sum = 0             # 초기화
# while n:            # n > 0을 축약한 것임. 파이썬은 정수값이 0이 아니면 모두 참으로 간주함.
#     sum += n
#     n -= 1          # 파이썬은 증감연산자가 없어서 복합 대입 연산자로 구현해야 함.
# print(sum)

#---------------------------------------------------------------------------------

# while True:
#     age = int(input("나이를 입력 하세요 : "))
#     if 0 < age < 200 : break
#     print("나이 입력 범위를 벗어났습니다.")

#---------------------------------------------------------------------------------

# for 요소 in 시퀀스 : 시퀀스의 각 요소를 순회하는데에 사용함 (자바의 향상된 for문과 동일)
# fruits = ["apple", "banana", "cherry", ["seoul", "korea"]]      # 3차원 배열
# print(fruits[3][1][0])
# for e in fruits:
#     print(e[0])
#
# str1 = "서울시 강남구 역삼동 KH정보교육원"
# for e in str1:
#     print(e, end="/")

# for 변수 in rage (시작값, 종료값, 증감값):
# n = int(input("정수를 입력 하세요 : "))
# sum = 0
# for i in range(1, n+1):             # 1부터 n+1 미만!!!!!!!!!! 포함 안됨.
#     sum += i
# print(sum)

# for 문을 역순으로 반복하기
# for i in range(10, - 1, -1):      # 10 ~ 0 까지 출력, 0을 출력시킬려면 0 - 1 해야함
#     print(i)

# 이중 for문 - 별찍기
# n = int(input("정수를 입력 하세요 : "))
# for i in range(0, n):
#     for j in range(0, n):
#         print("*", end = ' ')
#     print()

# 구구단 찍기
# for i in range(2, 10):      # 2단 ~ 9단
#     for j in range(1, 10) : # 1 ~ 9 까지
#         print(f"{i} X {j} = {i*j}")
#     print()

# 홀수/짝수 나누어 찍기
# n = int(input("정수 입력 : "))
# for i in range(0, n):
#     for j in range(0, n):
#         if j % 2 == 0:              # 짝수일경우
#             print("$", end=' ')
#         else:
#             print("*", end=' ')
#     print()

# 사각형 행렬 찍기
# 정수값을 n을 입력받아 n * n크기의 행렬을 출력하는 프로그램 작성
# 값은 1부터 시작
# 4
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16

# n = int(input("정수입력 : "))
# for i in range(1, n * n + 1):
#     print(f"{i:>3}", end=' ')
#     if i % n == 0:print()

#-------------------------------------------------------------------------------------

# 별찍기

# *
# * *
# * * *
# * * * *
# * * * * *

# n = int(input("별 갯수 입력 : "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

#-------------------------------------------------------------------------------------

# * * * * *
# * * * *
# * * *
# * *
# *

# n = int(input("별 갯수 입력 : "))
# for i in range(n):
#     for j in range(n-i):
#         print("*", end=" ")
#     print()

#-------------------------------------------------------------------------------------

#   * * * * *
#    * * * *
#     * * *
#      * *
#       *

# n = int(input("별 갯수 입력 : "))

# for i in range(n):
#     for k in range(i):
#         print("", end=" ")
#     for j in range(n-i):
#         print("*", end=" ")
#     print()

# for i in range(n, 0, -1):
#     for s in range(n - i):
#         print("", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()

#-------------------------------------------------------------------------------------

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# n = int(input("별 갯수 입력 : "))
#
# for i in range(n):
#     for k in range(i):
#         print(" ", end=" ")
#     for j in range(n-i):
#         print("*", end=" ")
#     print()


#-------------------------------------------------------------------------------------

# 문자와 ASCII 코드
# chr : 유니코드 값을 입력받아 그 코드에 해당하는 문자를 출력
# ord : 문자를 유니코드 값으로 변환

for i in range(ord("A"), ord("Z")+1):       # A ~ Z 까지 순회
    print(chr(i), end=" ")
print()

for i in range(65, 91):
    print(chr(i), end=" ")
print()
