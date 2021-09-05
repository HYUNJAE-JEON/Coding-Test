# 좌표 평면상에 현재 나이트가 위치한 곳 입력
n = input()
x = int(n[1])
y = n[0]
inty = 0

# y좌표 int로 바꾸기
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(len(list)):
  if y == list1[i]:
    inty = i + 1

# 경우의 수 구하기

count = 8
if x - 2 < 1:
  count -= 2
if x + 2 > 8:
  count -= 2
if y - 2 < 1:
  count -= 2
if y + 2 > 8:
  count -= 2

print(count)