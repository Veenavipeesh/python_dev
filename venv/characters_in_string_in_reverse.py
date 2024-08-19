word = input("Enter the word to reverse: ")
reversed_word = ""
for i in range(len(word)-1,-1,-1):
   reversed_word += word[i]
print(f"Word {word} in reversed order is {reversed_word}")