#!/usr/bin/python3
def element_at(my_list, id):
    if id < 0:
        return (None)

    length = len(my_list)

    if id > length - 1:
        return (None)

    return(my_list[id])
