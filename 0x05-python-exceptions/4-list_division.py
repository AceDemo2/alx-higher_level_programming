#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    li = []
    while i in range(list_length):
        try:
            n += my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            n = 0
        except ZeroDivisionError:
            print("ZeroDivisionError")
            n = 0
        except IndexError:
            print("out of range")
            n = 0
        finally:
            li += n
    return li
