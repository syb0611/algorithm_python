# 그리디 알고리즘, 정렬

# ATM
# https://www.acmicpc.net/problem/11399

n = int(input()) # 사람 수
times = list(map(int, input().split())) # 돈 인출 시간
times.sort()  

sum = 0 # 줄 서는 시간 + 돈 인출하는 시간
total = 0 # 모든 사람이 돈 인출하는데 필요한 시간의 합의 최솟값

for time in times:
    sum += time
    total += sum

print(total)