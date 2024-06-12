#  ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# ㅣ10개의 단어를 입력 받아 순서대로 출력하는 코드ㅣ
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
count = 0
resultArr = []

while count < 10:
    resultArr.append(input("단어를 하나씩 입력해주세요 :"))
    count += 1

for i in resultArr:
    print(i)