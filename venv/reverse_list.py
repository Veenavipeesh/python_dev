my_list = [3,4,5,6,7,8,9,10]
reversed_list = []
for i in range(len(my_list)-1,-1,-1):
    reversed_list.append(my_list[i])
print(f"Given list is {my_list}")
print(f"Reversed list is {reversed_list}")