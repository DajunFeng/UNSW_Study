def birthdayCakeCandles(ar):

    ar = sorted(ar)
    maximum_num = max(ar)
    first_max_index = ar.index(maximum_num)

    last_max_index = len(ar) - 1

    result = last_max_index - first_max_index + 1

    return result

