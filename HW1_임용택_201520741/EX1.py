"""
Ex1. loop 문으로 0 ~ 2PI (36 등분) 에 대한 cosine 의 양수 값과 음수 값을 각각 다른
array 로 저장하고 print 해보기
"""

import numpy as np

angle_list = [(i / 36.0) * 2 * np.pi for i in range(36)]
# print(angle_list) #DEBUG
negative_list = []
positive_list = []

for angle in angle_list:
    if np.cos(angle) > 0:
        positive_list.append(np.cos(angle))
    else:
        negative_list.append(np.cos(angle))


print("positive val")
for positive in positive_list:
    print(positive)

print("negative val")
for negative in negative_list:
    print(negative)

