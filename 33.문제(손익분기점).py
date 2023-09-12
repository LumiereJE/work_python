# 고정비용 1000 fix
# 가변기용 70 var
# 판매비용 170 sell


fix, var, sell = map(int, input().split())

# 손익분기점 판매량 계산


if sell <= var:     # 예외처리 → 손익분기점에 도달할 수 없는 경우
    print(-1)       # 가변 비용이 판매 가격보다 높으면 손익분기점이 없음
else: print(fix // (sell - var) + 1)
















