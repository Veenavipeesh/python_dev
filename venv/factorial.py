fact = 1
num = int(input("Enter the number to find factorial: "))
for i in range(num,1,-1):
    fact *= i
print(f"Factorial of {num} is :{fact}")