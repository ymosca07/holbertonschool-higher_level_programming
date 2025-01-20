def new_in_list(my_list, idx, element):
    
    duplicate = my_list[:]
    
    if idx < 0:
        return duplicate
    
    if idx > len(my_list):
        return duplicate
    
    duplicate[idx] = element

    return duplicate
