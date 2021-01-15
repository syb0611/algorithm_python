# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
# 수학, 그리디 알고리즘, 문자열, 파싱

exp = input() # 식 입력받기 ('0'~'9', '+', '-'로만 구성)
datas = exp.split('-')
list_add = []

for data in datas:
    arr = list(map(int, data.split('+')))
    list_add.append(sum(arr))
    
result = list_add[0] - sum(list_add[1:])    
print(result)



