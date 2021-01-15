# 회의실 배정
# https://www.acmicpc.net/problem/1931
# 그리디 알고리즘, 정렬

n = int(input()) # 회의실 수 입력받기
datas = [] # 회의 시작, 종료 시간 정보

for _ in range(n):
    start, end = map(int, input().split())
    datas.append((start, end))

# 회의 끝나는 시간 빠른 순으로 정렬, 똑같은 시간에 끝나면 먼저 시작하는 회의 우선 배정
datas = sorted(datas, key=lambda x: (x[1], x[0]))

count = 1 # 사용할 수 있는 회의 개수
end = datas[0][1] # 첫 회의 끝나는 시간

for data in datas[1:]:
    if data[0] >= end: # 다음 회의 시작 시간이 이전 회의 시간 이후면 회의실 사용 가능
        count += 1
        end = data[1]

print(count)