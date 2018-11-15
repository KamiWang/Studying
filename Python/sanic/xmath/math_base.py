import math

digit_map = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
             'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def _radix_convert(number, src_base, dst_base, reverse=False):
    result_str = None
    base_10_num = int(number, src_base)

    if dst_base == 10:
        result_str = str(base_10_num)
        return result_str[::-1] if reverse else result_str

    temp = list()

    while base_10_num:
        temp.append(digit_map[base_10_num % dst_base])
        base_10_num //= dst_base

    temp.reverse()
    result_str = "".join(temp)

    return result_str[::-1] if reverse else result_str


def radix_convert(src, src_base: int = 0, dst_base: int = 10):
    if src_base == 0:
        if src[:2] == "0b":
            src_base = 2
        elif src[:2] == "0o":
            src_base = 8
        elif src[:2] == "0x":
            src_base = 16
        else:
            src_base = 10

    src_str = str(src).split(".")
    result = _radix_convert(src_str[0], src_base, dst_base)

    if len(src_str) > 1:
        result += '.' + _radix_convert(src_str[1], src_base, dst_base, True)

    return result
