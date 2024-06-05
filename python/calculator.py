#  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# ㅣ두 개의 값과 하나의 연산자를 받아와 계산하는 코드 ㅣ
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

num1 = int(input("첫번째 값을 입력해주세요. : "))
num2 = int(input("두번째 값을 입력해주세요. : "))
operator = input("연산자를 입력해주세요. :")

if operator == "+": #더하기
    print("입력하신", num1, "과", num2, "의 합은", num1 + num2, "입니다.") 
elif operator == "-": #빼기
    print("입력하신", num1, "과", num2, "의 차는", num1 - num2, "입니다.") 
elif operator == "*": #곱하기
    print("입력하신", num1, "과", num2, "의 곱은", num1 * num2, "입니다.") 
elif operator == "/": #나누기
    print("입력하신", num1, "과", num2, "를 나누면", num1 / num2, "입니다.") 
elif operator == "%": #나머지
    print("입력하신", num1, "과", num2, "의 나머지는", num1 % num2, "입니다.") 
elif operator == "//": #몫
    print("입력하신", num1, "과", num2, "의 몫은", num1 // num2, "입니다.") 
elif operator == "**": #거듭제곱
    print("입력하신", num1, "과", num2, "의 거듭제곱은", num1 ** num2, "입니다.")
elif operator != "+" and "-" and "*" and "/" and "%" and "//" and "**": # 연산자 입력 예외처리
    print("연산자 입력 값이 잘못되었습니다.")
