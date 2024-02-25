import re


def replace_with_colon(text):
    pattern = r'[ ,.]'

    replaced_text = re.sub(pattern, ':', text)

    return replaced_text


text = input("Enter a string: ")

modified_text = replace_with_colon(text)

print("Modified text:", modified_text)
