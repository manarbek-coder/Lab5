import re

def match_string(pattern, string):
    result = re.fullmatch(pattern, string)
    if result:
        print(f"String '{string}' matches the pattern '{pattern}'.")
    else:
        print(f"String '{string}' does not match the pattern '{pattern}'.")

pattern = r'a.*b$'

test_strings = []
num_tests = int(input("Enter the number of test strings: "))
for i in range(num_tests):
    test_string = input(f"Enter test string {i+1}: ")
    test_strings.append(test_string)

for test_string in test_strings:
    match_string(pattern, test_string)
