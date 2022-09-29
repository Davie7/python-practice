def str_replace(int_list,index): 
    for index in range(len(int_list)):
        if int_list[index] == 1:
            int_list[index] = "small"
    print(int_list)
    
str_replace([1,2,3],0)

