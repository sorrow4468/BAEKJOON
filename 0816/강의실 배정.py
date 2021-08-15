"""
실제 강의실 배정과 비슷하다
사용중인 강의실은 수업이 종료되기까지 다른 용도로 사용될 수 없다
과목은 N개
첫 강의 첫항목 초기화
다음강의 시작시간을 강의실들 전부 돌리면서 수업이 가능한지
불가능하면 새 강의실 추가
앞전 수업이 끝나서 강의실 안 만들 수 있으면
강의 가능한 강의실에 강의시간을 새로 저장

"""
N = int(input())
subjects = []
for n in range(N):
    subjects.append(list(map(int, input().split())))
classrooms = [subjects[0][1]]
for i in range(1, len(subjects)):
    if subjects[i][0] < classrooms[0]:
        classrooms.append(subjects[i][1])
    else:
        classrooms[0] = subjects[i][1]
        classrooms.reverse()
print(len(classrooms))