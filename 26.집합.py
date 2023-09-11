# 집합 : 주로 중복제거를 목적으로 자주 사용 됨.
# 순서가 보장되지 않음
# 중복 불가
# mutable 특성을 가짐

s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

# 중복제거
s3 = set([1,2,3,4,5,1,2,3,4,5,1,2,3])
print(s3)

# 합집합 : 집합에서 한군데만 존재하면 포함됨.
print(s1.union(s2))
print(s1 | s2)

# 교집합 : 집합에서 양쪽 모두에게 존재하는 요소만 선택.
print(s1.intersection(s2))
print(s1 & s2)

# 차집합 : 집합에서 앞에서 뒤를 빼개 해, 남은 앞의 요소만 선택함
print(s1.difference(s2))
print(s1 - s2)

import random
nums = set()
while True:
    num = random.randrange(1,46)
    nums.add(num)
    if len(nums) == 6: break

    print(nums)







