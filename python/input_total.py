#  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# ㅣ100까지 입력받는 코드ㅣ
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
total = 0

while True:
    num = int(input("값을 입력해주세요 :"))

    if num >= 101: # 입력 값 예외처리
        print("100이상은 입력하시면 안됩니다.")
        break
    elif total + num >= 101:
        print(" 그 숫자를 더하면 100을 넘어가버려서 안돼", 100-total, "까지만 입력할 수 있어.")
        break

    total += num #누적
    print("현재 합계 :", total)
    
    if total >= 100:
        print("100 달성 종료합니다~")
        break
