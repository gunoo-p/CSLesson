# 1. 두 개의 값을 더하는 함수
def sum_num(num1, num2):
    # 입력 값 유효성 검사
    if num1 == "":
        res = "첫번째 숫자를 입력해주세요."
        return res
    elif num2 == "":
        res = "두번째 숫자를 입력해주세요."
        return res
    else:
        num3 = int(num1) + int(num2)
        res = f"두 숫자의 합은 {num3} 입니다."
        return res

num1 = input("첫번째 숫자를 입력해주세요 :")
num2 = input("두번째 숫자를 입력해주세요 :")

result = sum_num(num1, num2)

print(result)

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        
# 2. 이름과 나이를 입력받아 자기소개 출력하는 함수
def Introduction(name, age):
    if name == "":
        print("성함을 입력해주세요.")
    else:
        print(f"안녕하세요. 저는 {name}이고, 나이는 {age}살입니다.")


name = input("성함을 입력해주세요 :")
age = input("나이를 입력해주세요 :")

# 입력 값 유효성 검사
if age == "":
    age = 0
else:
    int(age)

# 자기소개 함수 호출
Introduction(name, age)   

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 3. 임의의 값을 더하는 함수 호출
def print_sum(text):
    total = 0
    for i in text:
        int(i)
        total += i
    print(total)

text = list(map(int, input("더하실 숫자들을 입력해주세요. 구분은 쉼표(,)로 해주세요. :").split(',')))

print_sum(text)
