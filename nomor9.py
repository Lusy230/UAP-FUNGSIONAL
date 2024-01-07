data = range(10)
filterData = filter(lambda x : x%2==1, data)
mapping = map(lambda y : y*2, filterData)

print(data)
