# list로 풀어야 함
# 영식 요금제 : 30초에 10원
# 민식 요금제 : 60초에 15원

# n = int(input())                                     # 통화 횟수
# call = list(map(int,input().split()))                # 통화 횟수 당 통화 시간
# y_pay = m_pay = 0
# for i in range(n):
#     y_pay += (call[i] // 30) * 10 + 10               # 30초당 10원 이어서 몫을 구하고 * 10
#     m_pay += (call[i] // 60) * 15 + 15
#
# if y_pay > m_pay:
#     print("M", m_pay)
# elif y_pay < m_pay:
#     print("Y", y_pay)
# else:
#     print("Y M", y_pay)


# 대소문자 바꾸기
# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력

# result = ""
# for e in input():       # 입력받는 문자열 만큼 자동 순회
#     if e.islower():     # 소문자 이면
#         result += e.upper()     # 대문자로 만들어서 문자열에 추가
#     else:
#         result += e.lower()     # 대문자 → 소문자로 변환해서 문자열에 추가
# print(result)



# 숫자의 개수
# A = 150, B = 266, C = 427이라면 A × B × C = 150 × 266 × 427 = 17037300
# 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력  → 굳이 숫자일 필요는 없음

a, b, c = map(int, input("정수 3개 입력 : ").split())

total_val = str(a * b * c)      # a * b * c 결과를 문자열로 변환
for i in range(10):
    print(total_val.count(str(i)))      # (str(i))의 갯수














