# 무작위 수를 공백으로 기준하여 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력 하는 문제 입니다.

# map(int,input().split())

print("입력 : ")
num = list(map(int,input().split()))

even = []
odd = []

for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f"짝수 : {even}")
print(f"홀수 : {odd}")


















