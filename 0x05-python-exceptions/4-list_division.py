#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    l_div = []
    for i in range(list_length):
        try:
            l_div.append(my_list_1[i] / my_list_2[i])
        except (ZeroDivisionError, TypeError, IndexError) as err:
            if isinstance(err, ZeroDivisionError):
                print("division by 0")
            elif isinstance(err, TypeError):
                print("wrong type")
            elif isinstance(err, IndexError):
                print("out of range")
            l_div.append(0)
        finally:
            pass
    return l_div
