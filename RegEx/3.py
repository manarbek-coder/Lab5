import re

def find_sequences(text):
    pattern = r'[a-z]+_[a-z]+'
    sequences = re.findall(pattern, text)
    return sequences

text = input("Enter a string: ")
result = find_sequences(text)
if result:
    print("Sequences found:", result)
else:
    print("No sequences found.")
