n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result1 = 0
result2 = 0

result1 = first * (int(m / (k+1)) * k + m % (k+1))
result2 = second * (k+1)

print(result1 + result2)