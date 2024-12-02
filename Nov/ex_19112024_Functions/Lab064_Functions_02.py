def say_hello_default_argument(name="Pramod"):
    print("Hello", name.upper())

say_hello_default_argument("Dutta")
say_hello_default_argument()

def multiple_arguments(name1="A", name2="B"):
    print("Mult -> ", name1, name2)

multiple_arguments()
multiple_arguments("Lucky", "Sharma")
multiple_arguments(name1="Amit")
multiple_arguments(name1="Mohit", name2="Tiwari")

def sum_of_two_numbers(a,b):
    return a+b

result=sum_of_two_numbers(2,3)
print(result)

def sum_of_two_num_withdefault(num1=100,num2=200):
    return num1+num2
result=sum_of_two_num_withdefault()
print(result)
result=sum_of_two_num_withdefault(num1=32,num2=35)
print(result)
