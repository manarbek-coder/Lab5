def split_at_uppercase(string):
    result = []
    current_word = []

    for char in string:
        if char.isupper():
            if current_word:
                result.append(''.join(current_word))
                current_word = []
            current_word.append(char)
        else:
            current_word.append(char)

    if current_word:
        result.append(''.join(current_word))

    return result

input_string = input("Enter a string: ")

splitted_string = split_at_uppercase(input_string)

print("Split at uppercase letters:", splitted_string)
