my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list1 = [1, 2, 3 ,4 ]

i = 0
while i < len(my_list):
    if my_list[i] > 0:
        print(my_list[i])
        i += 1
    elif my_list[i] == 0:
        i += 1
    else:
        break
    if i > len(my_list) - 1:
        print('Я закончился')
        break


