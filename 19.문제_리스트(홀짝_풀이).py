# 무작위 수를 공백 기준으로 입력받아 홀수와 짝수로 리스트에 나누어 담아 출력하는 형태

# num = list(map(int,input("입력 : ").split()))
# even = []
# odd = []
# for e in num:       # 향상된 for문
#     if e % 2 == 0: even.append(e)
#     else: odd.append(e)
# print(f"홀수 : {odd}")
# print(f"짝수 : {even}")

# map : 전달받은 값을 함수내부에서 적용시켜서 반환함. (입력 개수와 반환개수가 동일함)
# filter : 전달받은 값을 함수내부에서 조건에 일치하는 것만 골라서 반환함.

# 람다식 방법
num = list(map(int,input("입력 : ").split()))
odd = list(filter(lambda e: e % 2 == 1, num))     # 익명의 함수를 넣으려면 람다가 필요/ filter의 매개변수 자리는 조건
even = list(filter(lambda e: e % 2 == 0, num))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")











