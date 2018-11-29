#!/usr/bin/env python


def format_to_camel(name, sep='_', first_cap=False):
    temp = name.split(sep)
    for i in range(len(temp)):
        if not i and not first_cap:
            continue
        temp[i] = temp[i].capitalize()
    return "".join(temp)


def format_func_name_to_camel(func, sep='_', first_cap=False):
    return format_to_camel(func.__name__, sep, first_cap)


if "__main__" == __name__:
    print(format_func_name_to_camel(format_to_camel))
    pass
