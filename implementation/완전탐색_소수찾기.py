# 프로그래머스 코딩테스트 연습
# 완전탐색 > 소수찾기 (Level 2)
# https://programmers.co.kr/learn/courses/30/lessons/42839


from itertools import permutations

def solution(numbers):
    answer = 0 # 만들 수 있는 소수 개수
    case = set() # 모든 조합의 집합

    # 주어진 숫자 카드로 만들 수 있는 모든 조합의 수들 찾기
    for r in range(1, len(numbers)+1):
        case |= set(map(int, map(''.join, permutations(numbers, r))))

    # 모든 조합의 수 중에서 소수인 수 개수 구하기
    for num in case:
        if isPrime(num): 
            answer += 1
    
    return answer

# 값이 소수인지 확인하는 함수
def isPrime(num):
    if num < 2:
        return False

    for i in range(2, num) :
        if num % i == 0:
            return False
           
    return True 


numbers = "17"

print(solution(numbers))

