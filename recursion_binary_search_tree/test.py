
def balanced_insert(arr):
    ret = []
    arr_len = len(arr)
    if arr_len == 0:
        return []
    median = (arr_len + (arr_len % 2)) // 2
    ret.append(arr[median - 1])

    for i in range(1, arr_len // 2 + 1):
        ret.append(arr[(median - 1) - i])
        if len(ret) != arr_len:
            ret.append(arr[(median - 1) + i])
    return ret

balanced_insert([])