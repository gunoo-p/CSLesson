#  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# ㅣ세 개의 숫자 중 가장 큰 수를 출력하는 코드ㅣ
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

num1 = int(input("첫번째 값을 입력해주세요. : "))
num2 = int(input("두번째 값을 입력해주세요. : "))
num3 = int(input("세번째 값을 입력해주세요. : "))

result1 = num1 > num2
result2 = num1 > num3
result3 = num2 > num3

if result1 == True and result2 == True:
    print("첫번째 숫자", num1, "가장 큽니다.")
elif result1 == False and result3 == True:
    print("두번째 숫자", num2, "가장 큽니다.")
else:
    print("세번째 숫자", num3, "가장 큽니다.")


