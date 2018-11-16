def name_capitalize(name, acronym=False):
    temp = name.split("_")
    for i in range(len(temp)):
        if i == 0 and not acronym:
            continue
        temp[i] = temp[i].capitalize()
    return "".join(temp)


def function_name_capitalize(func, acronym=False):
    return name_capitalize(func.__name__, acronym)
