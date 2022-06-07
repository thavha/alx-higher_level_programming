#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n_list = []
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        for i in range(len(my_list)):
            if i == idx:
                n_list.append(element)
            else:
                n_list.append(my_list[i])
        return n_list
