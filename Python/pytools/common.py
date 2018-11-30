#!/usr/bin/env python

import re


def format_identifier(identifier: str, rule=0) -> str:
    if rule < 0 or rule > 2:
        rule = 0

    if re.search(r"[^a-z\d]", identifier) is None:
        return identifier

    sep = re.search(r"[^a-zA-Z\d]", identifier)
    if sep is None:
        word_list = re.findall(r"([a-z\d]+[A-Z]|[A-Z]+)", identifier[::-1])[::-1]
    else:
        word_list = re.split(sep.string[sep.regs[0][0]:sep.regs[0][1]], identifier)

    for i in range(len(word_list)):
        if sep is None:
            word_list[i] = word_list[i][::-1]
        word_list[i] = word_list[i].lower()
        if rule == 2 or (rule == 0 and i == 0):
            continue
        word_list[i] = word_list[i].capitalize()

    if rule == 2:
        return "_".join(word_list)

    return "".join(word_list)


def format_function_identifier(func, rule=0) -> str:
    return format_identifier(func.__name__, rule)


def change_dict_value(dictionary: dict, key, delta):
    if key not in dictionary:
        dictionary[key] = 0
    dictionary[key] += delta
    return dictionary[key]


if "__main__" == __name__:
    pass
