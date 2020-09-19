"""
Ex2. input 으로 10명의 "이름,학번,성적"을 입력 받아 list 로 관리
- input string 을 ['이름', '학번', '성적'] list 로 바꿔서 list 에 추가
- (학번, 성적은 integer 로 바꿔야함)
"""

student_num = 10
student_list = []
for _ in range(student_num):
    student_info = input("Name, Student ID, Score")
    student_info.replace(" ", "")  # remove blank
    [name, student_id, score] = student_info.split(",")  # split
    student_id, score = int(student_id), int(score)
    student_list.append([name, student_id, score])

for student in student_list:
    print(student)

