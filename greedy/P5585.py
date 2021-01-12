# 그리디 알고리즘

# 거스름돈
# https://www.acmicpc.net/problem/5585

coins = [500, 100, 50, 10, 5, 1] # 동전 종류

cost = int(input()) # 물건 가격
pay = 1000 # 지불한 가격
change = pay - cost # 거스름돈

count = 0 # 잔돈 동전 개수

for coin in coins:
    count += (change // coin)
    change %= coin

    if change == 0: break

print(count)


