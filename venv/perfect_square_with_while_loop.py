num = int(input("Enter the number to check the perfect square: "))
i = 1
perfect_square_check = False
while (i <= num):
    if(int(i)*int(i) == num):
        perfect_square_check = True
    i += 1
if(perfect_square_check):
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square !")