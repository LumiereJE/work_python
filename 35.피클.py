import pickle

# 객체를 직렬화하여 파일에 저장하기 → 눈에 보이게 읽히진 않음, 기록 용도.
# data = {"name":"곰돌이사육사", "age":22, "addr": "서울시 강남구 역삼동"}
# with open("data.pickle", "wb") as file:
#     pickle.dump(data, file)

# 파일에서 객체를 역직렬화해서 복원하기  → 읽혀지면 끝임
with open("data.pickle", "rb") as file:
    restored_data = pickle.load(file)

print(restored_data)









