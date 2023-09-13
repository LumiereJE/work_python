# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분

# 입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다.
# 각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.
# 세변의 길이의 입력 순서는 정해져 있지 않다.

# 각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.


# 풀이
rst = []            # 결과를 출력하기 위한 빈 리스트
while True:
    li = list(map(int,input("세가지 숫자 입력 : ").split()))
    li.sort()                                                 # 계산하기 쉽도록 오름차순으로 정렬
    if li[0] == 0 and li[1] == 0 and li[2] == 0 :break        # 세 변이 0이면 break
    elif li[2] ** 2 == li[1] ** 2 + li[0] ** 2:               # 가장 긴 변의 제곱 = 나머지 두 변 제곱의 합
        rst.append("right")
    else:
        rst.append("wrong")

for e in rst: print(e)












