def is_palindrome(word):
    if len(palindrome.middle(word)) == 1 and palindrome.first(word) == palindrome.last(word) :
            return True
    elif palindrome.middle(word) == '' and palindrome.first(word) == palindrome.last(word) :
            return True
    elif len(palindrome.middle(word)) == 1:
            return False
    elif palindrome.middle(word) == '':
            return False
    else:
            return is_palindrome(palindrome.middle(word))
