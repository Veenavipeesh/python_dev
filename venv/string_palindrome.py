word = input("Enter the string to check palindrome: ")
reversed_wrd = ""
for i in range(len(word)-1,-1,-1):
    reversed_wrd += word[i]
if word == reversed_wrd:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome !")