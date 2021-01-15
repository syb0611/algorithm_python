# 주유소
# https://www.acmicpc.net/problem/13305
# 그리디 알고리즘

n = int(input()) # n개 도시 입력받기
dists = list(map(int, input().split())) # 도시 간의 거리 입력받기
costs = list(map(int, input().split())) # 각 도시 주유소의 기름 가격 입력받기

min = costs[0] # 주유소 최소 기름 가격

result = 0 # 모든 도시 이동했을 때의 비용

for i in range(n-1): 
    if costs[i] < min: min = costs[i]

    result += min * dists[i]

print(result)

