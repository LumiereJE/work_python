# 정수 n(0 < n < 1000)과 수의 목록이 주어졌을 때,
# 목록에 들어있는 수가 n의 배수인지 아닌지를 구하는 프로그램

# 첫째 줄에 n이 주어진다.
# 다음 줄부터 한 줄에 한 개씩 목록에 들어있는 수가 주어진다.
# 이 수는 0보다 크고, 10,000보다 작다.
# 목록은 0으로 끝난다.

# 받은 숫자들이 n의 배수인지 판별 → if


n = int(input("정수 n 입력 : "))
nums = list(map(int, input("0 ~ 10000 입력 : ").split(" ")))
for i in range(len(nums)):
    if nums[i] % n == 0:
        print(f"{nums[i]} is a multiple of {n}")
    elif not nums[i] % n == 0:
        print(f"{nums[i]} is NOT a multiple of {n}")
    else:pass

# 풀이
n = int(input())    # 디폴트가 문자열로 반환이기 때문에 정수타입으로 변환.
ls = []             # 빈 리스트 생성
while True:         # 0이 입력되기 전까지 반복수행
    x = (int(input()))                              # 목록의 수 입력받음
    if x == 0: break                                # 0이 입력되면 탈출
    ls.append(x)

for e in ls:
    if e % n == 0: print(f"{e} is a multiple of {n}.")
    else: print(f"{e} is NOT a multiple of {n}.")

















