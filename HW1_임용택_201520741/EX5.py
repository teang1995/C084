"""
Ex5. String examples
C:\\USER\\.HATECOVID19\\KONO\\GAGOSIPDA\\python\\example.py # me too
위 주어진 string 을 아래와 같이 변경해보기
->C:\\USER\\.HATECOVID19\\KONO\\GAGOSIPDA\\python\\example_test.py
->C:\\USER\\.HATECOVID19\\KONO\\GAGOSIPDA\\python\\new_folder\\example.py
->C:\\USER\\.HATECOVID19\\KONO\\GAGOSIPDA\\python\\new_name.py
"""

src = "C:\\USER\\.HATECOVID19\\KONO\\GAGOSIPDA\\python\\example.py"
# 5 - 1
index_point = src.rfind(".")
print(index_point)
str1 = src[:index_point] + "_test.py"

# 5 - 2
split = src.split("\\")
split[-1] = "new_folder\\" + split[-1]
str2 = "\\".join(split)

# 5 - 3
split = src.split("\\")
split[-1] = "new_name.py"
str3 = "\\".join(split)

print(str1)
print(str2)
print(str3)