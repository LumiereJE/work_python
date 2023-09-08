# 내장함수 : 파이썬이 기본적으로 제공, import가 필요없음
# 외장함수 : 파이썬이 기본적으로 제공, import가 필요함

# 큰값, 작은값 찾기
# print(max(1,2,3,4,5,45,88,6994,123,454,55))
# print(min(1,2,3,4,5,45,88,6994,123,454,55))
#
# # 총 합 구하기 → 리스트화 or 딕셔너리 해야함
# print(sum([1,2,3,4,5,45,88,6994,123,454,55]))       # 리스트로 총 합 구함
# print(sum((1,2,3,4,5,45,88,6994,123,454,55)))       # 튜플로 총 합 구함
# num = list(map(int, input("정수값 입력 : ").split()))
# print(f"입력받은 수의 총 합 : {sum(num)}")
# print(f"입력받은 수의 평균 : {sum(num)/len(num)}")

# 몫과 나머지 구하기
print(f"몫과 나머지 : {divmod(10, 4)}")              # divide mode의 약자. 튜플의 동작 원리와 흡사함. 두개의 반환값을 받음.

# 정렬
my_list = [1,2,3,4,5,45,88,6994,123,454,55]
print(sorted(my_list))                  # 오름차순
print(sorted(my_list, reverse=True))    # 내림차순





# 예제
# 여러개의 값을 한번에 입력 받아 리스트로 만들기
# 최대값 최소값 합계 평균 몫+나머지 구하기

ns = list(map(int, input("숫자 입력 (공백 이용) : ").split()))
print(f"최대값 : {max(ns)}")
print(f"최소값 : {min(ns)}")
print(f"합계 : {sum(ns)}")
print(f"평균 : {sum(ns) / len(ns)}")
print(f"몫+나머지 : {divmod(sum(ns), 5)}")









