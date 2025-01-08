# writ a program to calculate even and odd

def find_even_odd(num):
   if num%2==0:
      print("even")
   else:
      print("odd")

find_even_odd(9)

n=int(input("Enter the number\n"))
check_even_odd = lambda num: "Even" if num%2==0 else "odd"
#print(check_even_odd(6))
print(check_even_odd(n))
