import pandas as pd
import numpy as np

# 판다스 : 데이터 분석과 조작을 위한 라이브러리, 데이터를 구조화 하고 저장, 처리, 분석을 수행함

s1 = pd.Series([10,20,30,40,50])
print(s1) # 자동으로 index 번호가 생김
print(s1.index)
print(s1.values) # 우리가 보고싶어하는 결과값
print(s1.dtype)

# 판다스는 원소의 데이터 타입이 달라도 가능
s2 = pd.Series(['a', 'b', 'c', 1,2,3])
print(s2)
print(s2.dtype)

# 데이터가 없는 경우 넘파이 np.nan으로 표시 가능
s3 = pd.Series([np.nan, 10, 30])
print(s3)

# Series 데이터 생성 시, 인덱스 추가 기능
index_date = ['2023-09-15', '2023-09-16', '2023-09-17', '2023-09-18']
s4 = pd.Series([200, 195, np.nan, 345], index=index_date)
print(s4)

# 파이썬의 딕셔너리 이용 (java - Hash Map, js - object literal, json 과 같음)
# java의 map은 순회,, 하나씩 확인 filter와 헷갈림
s5 = pd.Series({'국어': 100, '영어':95, '수학': 90})
print(s5)

# 날짜 자동 생성 : date_range
s6 = pd.date_range(start='2023-09-16', end='2023-10-10')
print(s6)

# 달력을 요일을 기준으로 일주일씩 증가
s7 = pd.date_range(start='2023-09-16', periods=4, freq='W')
print(s7)

# 데이터프레임 : 데이터를 다룰 때 가장 많이 사용하는 데이터 형태로, 행과 열로 구성된 사각형 모양의 표 → 엑셀
df = pd.DataFrame({'name': ['민지', '하니', '혜린', '다니엘', '혜인'],
                   'kor': [90, 88, 97, 77, 92],
                   'eng': [88, 82, 87, 96, 97]
                   })
print(df)
print(df['kor'])
print(sum(df['kor'])/df['kor'].size) # 평균구하기

# 실습문제
df_fruit = pd.DataFrame({
    '제품': ['사과', '딸기', '수박'],
    '가격': [1800, 1500, 3000],
    '판매량': [24, 38, 13]
})

print(f"과일 평균 가격 : {sum(df_fruit['가격']) / df_fruit['가격'].size}")
print(f"평균 판매량 : {sum(df_fruit['판매량']) / df_fruit['판매량'].size}")

# 엑셀 파일 읽기
df_excel = pd.read_excel('./excel_exam.xlsx')
print(df_excel)

print(f"엑셀의 영어 점수 평균 : {sum(df_excel['english']) / df_excel['english'].size}")
print(f"엑셀의 수학 점수 평균 : {sum(df_excel['math']) / df_excel['math'].size}")

# csv(Comma Seperated Values)파일 읽기
df_csv = pd.read_csv('./exam.csv')
print(df_csv)

# 데이터프레임을 csv파일로 저장하기, 위의 변수(df_fruit) 이용
df_fruit.to_csv('과일 데이터 프레임.csv', index=False)








