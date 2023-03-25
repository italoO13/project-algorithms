def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    tam = len(word) // 2
    if low_index == tam:
        return True
    elif word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
