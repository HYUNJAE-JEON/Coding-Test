order = [1, 2, 3, 4, 5, 6]
value = ["합", "격", "하", "고", "싶", "다"]

mydict = {order[i] : value[i] for i in range(len(order))}

print(mydict)