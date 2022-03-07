from palindrome import middle, last, first


def is_palindrome(word):
    if len(middle(word)) == 1 and first(word) == last(word):
        return True
    elif middle(word) == '' and first(word) == last(word):
        return True
    elif len(middle(word)) == 1:
        return False
    elif middle(word) == '':
        return False
    else:
        return is_palindrome(middle(word))
