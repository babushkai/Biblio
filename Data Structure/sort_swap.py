for i in range(len(num_list)-1):
    for i in range(len(num_list)-1):
        if num_list[i]== 0:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]

