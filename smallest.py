def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a1 in list:
        if a1 < min:
            min = a1
    return min
print(smallest_num_in_list([1, 2, -8, 0]))
