# 계좌 개설
def open_account(name):
    print(f"{name}님의 계솨가 개설 되었습니다.")
    return name                                # 반환값으로 이름을 전달

# 입금 함수
def deposit(balance, input):                   # 잔고와 입금액을 매개변수로 전달받음
    print(f"{input}원이 입급되었습니다. 잔액은 {balance+input}원 입니다.")
    return balance + input

# 출금 함수
def withdraw(balance, output):
    if balance >= output:
        print(f"{output}이 출금 되었습니다. 잔액은 {balance - output}원 입니다.")
        return balance - output
    else:
        print(f"출금을 실패했습니다. 잔액은 {balance}원 입니다.")
        return balance

balance = 0                                    # 0으로 초기화. 외부에서 선언했지만 매개변수로 전달하여 결과를 리턴받음
name = open_account("곰돌이사육사")
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
print(f"{name}의 잔액은 {balance}원 입니다.")









