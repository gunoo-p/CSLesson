PI = 3.14159
radius = input("반지름 값을 입력해주세요. : ")

radius = int(radius)

area = PI * (radius ** 2)  
Circumference = 2 * PI * radius

print("반지름이", radius, "인 원의 넓이는", area, "입니다.")
print("반지름이", radius, "인 원의 둘레는", Circumference, "입니다.")