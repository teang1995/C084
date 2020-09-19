"""
Ex4. integer 값으로 이루어진 두 개의 Set 을 만들어서 Union, intersection, difference,
Symmetric difference 확인
"""

setA = {1, 2, 3, 4, 6, 8, 12, 24}
setB = {1, 2, 3, 4, 36, 6, 9, 12, 18}

print("Union ", setA | setB)
print("Intersection : ", setA & setB)
print("B - A : ", setB - setA)
print("A - B : ", setA - setB)
print("Symmetrice Difference : ", (setA | setB) - (setA & setB))
