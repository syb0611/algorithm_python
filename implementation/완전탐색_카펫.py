# 프로그래머스 코딩테스트 연습
# 완전탐색 > 카펫 (Level 2)
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    xy = (brown - 4) // 2

    for i in range(1, xy//2+1):
        y = i
        x = xy - i

        if x * y == yellow:
            answer += [x+2, y+2]
    
    return answer

print(solution(24, 24))