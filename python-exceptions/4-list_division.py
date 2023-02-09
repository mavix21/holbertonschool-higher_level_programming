#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by zero")
            result = 0
        except (TypeError, ValueError):
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
        finally:
            div_list.append(result)

    return div_list
