num = int(input("Enter the number to check perfect square: "))
root = num ** 0.5
if (int(root)*int(root) == num):
    print(f"Number {num} is a perfect square")
else:
    print(f"Number {num} is not a perfect square!")