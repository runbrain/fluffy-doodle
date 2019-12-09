import re

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = re.sub(r"[#%!@., ]", "", input('input text: ')).lower()
print(something)
if (is_palindrome(something)):
    print('fuck yeahh')
else:
    print('nooooop')
