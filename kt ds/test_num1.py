import sys

#data1 = sys.stdin.readline().rstrip()
#data2 = sys.stdin.readline().rstrip()
#data3 = sys.stdin.readline().rstrip()

data1, data2, data3, data4 = list(map(str, input().split()))

result1 = []
result2 = []
result3 = []
str1 = ''
str2 = ''
str3 = ''
count = 0

v = []
v.append(data1)
v.append(data2)
v.append(data3)
v.append(data4)

numarr = '1234567890'
strarr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
spearr = '!@#$%^&*'

for i in range(len(v)):
  for j in range(len(v[i])):
    for x in range(len(numarr)):
      if v[i][j] == numarr[x]:
        str1 += v[i][j]
    for y in range(len(strarr)):
      if v[i][j].upper() == strarr[y]:
        str2 += v[i][j].upper()
    for z in range(len(spearr)):
      if v[i][j] == spearr[z]:
        str3 += v[i][j]    
  result1.append(str1)
  str1 = ''
  result2.append(str2)
  str2 = ''
  result3.append(str3)
  str3 = ''

for i in range(len(v)):
  if len(result1[i]) != 0 and len(result2[i]) != 0 and len(result3[i]) != 0:
    pivot1 = len(result1[i]) // 2
    pivot2 = len(result2[i]) // 2
    pivot3 = len(result3[i]) // 2
    for j in range(0, pivot1):
      if result1[i][pivot1 - j] == result1[i][pivot1 + j]:
        count += 1
    for x in range(0, pivot2):
      if result2[i][pivot1 - x] == result2[i][pivot1 + x]:
        count += 1
    for y in range(0, pivot3):
      if result3[i][pivot1 - y] == result3[i][pivot1 + y]:
        count += 1
    if count == 3:
      print(len(v[i]))
  else:
    continue

print(result1)
print(result2)
print(result3)




