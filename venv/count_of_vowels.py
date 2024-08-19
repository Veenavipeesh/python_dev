
word = input("Enter the string to count vowels: ")
count = 0
for i in word:
    if i in "AEIOUaeiou":
        count += 1
if (count > 0):
    print(f"Number of vowels in the given word is : {count}")
else:
    print("No vowels!")