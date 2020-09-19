"""
Ex3. shallow copy and deep copy test
- 새로운 예제 혹은 강의에 있는 예제로 shallow copy, deep copy test 후 간단한 설명 작성
- (동작에 대한 설명 필수, nested object 에 대한 예제는 필수로 포함)
"""
import copy

# SHALLOW COPY
# list2에 list1을 복사하였다.
# 메모리의 동일한 주소를 가리키고 있으므로 list1을 수정하면 그에 따라 list2도 수정된다.
list1 = [1, 2, [3, 4, 5]]
list2 = list1
list1[2][0] = 4
'''
[1, 2, [4, 4, 5]]
[1, 2, [4, 4, 5]]
'''
print(list1)
print(list2)

# DEEP COPY - using copy library
# copy library 의 deepcopy 를 이용했으므로 list4가 list3와 다른 주소를 가리키고 있다.
# 따라서 list3를 수정해도 list4에 영향이 없게 된다.
list3 = [1, 2, [3, 4, 5]]
list4 = copy.deepcopy(list3)
list3[2][0] = 4
'''
[1, 2, [4, 4, 5]]
[3, 4, 5]
'''
print(list3)
print(list4)

# DEEP COPY - using slicing
# slicing 을 이용해 deepcopy 를 수행했다.
# list6가 list5[2]와 다른 주소를 가리키고 있다.
# 따라서 list5를 수정해도 list6에는 영향이 없게 된다.
list5 = [1, 2, [3, 4, 5]]
list6 = list5[2][:]
list5[2][0] = 4
'''
[1, 2, [4, 4, 5]]
[3, 4, 5]
'''
print(list5)
print(list6)

# incomplete DEEP COPY - using slicing
# slicing 을 이용했지만 리스트 내부의 리스트는 같은 주소를 가리키고 있다.
# 완전한 deepcopy 가 이루어지지 않아 list7을 수정하면 list8도 그에 따라 수정된다.

list7 = [1, 2, [3, 4, 5]]
list8 = list7[:]
list7[2][0] = 4
'''
[1, 2, [4, 4, 5]]
[1, 2, [4, 4, 5]]
2649917196800
2649917196864
2649917196672
2649917196672

'''
print(list7)
print(list8)
print(id(list7))
print(id(list8))
print(id(list7[2]))
print(id(list8[2]))
