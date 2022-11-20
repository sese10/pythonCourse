def isPalindrome(s):
    # reverse the string
    rev = ''.join(reversed(s))
    # Checking if both string are equal or not
    if s == rev:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


data = 'aIbohPhoBiA' #'mIyojRIoBiA'
# making all latters caseless comparison
my_data = data.casefold()
print(my_data)
isPalindrome(my_data)
