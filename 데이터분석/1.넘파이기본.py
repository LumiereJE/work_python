# np : 넘파이의 약자
import numpy as np

# [] : 리스트 - 어떤 데이터든 올 수 있음
# {} : 딕셔너리
# () : 튜플 - 괄호가 없어도 튜플임

data1 = [0,1,2,3,4,5,6,7,8,9,10] # 리스트로 데이터 생성, 넘파이(배열)로 변환 하기 위해 정수만 사용함 → [0 1 2 3 4 5 6 7 8 9 10]
a1 = np.array(data1) #리스트를 넘파이 배열로 변환함
print(a1)

data2 = [0,1,2,3,4,5, 1.56, 3.14, 0.3333] # 정수도 실수 타입으로 바꿔주기
a2 = np.array(data2) # 실수로 변환(묵시적 타입캐스팅 - 자동 타입변환)
print(a2)

x = np.array([0.1, 0.2, 0.3])
print(x)
print(x.shape) # 배열의 형태를 튜플-행렬로 나타냄 (몇 행, 몇 열)
print(x.dtype) # 배열 요소의 type 확인

y = np.array(([1,2,3], [4,5,6])) # 2차원 배열 → 2행 3열
print(y)
print(y.shape)
print(y.dtype)

# 범위를 지정해 배열 생성
a3 = np.arange(0, 10, 2) # 0 ~ 10 미만, 간격(증가값) : 2
print(a3)

a4 = np.arange(1, 20) # 1 ~ 20 미만, 간격 : 1
print(a4)

# 배열 형태 변경, 0 ~ 12 미만 배열 생성 (초기값 없이, 최종값만 주면 0부터임)
a5 = np.arange(12).reshape(4, 3) # 배열의 구조를 변경 (4행 3열)
print(a5)
print(a5.shape)

# 배열의 시작과 끝 지정, 데이터의 갯수를 지정해 배열 생성, 갯수를 부여하면 간격을 알아서 계산함
a6 = np.linspace(1, 10, 4) # 시작, 끝, 갯수를 지정하면 시작과 끝 범위 내에서 분포됨
print(a6)
a7 = np.linspace(0, np.pi, 20)
print(a7)

# 특별한 형태의 배열 생성
# 1차원 배열
a8 = np.zeros(10) # 0으로 10개 채워진 배열 생성
print(a8)
a9 = np.zeros((3, 4)) # 3행 4열로 구성된 0으로 채워진 배열 생성
print(a9)
a10 = np.ones(10)
print(a10)
a11 = np.ones((5, 5))
print(a11)

# 단위 행열 생성 → n x n 정사각형의 행렬에서 주 대각선 방향으로 1이 진행됨
a12 = np.eye(4) # 4 x 4
print(a12)

# 배열의 타입 변환 : 배열은 숫자 뿐만 아니라 문자열도 요소로 가질 수 있음 (단, 같은 타입이어야함, 정수 + 실수면 실수로 형변환 됨)
a13 = np.array(['1.5', '0.62', '2', '3.14', '3.141592', '-12', '+12'])
print(a13)
print(a13.dtype)  # <U8 → 데이터 형식이 유니코드이며, 가장 긴 문자의 글자수가 8개라는 의미
# 유니코드 : 전세계 문자를 테이블로 넣어서 번호형태로 구분

num_a13 = a13.astype(float) # 문자열을 실수 타입으로 변환
print(num_a13)

# 난수 배열의 생성 : 0 ~ 1 미만의 임의의 실수형태로 난수를 발생시킴
a15 = np.random.rand(2,3) # 2행 3열로.
print(a15)
a16 = np.random.rand(2,3,4) # 3차원 배열. 2개 3행 4열
print(a16)

# 지정한 범위에 해당하는 정수로 난수 배열 생성
a17 = np.random.randint(10, size=(3,10)) # 0 ~ 10미만의 정수
print(a17)

# 배열의 연산 : 넘파이의 배열은 배열끼리 형태가 같다면 사칙 연산 수행 가능함 (java엔 없음)
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
result = arr1 ** arr2  # 제곱 2의 5제곱
print(result)

# 요소별 연산 : true, false로 반환
arr3 = np.array([10, 20, 30, 40, 50])
print(arr3 > 20)

# 통계를 위한 연산 : 배열의 합, 평균, 표준편차, 분산, 최소값, 최대값, 누적합, 누적동 등의 통계에서 많이 사용되는 메서드
arr4 = np.arange(5) # 0 ~ 5 미만의 값으로 구성된 배열 생성
print(f"합계 : {arr4.sum()}") # f"" → 포멧, JS의 ${}와 유사함
print(f"평균 : {arr4.mean()}")
print(f"표준편차 : {arr4.std()}")
print(f"분산 : {arr4.var()}")
print(f"최소값 : {arr4.min()}")
print(f"최댓값 : {arr4.max()}")

# 배열 인덱싱
arr5 = np.arange(1, 6)
print(arr5)
print(arr5[3]) # 3번째
print(arr5[0]) # 0번째

# 슬라이싱 : 값을 잘라냄
new_arr = arr5[1:3] # 1번 index ~ 3번 index 미만의 값을 슬라이싱
print(new_arr)

# Universal 함수 : 배열의 원소별 연산을 지원하는 함수
# 산술연산 : add(), substract(), multiply(), divide(), power()
# 삼각함수 : sin(), cos(), tan()
# 지수와 로그 : exp(), log(), log10()
# 집계함수 : sum(), mean(), max(), min()
# 논리함수 : logical_and(), logical_or(), logical_not()
xx = np.arange(0., 2*np.pi, 0.1)
print(np.pi)
yy = np.sin(xx)
print(yy)

matrix1 = np.array([[1,2], [4,5]])
matrix2 = np.array([[5,6], [7,8]])

# 행열 덧셈
res = np.add(matrix1, matrix2)
print(res)

# 정렬과 탐색 : 배열의 정렬과 탐색을 위한 함수와 메서드
xxx = np.array([9,8,7,2,3,4,6,11])
print(np.min(xxx))
print(np.amin(xxx)) # 배열 내의 최소값
print(np.max(xxx))
print(np.amax(xxx)) # 배열 내의 최댓값
print(np.argmin(xxx)) # 배열 내의 최소값의 위치
print(np.sort(xxx)) # 오름차순
print(np.sort(xxx)[::-1]) # 내림차순
print(np.argsort(xxx)) # 값의 인덱스 표시

# 브로드캐스팅 : 배열의 크기가 다른 경우에 연산을 수행하도록 해주는 기능
ax = np.array([1,2,3]) # 1차원 배열 (1줄)
bx = np.array([[4],[5],[6]]) # (3 x 1)로 구성 된 2차원 배열 (3줄)
cx = ax + bx
# [1,2,3] + 4씩
# [1,2,3] + 5씩
# [1,2,3] + 6씩
print(cx)
