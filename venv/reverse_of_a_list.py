my_list = [2,5,7,8,9,15]
element_index = len(my_list) -1
print(len(my_list)-1)
print("Riversed list:")
reversed_list = []
while(element_index>=0):
    reversed_list.append(my_list[element_index])
    element_index -= 1
print(reversed_list)