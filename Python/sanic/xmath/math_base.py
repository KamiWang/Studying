import math


digit_map = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
             'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def _radix_interger_convert(number, src_base, dst_base):
    base_10_num = int(number, src_base)
    if dst_base == 10:
        return str(base_10_num)
    temp = list()
    while base_10_num:
        temp.append(digit_map[base_10_num % dst_base])
        base_10_num //= dst_base
    temp.reverse()
    if not temp:
        temp.append('0')

    return "".join(temp)


def _radix_decimals_convert(number, src_base, dst_base):
    base_10_num = 0.0
    if 10 != src_base:
        for i in range(len(number)):
            x = int(number[i], 36)
            base_10_num += x * (src_base**-(i+1))
    else:
        base_10_num = float("0." + number)

    if dst_base == 10:
        return str(base_10_num).split('.')[1]

    temp = list()
    for _ in range(100):
        if 0 == base_10_num:
            break
        base_10_num *= dst_base
        temp.append(digit_map[int(str(base_10_num).split('.')[0])])
        base_10_num = math.modf(base_10_num)[0]

    return "".join(temp)


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

    if src_base < 2 or src_base > 36 or dst_base < 2 or dst_base > 36:
        raise ValueError("base must be >= 2 and <= 36")

    src_parts = str(src).split(".")
    result = _radix_interger_convert(src_parts[0], src_base, dst_base)

    if len(src_parts) > 1:
        decimals_str = _radix_decimals_convert(src_parts[1], src_base, dst_base)
        if decimals_str:
            result += '.' + decimals_str

    return result
