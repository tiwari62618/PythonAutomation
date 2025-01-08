cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Paris" in cities)
print("New Delhi" in cities)

l=(1,2,3,3,8,5,"amit")
print(l)


t = (12, 34, 56)
# t.append(12) # AttributeError: 'tuple' object has no attribute 'append'
my_list=list(t)
my_list.append(12)
my_list.append(2)
t=tuple(my_list)
print(t)

ENV_API_URLS = tuple(["abc.com/get", "xyz.com/post", "qwe.com/put"])
print(ENV_API_URLS)