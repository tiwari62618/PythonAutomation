#Create a program to sum of three numbers from the user input,
#if user doesn't enter any number', use default as 100, 200, 300

def sum_of_three_num(n1=100, n2=200, n3=300):
    return n1+n2+n3

num1=int(input("enter the num1\n"))
num2=int(input("enter the num2\n"))
num3=int(input("enter the num3\n"))

result=sum_of_three_num()
print(result)

print(sum_of_three_num(num1,num2,num3))


