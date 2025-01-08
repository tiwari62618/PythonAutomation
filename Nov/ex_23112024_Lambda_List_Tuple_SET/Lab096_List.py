# list-Collection of items
my_list=[1,2,3]
my_list2=[1,True,"Pramod",12.34]
print(my_list)
print(len(my_list))
print(my_list2[0])
print(my_list2[1])
print(my_list2[2])
print(my_list2[3])
#print(my_list2[4])--list index out of range
print("----------------")

my_list[0]="Pramod"
my_list[1]="Dutta"

for item in my_list:
    print(item)

print("----------------")

for item in my_list2:
    print(item)

#range(1,5) returns list[1,2,3,4]

for i in range(1,5):
    print(i, end=" ")





