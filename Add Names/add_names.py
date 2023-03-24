def addNames(name_list, name_to_add):
    if name_to_add in name_list:
        print("Name already exist in the list", end="\n")
    else:
        name_list.append(name_to_add)
        print(name_list)