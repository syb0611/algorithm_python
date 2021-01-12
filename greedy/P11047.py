# 그리디 알고리즘

# 동전 0
# https://www.acmicpc.net/problem/11047

coins = [] # 동전 종류
n, k = map(int, input().split()) # n : 동전의 종류 개수, k : 만들 동전의 가치
count = 0 # 필요한 동전 개수

# 동전 입력받기
for _ in range(n):
    coins.append(int(input()))

for i in range(1, n+1):
    if coins[-i] > k: # 만들려는 돈의 가치보다 동전의 가치가 크면 건너뛰고 다음 동전 비교 
        continue
    
    count += (k // coins[-i])
    k %= coins[-i]
    
    if k == 0:
        break

print(count)
