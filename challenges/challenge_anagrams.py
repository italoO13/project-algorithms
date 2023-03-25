def merge_sort(lista, start=0, end=None):
    if end is None:
        end = len(lista)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(lista, start, mid)
        merge_sort(lista, mid, end)
        merge(lista, start, mid, end)
    return "".join(lista)


def merge(lista, start, mid, end):
    left = lista[start:mid]
    right = lista[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            lista[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            lista[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            lista[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            lista[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    first_string_sort = "".join(merge_sort(list(first_string.lower())))
    second_string_sort = "".join(merge_sort(list(second_string.lower())))

    if (
        first_string_sort == ""
        or second_string_sort == ""
        or len(first_string_sort) != len(second_string_sort)
    ):
        return (first_string_sort, second_string_sort, False)
    if first_string_sort not in second_string_sort:
        return (first_string_sort, second_string_sort, False)
    return (first_string_sort, second_string_sort, True)
