import re

def match_string(pattern, text):
    if re.search(pattern, text):
        return True
    else:
        return False

pattern = r'ab{2,3}'
text = input("Enter a string: ")

if match_string(pattern, text):
    print("String matches the pattern: 'a' followed by two to three 'b's")
else:
    print("String does not match the pattern: 'a' followed by two to three 'b's")
