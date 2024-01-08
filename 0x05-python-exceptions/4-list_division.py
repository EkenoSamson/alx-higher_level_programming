#!/usr/bin/python3
# By Ekeno

def list_division(my_list_1, my_list_2, list_length):
    my_list = []

    for i in range(list_length):
        try:
            r = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            r = 0
            print("wrong type")
        except ZeroDivisionError:
            r = 0
            print("division by 0")
        except IndexError:
            r = 0
            print("out of range")
        finally:
            my_list.append(r)
#    print(my_list)
    return (my_list)
