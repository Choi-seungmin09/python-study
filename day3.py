password = "0000"
count = 0

while count < 3:
    user_input = input("비밀번호를 입력해주세요: ")
    if user_input == password:
        print("환영합니다! ")
        break
    else:
        print("틀렸습니다")
        count += 1

if count == 3:
    print("3번 실패. 프로그램 종료.")
    