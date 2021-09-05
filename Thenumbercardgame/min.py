# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 가장 작은 수 찾기
  min_value = min(data)
  # 가장 작은 수 들 중에서 가장 큰 수 찾기 - 인자를 2개 넣음으로써 비교를 해서 하나씩 없애나가는 수순이다.
  result = max(result, min_value)
  print(result)

print(result) #최종 답안 출력