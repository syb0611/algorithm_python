# 프로그래머스 코딩테스트 연습
# 완전탐색 > 모의고사 (Level 1)
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    
    answer = [] # 가장 높은 점수 받은 학생

    # a, b, c 학생이 문제 찍는 방식
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    corrects = [0, 0, 0] # 각 학생들이 문제 맞힌 개수

    # 문제 정답 확인하여 각 학생들의 문제 갯수 구하기
    for i in range(len(answers)):
        ans = answers[i]
        if (ans == a[i%len(a)]): corrects[0] += 1
        if (ans == b[i%len(b)]): corrects[1] += 1
        if (ans == c[i%len(c)]): corrects[2] += 1

    max_corrects = max(corrects) # 가장 높은 점수

    # 가장 높은 점수 받은 학생들 구하기
    for i in range(3):
        if corrects[i] == max_corrects: 
            answer.append(i+1)

    return answer

# 문제 정답 예제
answers = [1,3,2,4,2]

print(solution(answers))